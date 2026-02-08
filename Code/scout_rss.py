#!/usr/bin/env python3
"""
SCOUT RSS Reader + News Processor (MVP)
- RSS/Atom ingestion -> SQLite
- Deduplication (GUID/URL/title)
- Lightweight enrichment (CVE extraction + keyword/entity tagging)
- Transparent scoring + status workflow
- Obsidian note publishing (staging or final)

Dependencies:
  pip install feedparser requests

Usage (from SCOUT launcher via subprocess):
  python scout_rss.py init
  python scout_rss.py collect
  python scout_rss.py list --status new --limit 30
  python scout_rss.py show NEWS-...
  python scout_rss.py mark NEWS-... --status flagged
  python scout_rss.py publish --status flagged --dest staging
  python scout_rss.py publish --status flagged --dest final

Config:
  Expects config.json next to this script (or next to exe if frozen),
  with an "rss" section (see example at bottom of this file).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import feedparser  # type: ignore
import requests  # type: ignore


# -------------------------------
# PyInstaller-friendly path resolution
# -------------------------------
def get_app_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


# -------------------------------
# Config
# -------------------------------
_TOKEN_RE = re.compile(r"\{([A-Z0-9_]+)\}")

def _expand_tokens(s: str, app_dir: Path) -> str:
    """
    Expands {APP_DIR}, {HOME}, and environment variables {VARNAME}.
    """
    if not isinstance(s, str):
        return s
    mapping = {
        "APP_DIR": str(app_dir),
        "HOME": str(Path.home()),
    }

    def repl(m: re.Match) -> str:
        key = m.group(1)
        if key in mapping:
            return mapping[key]
        return os.environ.get(key, m.group(0))

    return _TOKEN_RE.sub(repl, s)

def load_config(app_dir: Path) -> dict:
    cfg_path = app_dir / "config.json"
    if not cfg_path.exists():
        raise FileNotFoundError(f"Missing config.json next to application: {cfg_path}")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))

    # Expand tokens recursively for strings
    def walk(x: Any) -> Any:
        if isinstance(x, dict):
            return {k: walk(v) for k, v in x.items()}
        if isinstance(x, list):
            return [walk(v) for v in x]
        if isinstance(x, str):
            return _expand_tokens(x, app_dir)
        return x

    return walk(cfg)


# -------------------------------
# Helpers
# -------------------------------
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.IGNORECASE)

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def iso_date(d: datetime) -> str:
    return d.astimezone(timezone.utc).strftime("%Y-%m-%d")

def safe_filename(s: str, max_len: int = 140) -> str:
    s = s.strip()
    s = re.sub(r"[\\/:*?\"<>|]", "-", s)
    s = re.sub(r"\s+", " ", s)
    s = s.replace(" - ", " – ")
    if len(s) > max_len:
        s = s[:max_len].rstrip()
    return s

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8", errors="ignore")).hexdigest()

def canonicalize_url(url: str) -> str:
    """
    MVP canonicalization: strip common tracking params and fragments.
    """
    if not url:
        return url
    url = url.split("#", 1)[0]
    # Remove common tracking params very conservatively
    # (We do not do full URL parsing to keep MVP tight.)
    for token in ["utm_source=", "utm_medium=", "utm_campaign=", "utm_term=", "utm_content=", "gclid=", "fbclid="]:
        if token in url:
            base = url.split("?", 1)[0]
            return base
    return url

def parse_entry_datetime(entry: dict) -> datetime:
    """
    feedparser provides entry.published_parsed / updated_parsed (time.struct_time).
    """
    for key in ("published_parsed", "updated_parsed"):
        if key in entry and entry[key]:
            tt = entry[key]
            return datetime(tt.tm_year, tt.tm_mon, tt.tm_mday, tt.tm_hour, tt.tm_min, tt.tm_sec, tzinfo=timezone.utc)
    # Fallback: now
    return datetime.now(timezone.utc)


# -------------------------------
# Data model (in-code)
# -------------------------------
@dataclass
class FeedDef:
    name: str
    url: str
    category: str = "general"
    enabled: bool = True
    tags: List[str] = None

@dataclass
class NewsItem:
    news_id: str
    title: str
    url: str
    source: str
    published_utc: datetime
    ingested_at: str
    summary: str
    content_text: str
    cves: List[str]
    vendors: List[str]
    products: List[str]
    threat_actors: List[str]
    tags: List[str]
    tlp: str
    confidence: int
    severity_estimate: int
    relevance_score: int
    status: str


# -------------------------------
# SQLite
# -------------------------------
SCHEMA_SQL = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS feeds (
  feed_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  url TEXT NOT NULL UNIQUE,
  category TEXT,
  enabled INTEGER NOT NULL DEFAULT 1,
  tags_json TEXT
);

CREATE TABLE IF NOT EXISTS entries_raw (
  entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
  feed_id INTEGER NOT NULL,
  guid TEXT,
  title TEXT,
  link TEXT,
  published TEXT,
  summary TEXT,
  raw_json TEXT,
  seen_at TEXT NOT NULL,
  UNIQUE(feed_id, guid),
  FOREIGN KEY(feed_id) REFERENCES feeds(feed_id)
);

CREATE TABLE IF NOT EXISTS news_items (
  news_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  source TEXT NOT NULL,
  published TEXT NOT NULL,
  ingested_at TEXT NOT NULL,
  summary TEXT,
  content_text TEXT,
  entities_json TEXT,
  tlp TEXT,
  confidence INTEGER,
  severity_estimate INTEGER,
  relevance_score INTEGER,
  status TEXT NOT NULL,
  obsidian_path TEXT
);

CREATE INDEX IF NOT EXISTS idx_news_status ON news_items(status);
CREATE INDEX IF NOT EXISTS idx_news_published ON news_items(published);
"""

def db_connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn

def db_init(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)
    conn.commit()

def db_upsert_feeds(conn: sqlite3.Connection, feeds: List[FeedDef]) -> None:
    cur = conn.cursor()
    for f in feeds:
        tags_json = json.dumps(f.tags or [])
        cur.execute(
            """
            INSERT INTO feeds(name, url, category, enabled, tags_json)
            VALUES(?, ?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
              name=excluded.name,
              category=excluded.category,
              enabled=excluded.enabled,
              tags_json=excluded.tags_json
            """,
            (f.name, f.url, f.category, 1 if f.enabled else 0, tags_json),
        )
    conn.commit()

def db_list_feeds(conn: sqlite3.Connection) -> List[sqlite3.Row]:
    return conn.execute("SELECT * FROM feeds WHERE enabled=1 ORDER BY name").fetchall()

def db_insert_raw_entry(conn: sqlite3.Connection, feed_id: int, guid: str, title: str, link: str,
                        published: str, summary: str, raw_json: str) -> bool:
    """
    Returns True if inserted, False if duplicate.
    """
    try:
        conn.execute(
            """
            INSERT INTO entries_raw(feed_id, guid, title, link, published, summary, raw_json, seen_at)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (feed_id, guid, title, link, published, summary, raw_json, utc_now_iso()),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def db_news_exists(conn: sqlite3.Connection, news_id: str) -> bool:
    row = conn.execute("SELECT 1 FROM news_items WHERE news_id=?", (news_id,)).fetchone()
    return row is not None

def db_insert_news_item(conn: sqlite3.Connection, ni: NewsItem) -> None:
    entities = {
        "cves": ni.cves,
        "vendors": ni.vendors,
        "products": ni.products,
        "threat_actors": ni.threat_actors,
        "tags": ni.tags,
    }
    conn.execute(
        """
        INSERT INTO news_items(
          news_id, title, url, source, published, ingested_at, summary, content_text,
          entities_json, tlp, confidence, severity_estimate, relevance_score, status, obsidian_path
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ni.news_id,
            ni.title,
            ni.url,
            ni.source,
            ni.published_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            ni.ingested_at,
            ni.summary,
            ni.content_text,
            json.dumps(entities),
            ni.tlp,
            ni.confidence,
            ni.severity_estimate,
            ni.relevance_score,
            ni.status,
            None,
        ),
    )
    conn.commit()

def db_list_news(conn: sqlite3.Connection, status: str, limit: int) -> List[sqlite3.Row]:
    return conn.execute(
        """
        SELECT news_id, published, source, relevance_score, status, title, url
        FROM news_items
        WHERE status=?
        ORDER BY relevance_score DESC, published DESC
        LIMIT ?
        """,
        (status, limit),
    ).fetchall()

def db_get_news(conn: sqlite3.Connection, news_id: str) -> Optional[sqlite3.Row]:
    return conn.execute("SELECT * FROM news_items WHERE news_id=?", (news_id,)).fetchone()

def db_mark_status(conn: sqlite3.Connection, news_id: str, status: str) -> None:
    conn.execute("UPDATE news_items SET status=? WHERE news_id=?", (status, news_id))
    conn.commit()

def db_set_obsidian_path(conn: sqlite3.Connection, news_id: str, path: str, new_status: str) -> None:
    conn.execute(
        "UPDATE news_items SET obsidian_path=?, status=? WHERE news_id=?",
        (path, new_status, news_id),
    )
    conn.commit()


# -------------------------------
# Enrichment + scoring
# -------------------------------
def normalize_text(s: str) -> str:
    s = s or ""
    s = re.sub(r"\s+", " ", s).strip()
    return s

def extract_cves(text: str) -> List[str]:
    cves = sorted({m.group(0).upper() for m in CVE_RE.finditer(text or "")})
    return cves

def find_from_dictionary(text: str, dictionary: List[str]) -> List[str]:
    """
    Case-insensitive contains match; returns canonical (dictionary) forms.
    """
    hits = []
    t = (text or "").lower()
    for term in dictionary or []:
        if term and term.lower() in t:
            hits.append(term)
    return sorted(set(hits))

def keyword_tags(text: str, rules: Dict[str, List[str]]) -> List[str]:
    t = (text or "").lower()
    tags = []
    for tag, keys in (rules or {}).items():
        for k in keys:
            if k.lower() in t:
                tags.append(tag)
                break
    return sorted(set(tags))

def score_item(
    text: str,
    cves: List[str],
    vendors: List[str],
    products: List[str],
    actors: List[str],
    tags: List[str],
    source: str,
    cfg_rss: dict
) -> Tuple[int, int, int, str, int]:
    """
    Returns: (relevance_score, severity_estimate, confidence, tlp, source_tier)
    """
    weights = cfg_rss.get("scoring", {}).get("weights", {})
    source_tiers = cfg_rss.get("source_tiers", {})  # { "high": [...], "medium": [...], "low": [...] }
    default_tier = cfg_rss.get("scoring", {}).get("default_source_tier", "medium")

    def tier_for_source(src: str) -> str:
        for tier, srcs in source_tiers.items():
            if any((s.lower() == src.lower()) for s in (srcs or [])):
                return tier
        return default_tier

    tier = tier_for_source(source)
    tier_weight = cfg_rss.get("scoring", {}).get("source_tier_weight", {"high": 10, "medium": 0, "low": -10})
    score = 0

    if cves:
        score += int(weights.get("has_cve", 25))
    if vendors:
        score += int(weights.get("tracked_vendor", 20))
    if products:
        score += int(weights.get("tracked_product", 20))
    if actors:
        score += int(weights.get("tracked_actor", 15))

    # Keyword-based boosts
    # (tags already derived from keyword rules)
    score += int(weights.get("tag_hit", 5)) * min(len(tags), 5)

    # High-signal phrases
    high_signal = cfg_rss.get("scoring", {}).get("high_signal_phrases", [])
    t = (text or "").lower()
    if any(p.lower() in t for p in high_signal):
        score += int(weights.get("high_signal_phrase", 20))

    score += int(tier_weight.get(tier, 0))

    # Clamp
    score = max(0, min(100, score))

    # Severity estimate (very rough MVP)
    severity = 1
    if score >= 85:
        severity = 4
    elif score >= 70:
        severity = 3
    elif score >= 40:
        severity = 2

    # Confidence (1-5, lower is higher confidence is not aligned; you used 1-high for attribution.
    # For MVP, use 1-5 where 1=high confidence.)
    confidence = 3
    if tier == "high":
        confidence = 2
    elif tier == "low":
        confidence = 4

    tlp = cfg_rss.get("default_tlp", "TLP:CLEAR")

    tier_numeric = {"high": 3, "medium": 2, "low": 1}.get(tier, 2)
    return score, severity, confidence, tlp, tier_numeric


# -------------------------------
# Publishing to Obsidian
# -------------------------------
def write_obsidian_note(
    vault_root: Path,
    dest_folder: str,
    ni_row: sqlite3.Row,
    entities: dict,
    banner_path: str,
) -> Path:
    """
    Writes a flat-YAML Obsidian note and returns the file path.
    """
    published_dt = datetime.strptime(ni_row["published"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    date_str = iso_date(published_dt)
    source = ni_row["source"]
    title = ni_row["title"]

    filename = safe_filename(f"{date_str} - {source} - {title}.md")
    out_dir = vault_root / dest_folder
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    # Avoid collisions
    if out_path.exists():
        stem = out_path.stem
        out_path = out_dir / f"{stem} ({ni_row['news_id'][:8]}).md"

    # YAML (flat keys)
    yaml = {
        "entity_type": "news_item",
        "news_id": ni_row["news_id"],
        "title": title,
        "source": source,
        "source_url": ni_row["url"],
        "published": date_str,
        "ingested": ni_row["ingested_at"][:10],
        "tlp": ni_row["tlp"] or "TLP:CLEAR",
        "status": ni_row["status"],
        "relevance_score": int(ni_row["relevance_score"] or 0),
        "cves": entities.get("cves", []),
        "vendors": entities.get("vendors", []),
        "products": entities.get("products", []),
        "threat_actors": entities.get("threat_actors", []),
        "tags": entities.get("tags", []),
        "related_notes": [],
        "banner": banner_path,
    }

    def dump_yaml_flat(d: dict) -> str:
        lines = ["---"]
        for k, v in d.items():
            if isinstance(v, list):
                lines.append(f"{k}: {json.dumps(v)}")
            elif isinstance(v, (int, float)):
                lines.append(f"{k}: {v}")
            else:
                # Quote strings safely
                sv = "" if v is None else str(v)
                sv = sv.replace('"', '\\"')
                lines.append(f'{k}: "{sv}"')
        lines.append("---")
        return "\n".join(lines)

    summary = normalize_text(ni_row["summary"] or "")
    content = normalize_text(ni_row["content_text"] or "")

    body_lines = [
        dump_yaml_flat(yaml),
        "",
        "# Summary",
        "",
        f"- {summary}" if summary else "- (No summary provided by source.)",
        "",
        "# Key Entities",
        "",
    ]

    if entities.get("cves"):
        body_lines.append(f"- CVEs: {', '.join(entities['cves'])}")
    if entities.get("vendors"):
        body_lines.append(f"- Vendors: {', '.join(entities['vendors'])}")
    if entities.get("products"):
        body_lines.append(f"- Products: {', '.join(entities['products'])}")
    if entities.get("threat_actors"):
        body_lines.append(f"- Threat Actors: {', '.join(entities['threat_actors'])}")
    if entities.get("tags"):
        body_lines.append(f"- Tags: {', '.join(entities['tags'])}")

    body_lines += [
        "",
        "# Source",
        "",
        f"- URL: {ni_row['url']}",
        "",
        "# Notes",
        "",
        "- Analyst actions:",
        "  - [ ] Determine relevance to our environment",
        "  - [ ] If urgent, create an ITID and link here",
        "  - [ ] If active incident, link to Incident note",
        "",
    ]

    # Keep content optional to avoid dumping large scraped text into vault
    if content:
        body_lines += ["# Extract (MVP)", "", content[:4000].strip(), ""]

    out_path.write_text("\n".join(body_lines), encoding="utf-8")
    return out_path


# -------------------------------
# Collector
# -------------------------------
def fetch_feed(url: str, timeout: int = 20, tls_cfg: dict | None = None) -> feedparser.FeedParserDict:
    """
    Fetch RSS/Atom feed with configurable TLS behavior.
    """
    tls_cfg = tls_cfg or {}

    verify = tls_cfg.get("verify", True)
    ca_bundle_path = (tls_cfg.get("ca_bundle_path") or "").strip()

    # requests.verify can be: True | False | path-to-ca-bundle
    verify_arg = ca_bundle_path if ca_bundle_path else verify

    headers = {
        "User-Agent": "SCOUT-RSS/1.0 (+local)",
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml",
    }
    print(f"[DEBUG] fetch_feed verify_arg={verify_arg} url={url}")
    r = requests.get(
        url,
        headers=headers,
        timeout=timeout,
        verify=verify_arg
    )
    r.raise_for_status()
    return feedparser.parse(r.content)

def _safe_str(x) -> str:
    return "" if x is None else str(x)

def _rss_fp(item: dict) -> str:
    """
    Stable fingerprint for state tracking.
    Prefer URL; fallback to source||title.
    """
    url = _safe_str(item.get("url")).strip()
    if url:
        return url
    src = _safe_str(item.get("source")).strip()
    title = _safe_str(item.get("title")).strip()
    return f"{src}||{title}"

def _fmt_when(s: str) -> str:
    """
    Render a published timestamp in a compact way if possible.
    Accepts ISO-ish strings; otherwise returns as-is.
    """
    s = _safe_str(s).strip()
    if not s:
        return ""
    try:
        # Handle common formats; keep it tolerant
        dt = None
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            dt = None
        if dt:
            # local-ish display
            return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        pass
    return s

def _mk_markdown_from_item(item: dict, tags=None, notes: str = "") -> str:
    """
    Minimal, Obsidian-friendly markdown payload for copy/export.
    """
    title = _safe_str(item.get("title")).strip() or "Untitled"
    url = _safe_str(item.get("url")).strip()
    source = _safe_str(item.get("source")).strip()
    published = _safe_str(item.get("published")).strip()
    summary = _safe_str(item.get("summary")).strip()
    content = _safe_str(item.get("content")).strip()

    tags = tags or []
    tags_yaml = "[" + ", ".join([f'"{t}"' for t in tags if _safe_str(t).strip()]) + "]"

    fm = [
        "---",
        'entity_type: "rss_article"',
        f'title: "{title.replace(chr(34), chr(39))}"',
        f'source: "{source.replace(chr(34), chr(39))}"' if source else 'source: ""',
        f'published: "{published.replace(chr(34), chr(39))}"' if published else 'published: ""',
        f'url: "{url.replace(chr(34), chr(39))}"' if url else 'url: ""',
        f"tags: {tags_yaml}",
        "---",
        "",
    ]

    body = [f"# {title}", ""]
    if url:
        body.append(url)
        body.append("")
    if summary:
        body.append("## Summary")
        body.append(summary)
        body.append("")
    if content and content != summary:
        body.append("## Content")
        body.append(content)
        body.append("")
    if notes:
        body.append("## Analyst Notes")
        body.append(notes)
        body.append("")

    return "\n".join(fm + body)

def build_news_id(source: str, url: str, title: str) -> str:
    base = f"{source}|{canonicalize_url(url)}|{title.strip().lower()}"
    return "NEWS-" + sha256_hex(base)[:24].upper()

def collect(cfg: dict) -> Tuple[int, int]:
    """
    Returns (feeds_processed, items_inserted).
    """
    app_dir = get_app_dir()
    rss_cfg = cfg.get("rss", {})
    db_path = Path(rss_cfg.get("db_path", str(app_dir / "data" / "rss_news.db")))
    conn = db_connect(db_path)
    db_init(conn)

    # Load feeds from config into DB (idempotent)
    feed_defs = []
    for f in (rss_cfg.get("feeds") or []):
        feed_defs.append(
            FeedDef(
                name=f.get("name", "Unnamed Feed"),
                url=f.get("url", ""),
                category=f.get("category", "general"),
                enabled=bool(f.get("enabled", True)),
                tags=f.get("tags", []) or [],
            )
        )
    db_upsert_feeds(conn, feed_defs)

    feeds = db_list_feeds(conn)
    inserted = 0

    tracked_vendors = rss_cfg.get("tracked", {}).get("vendors", []) or []
    tracked_products = rss_cfg.get("tracked", {}).get("products", []) or []
    tracked_actors = rss_cfg.get("tracked", {}).get("threat_actors", []) or []
    tag_rules = rss_cfg.get("tag_rules", {}) or {}

    for f in feeds:
        feed_id = int(f["feed_id"])
        source = f["name"]
        url = f["url"]

        try:
            parsed = fetch_feed(
                url,
                timeout=int(rss_cfg.get("http_timeout", 20)),
                tls_cfg=rss_cfg.get("tls", {})
)

        except Exception as e:
            print(f"[WARN] Feed fetch failed: {source} ({url}) -> {e}")
            continue

        for entry in parsed.entries:
            guid = entry.get("id") or entry.get("guid") or entry.get("link") or sha256_hex(entry.get("title", ""))
            title = normalize_text(entry.get("title", "") or "")
            link = canonicalize_url(entry.get("link", "") or "")
            published_dt = parse_entry_datetime(entry)
            published_iso = published_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            summary = normalize_text(entry.get("summary", "") or entry.get("description", "") or "")

            raw_json = json.dumps({k: entry.get(k) for k in entry.keys()}, default=str)

            if not title or not link:
                continue

            # Insert raw entry; skip if we've already seen GUID for this feed
            if not db_insert_raw_entry(conn, feed_id, str(guid), title, link, published_iso, summary, raw_json):
                continue

            # Canonical news item
            news_id = build_news_id(source, link, title)
            if db_news_exists(conn, news_id):
                continue

            # Enrichment input text
            text = f"{title}\n{summary}"

            cves = extract_cves(text)
            vendors = find_from_dictionary(text, tracked_vendors)
            products = find_from_dictionary(text, tracked_products)
            actors = find_from_dictionary(text, tracked_actors)
            tags = keyword_tags(text, tag_rules)

            score, severity, confidence, tlp, _tier_num = score_item(
                text=text,
                cves=cves,
                vendors=vendors,
                products=products,
                actors=actors,
                tags=tags,
                source=source,
                cfg_rss=rss_cfg,
            )

            # Status routing
            status = "new"
            if score >= int(rss_cfg.get("scoring", {}).get("auto_flag_threshold", 85)):
                status = "flagged"

            ni = NewsItem(
                news_id=news_id,
                title=title,
                url=link,
                source=source,
                published_utc=published_dt,
                ingested_at=utc_now_iso(),
                summary=summary,
                content_text="",  # MVP: do not scrape full text by default
                cves=cves,
                vendors=vendors,
                products=products,
                threat_actors=actors,
                tags=tags,
                tlp=tlp,
                confidence=int(confidence),
                severity_estimate=int(severity),
                relevance_score=int(score),
                status=status,
            )

            db_insert_news_item(conn, ni)
            inserted += 1

    conn.close()
    return (len(feeds), inserted)


# -------------------------------
# CLI
# -------------------------------
def cmd_init(cfg: dict) -> int:
    app_dir = get_app_dir()
    rss_cfg = cfg.get("rss", {})
    db_path = Path(rss_cfg.get("db_path", str(app_dir / "data" / "rss_news.db")))
    conn = db_connect(db_path)
    db_init(conn)

    # Sync feeds into DB
    feed_defs = []
    for f in (rss_cfg.get("feeds") or []):
        feed_defs.append(
            FeedDef(
                name=f.get("name", "Unnamed Feed"),
                url=f.get("url", ""),
                category=f.get("category", "general"),
                enabled=bool(f.get("enabled", True)),
                tags=f.get("tags", []) or [],
            )
        )
    db_upsert_feeds(conn, feed_defs)
    conn.close()

    print(f"[OK] Initialized DB at: {db_path}")
    print(f"[OK] Feeds synced from config.json")
    return 0

def cmd_collect(cfg: dict) -> int:
    feeds_processed, items_inserted = collect(cfg)
    print(f"[OK] Feeds processed: {feeds_processed}")
    print(f"[OK] New items inserted: {items_inserted}")
    return 0

def cmd_list(cfg: dict, status: str, limit: int) -> int:
    app_dir = get_app_dir()
    rss_cfg = cfg.get("rss", {})
    db_path = Path(rss_cfg.get("db_path", str(app_dir / "data" / "rss_news.db")))
    conn = db_connect(db_path)

    rows = db_list_news(conn, status=status, limit=limit)
    if not rows:
        print("(no results)")
        return 0

    for r in rows:
        print(f"{r['news_id']} | {r['published']} | {r['source']} | {int(r['relevance_score']):3d} | {r['title']}")
        print(f"  {r['url']}")
    return 0

def cmd_show(cfg: dict, news_id: str) -> int:
    app_dir = get_app_dir()
    rss_cfg = cfg.get("rss", {})
    db_path = Path(rss_cfg.get("db_path", str(app_dir / "data" / "rss_news.db")))
    conn = db_connect(db_path)

    r = db_get_news(conn, news_id)
    if not r:
        print(f"[ERR] Not found: {news_id}")
        return 2

    entities = json.loads(r["entities_json"] or "{}")
    print(f"news_id: {r['news_id']}")
    print(f"title:   {r['title']}")
    print(f"source:  {r['source']}")
    print(f"url:     {r['url']}")
    print(f"published: {r['published']}")
    print(f"score:   {r['relevance_score']}  severity: {r['severity_estimate']}  confidence: {r['confidence']}  tlp: {r['tlp']}")
    print(f"status:  {r['status']}")
    if r["obsidian_path"]:
        print(f"obsidian_path: {r['obsidian_path']}")
    print("")
    print("entities:")
    print(json.dumps(entities, indent=2))
    print("")
    print("summary:")
    print(r["summary"] or "")
    return 0

def cmd_mark(cfg: dict, news_id: str, status: str) -> int:
    allowed = {"new", "reviewed", "flagged", "published", "ignored"}
    if status not in allowed:
        print(f"[ERR] Invalid status: {status}. Allowed: {sorted(allowed)}")
        return 2

    app_dir = get_app_dir()
    rss_cfg = cfg.get("rss", {})
    db_path = Path(rss_cfg.get("db_path", str(app_dir / "data" / "rss_news.db")))
    conn = db_connect(db_path)

    if not db_get_news(conn, news_id):
        print(f"[ERR] Not found: {news_id}")
        return 2

    db_mark_status(conn, news_id, status)
    print(f"[OK] {news_id} -> status={status}")
    return 0

def cmd_publish(cfg: dict, status: str, dest: str, limit: int) -> int:
    """
    Publish items in a given status to Obsidian and mark as published.
    dest: "staging" or "final"
    """
    if dest not in {"staging", "final"}:
        print("[ERR] dest must be 'staging' or 'final'")
        return 2

    app_dir = get_app_dir()
    rss_cfg = cfg.get("rss", {})
    db_path = Path(rss_cfg.get("db_path", str(app_dir / "data" / "rss_news.db")))
    vault_root = Path(rss_cfg.get("vault_root", ""))
    if not str(vault_root).strip():
        print("[ERR] rss.vault_root is not set in config.json")
        return 2

    staging_folder = rss_cfg.get("staging_folder", "00_System/99_Inbox/_staging/21_News")
    publish_folder = rss_cfg.get("publish_folder", "20_Intelligence/21_News")
    banner_path = rss_cfg.get("banner_path", "99_Attachments/SCOUT_Obsidian_Banner.png")

    dest_folder = staging_folder if dest == "staging" else publish_folder

    conn = db_connect(db_path)
    rows = db_list_news(conn, status=status, limit=limit)
    if not rows:
        print("(no results)")
        return 0

    published_count = 0
    for r in rows:
        full = db_get_news(conn, r["news_id"])
        if not full:
            continue
        entities = json.loads(full["entities_json"] or "{}")

        out_path = write_obsidian_note(
            vault_root=vault_root,
            dest_folder=dest_folder,
            ni_row=full,
            entities=entities,
            banner_path=banner_path,
        )
        rel_path = str(out_path.relative_to(vault_root))
        db_set_obsidian_path(conn, full["news_id"], rel_path, new_status="published")
        published_count += 1

        print(f"[OK] Published: {full['news_id']} -> {rel_path}")

    print(f"[OK] Total published: {published_count}")
    return 0


def main() -> int:
    app_dir = get_app_dir()
    cfg = load_config(app_dir)

    p = argparse.ArgumentParser(prog="scout_rss.py", description="SCOUT RSS Reader + News Processor (MVP)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="Initialize SQLite DB and sync feeds from config.json")
    sub.add_parser("collect", help="Poll all enabled feeds and ingest new items")

    lp = sub.add_parser("list", help="List news items by status")
    lp.add_argument("--status", default="new", choices=["new", "reviewed", "flagged", "published", "ignored"])
    lp.add_argument("--limit", type=int, default=30)

    sp = sub.add_parser("show", help="Show a single news item")
    sp.add_argument("news_id")

    mp = sub.add_parser("mark", help="Mark a news item status")
    mp.add_argument("news_id")
    mp.add_argument("--status", required=True, choices=["new", "reviewed", "flagged", "published", "ignored"])

    pp = sub.add_parser("publish", help="Publish items to Obsidian and mark published")
    pp.add_argument("--status", default="flagged", choices=["new", "reviewed", "flagged", "published", "ignored"])
    pp.add_argument("--dest", default="staging", choices=["staging", "final"])
    pp.add_argument("--limit", type=int, default=50)

    args = p.parse_args()

    if args.cmd == "init":
        return cmd_init(cfg)
    if args.cmd == "collect":
        return cmd_collect(cfg)
    if args.cmd == "list":
        return cmd_list(cfg, status=args.status, limit=args.limit)
    if args.cmd == "show":
        return cmd_show(cfg, args.news_id)
    if args.cmd == "mark":
        return cmd_mark(cfg, args.news_id, args.status)
    if args.cmd == "publish":
        return cmd_publish(cfg, status=args.status, dest=args.dest, limit=args.limit)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())


"""
---------------------------------------
Example config.json snippet (add to yours)
---------------------------------------

{
  "rss": {
    "db_path": "{APP_DIR}/data/rss_news.db",
    "vault_root": "C:/path/to/your/SCOUT/Vault",

    "staging_folder": "00_System/99_Inbox/_staging/21_News",
    "publish_folder": "20_Intelligence/21_News",
    "banner_path": "99_Attachments/SCOUT_Obsidian_Banner.png",

    "http_timeout": 20,
    "default_tlp": "TLP:CLEAR",

    "feeds": [
      {
        "name": "Bleeping Computer",
        "url": "http://www.bleepingcomputer.com/feed/",
        "category": "advisory",
        "enabled": true,
        "tags": ["news", "advisory"]
      },      
    ],

    "tracked": {
      "vendors": ["Microsoft", "Cisco", "Palo Alto", "Fortinet", "Ivanti", "VMware", "Okta"],
      "products": ["Exchange", "Active Directory", "Citrix", "PAN-OS", "FortiOS", "Connect Secure"],
      "threat_actors": ["Scattered Spider", "APT29", "Lazarus", "FIN7"]
    },

    "tag_rules": {
      "ransomware": ["ransomware", "extortion", "encrypt", "double extortion"],
      "exploitation": ["exploited in the wild", "active exploitation", "in the wild", "0-day", "zero-day"],
      "phishing": ["phishing", "credential theft", "BEC", "business email compromise"],
      "vulnerability": ["cve-", "buffer overflow", "remote code execution", "rce", "privilege escalation"]
    },

    "source_tiers": {
      "high": ["CISA Alerts"],
      "medium": ["KrebsOnSecurity"],
      "low": []
    },

    "scoring": {
      "auto_flag_threshold": 85,
      "default_source_tier": "medium",
      "source_tier_weight": { "high": 10, "medium": 0, "low": -10 },
      "high_signal_phrases": ["actively exploited", "in the wild", "proof of concept", "poc released"],
      "weights": {
        "has_cve": 25,
        "tracked_vendor": 20,
        "tracked_product": 20,
        "tracked_actor": 15,
        "tag_hit": 5,
        "high_signal_phrase": 20
      }
    }
  }
}

---------------------------------------
Launcher integration (typical subprocess)
---------------------------------------
- Collect now:  python scout_rss.py collect
- Review queue: python scout_rss.py list --status new --limit 50
- Publish flagged to staging: python scout_rss.py publish --status flagged --dest staging
- Publish flagged to final:   python scout_rss.py publish --status flagged --dest final
"""
