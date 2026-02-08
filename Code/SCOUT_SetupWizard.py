import json
import os
import sys
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog


TOKEN_KEYS = ["APP_DIR", "USER_HOME", "USERNAME", "LOCALAPPDATA", "APPDATA"]


def get_app_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def _read_config_file(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_config_file_with_backup(path: Path, cfg: dict) -> None:
    if path.exists():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        bak = path.with_name(f"{path.stem}.bak.{ts}{path.suffix}")
        try:
            bak.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        except Exception:
            pass
    path.write_text(json.dumps(cfg, indent=2), encoding="utf-8")


def _set_nested(cfg: dict, keys: list, value):
    cur = cfg
    for key in keys[:-1]:
        if key not in cur or not isinstance(cur[key], dict):
            cur[key] = {}
        cur = cur[key]
    cur[keys[-1]] = value


def _get_nested(cfg: dict, keys: list, default=None):
    cur = cfg
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def _looks_like_token(value: str) -> bool:
    if not value:
        return False
    if "{" in value and "}" in value:
        return True
    if "%" in value or "$" in value:
        return True
    return False


class WizardPage(ttk.Frame):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master)
        self.cfg_ref = cfg_ref
        self._validation_callback = None

    def load_from_cfg(self):
        pass

    def save_to_cfg(self) -> bool:
        return True

    def set_validation_callback(self, callback):
        self._validation_callback = callback

    def _notify_valid(self, is_valid: bool):
        if self._validation_callback:
            self._validation_callback(bool(is_valid))

    def validate_all(self) -> bool:
        return True

    def _add_token_button(self, parent, entry):
        btn = ttk.Menubutton(parent, text="Tokens")
        menu = tk.Menu(btn, tearoff=0)
        for token in TOKEN_KEYS:
            menu.add_command(
                label=f"{{{token}}}",
                command=lambda t=token: entry.insert(tk.INSERT, f"{{{t}}}")
            )
        btn["menu"] = menu
        return btn


class PathsPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.fields = {}
        self._build()

    def _add_path_row(self, row, label, key_path, is_file=False, is_dir=False, required=False):
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", padx=6, pady=4)
        var = tk.StringVar()
        entry = ttk.Entry(self, textvariable=var, width=70)
        entry.grid(row=row, column=1, sticky="we", padx=6, pady=4)
        self.fields[tuple(key_path)] = {
            "var": var,
            "entry": entry,
            "is_file": is_file,
            "is_dir": is_dir,
            "required": required,
        }

        btns = ttk.Frame(self)
        btns.grid(row=row, column=2, sticky="w", padx=6, pady=4)
        if is_file or is_dir:
            def browse():
                if is_file:
                    path = filedialog.askopenfilename()
                else:
                    path = filedialog.askdirectory()
                if path:
                    var.set(path)

            ttk.Button(btns, text="Browse", command=browse).grid(row=0, column=0, padx=2)
        self._add_token_button(btns, entry).grid(row=0, column=1, padx=2)
        err = tk.Label(self, text="", fg="#E05A5A", anchor="w")
        err.grid(row=row + 1, column=1, columnspan=2, sticky="w", padx=6, pady=(0, 4))
        self.fields[tuple(key_path)]["error"] = err

        var.trace_add("write", lambda *_args, k=tuple(key_path): self._on_field_change(k))

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="Paths & Vault", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", padx=6, pady=(6, 10)
        )
        fields = [
            ("SCOUT_ROOT", ["paths", "SCOUT_ROOT"], False, True, True),
            ("CIPHER_ROOT", ["paths", "CIPHER_ROOT"], False, True, False),
            ("VAULT_ROOT", ["paths", "VAULT_ROOT"], False, True, True),
            ("DAILY_NOTES_DIR", ["paths", "DAILY_NOTES_DIR"], False, False, False),
            ("OBSIDIAN_EXE", ["paths", "OBSIDIAN_EXE"], True, False, True),
            ("OBSIDIAN_VAULT", ["paths", "OBSIDIAN_VAULT"], False, False, False),
            ("DAILY_NOTES_REL", ["paths", "DAILY_NOTES_REL"], False, False, False),
            ("RSS_DB", ["paths", "RSS_DB"], True, False, False),
        ]
        row = 1
        for label, key_path, is_file, is_dir, required in fields:
            self._add_path_row(
                row,
                label,
                key_path,
                is_file=is_file,
                is_dir=is_dir,
                required=required
            )
            row += 2

    def load_from_cfg(self):
        for key_path, info in self.fields.items():
            info["var"].set(_get_nested(self.cfg_ref, list(key_path), "") or "")
        self.validate_all()

    def save_to_cfg(self) -> bool:
        if not self.validate_all():
            return False
        for key_path, info in self.fields.items():
            _set_nested(self.cfg_ref, list(key_path), info["var"].get().strip())
        return True

    def _validate_field(self, key_path):
        info = self.fields[key_path]
        val = info["var"].get().strip()
        err = ""
        if info["required"] and not val:
            err = "Required."
        elif val and not _looks_like_token(val):
            path = Path(val)
            if info["is_dir"]:
                if not path.exists():
                    err = "Folder not found."
                elif not path.is_dir():
                    err = "Not a folder."
            if info["is_file"]:
                if not path.exists():
                    err = "File not found."
                elif not path.is_file():
                    err = "Not a file."
        info["error"].configure(text=err)

    def validate_all(self) -> bool:
        valid = True
        for key_path, info in self.fields.items():
            val = info["var"].get().strip()
            err = ""
            if info["required"] and not val:
                err = "Required."
            elif val and not _looks_like_token(val):
                path = Path(val)
                if info["is_dir"]:
                    if not path.exists():
                        err = "Folder not found."
                    elif not path.is_dir():
                        err = "Not a folder."
                if info["is_file"]:
                    if not path.exists():
                        err = "File not found."
                    elif not path.is_file():
                        err = "Not a file."
            info["error"].configure(text=err)
            if err:
                valid = False
        return valid

    def _on_field_change(self, key_path):
        self._validate_field(key_path)
        self._notify_valid(self.validate_all())


class AppPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.fields = {}
        self._build()

    def _add_row(self, row, label, key_path, browse_file=False, is_int=False, is_file=False):
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", padx=6, pady=4)
        var = tk.StringVar()
        entry = ttk.Entry(self, textvariable=var, width=70)
        entry.grid(row=row, column=1, sticky="we", padx=6, pady=4)
        self.fields[tuple(key_path)] = {"var": var, "entry": entry, "is_int": is_int, "is_file": is_file}
        if browse_file or is_file:
            btns = ttk.Frame(self)
            btns.grid(row=row, column=2, sticky="w", padx=6, pady=4)
            if browse_file:
                def browse():
                    path = filedialog.askopenfilename()
                    if path:
                        var.set(path)
                ttk.Button(btns, text="Browse", command=browse).grid(row=0, column=0, padx=2)
            if is_file:
                self._add_token_button(btns, entry).grid(row=0, column=1, padx=2)
        err = tk.Label(self, text="", fg="#E05A5A", anchor="w")
        err.grid(row=row + 1, column=1, columnspan=2, sticky="w", padx=6, pady=(0, 4))
        self.fields[tuple(key_path)]["error"] = err
        var.trace_add("write", lambda *_args, k=tuple(key_path): self._on_field_change(k))

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="App Branding & Window", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", padx=6, pady=(6, 10)
        )
        fields = [
            ("Title", ["app", "title"], False, False, False),
            ("Background", ["app", "background"], True, False, True),
            ("Logo", ["app", "logo"], True, False, True),
            ("Logo Right", ["app", "logo_right"], True, False, True),
            ("Favicon ICO", ["app", "favicon_ico"], True, False, True),
            ("Favicon PNG", ["app", "favicon_png"], True, False, True),
            ("Center Offset Y", ["app", "center_offset_y"], False, True, False),
            ("Window Width", ["app", "window", "width"], False, True, False),
            ("Window Height", ["app", "window", "height"], False, True, False),
            ("Min Width", ["app", "window", "min_width"], False, True, False),
            ("Min Height", ["app", "window", "min_height"], False, True, False),
        ]
        row = 1
        for label, key_path, browse_file, is_int, is_file in fields:
            self._add_row(row, label, key_path, browse_file=browse_file, is_int=is_int, is_file=is_file)
            row += 2

    def load_from_cfg(self):
        for key_path, info in self.fields.items():
            info["var"].set(str(_get_nested(self.cfg_ref, list(key_path), "") or ""))
        self.validate_all()

    def save_to_cfg(self) -> bool:
        if not self.validate_all():
            return False
        for key_path, info in self.fields.items():
            val = info["var"].get().strip()
            if info["is_int"] and val != "":
                val = int(val)
            _set_nested(self.cfg_ref, list(key_path), val)
        return True

    def _validate_field(self, key_path):
        info = self.fields[key_path]
        val = info["var"].get().strip()
        err = ""
        if info["is_int"] and val != "":
            try:
                int(val)
            except ValueError:
                err = "Must be an integer."
        if info["is_file"] and val and not _looks_like_token(val):
            path = Path(val)
            if not path.exists():
                err = "File not found."
            elif not path.is_file():
                err = "Not a file."
        info["error"].configure(text=err)

    def validate_all(self) -> bool:
        valid = True
        for key_path in self.fields:
            self._validate_field(key_path)
            if self.fields[key_path]["error"].cget("text"):
                valid = False
        return valid

    def _on_field_change(self, key_path):
        self._validate_field(key_path)
        self._notify_valid(self.validate_all())


class DailyNotePage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.fields = {}
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="Daily Note Settings", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", padx=6, pady=(6, 10)
        )
        fields = [
            ("File Pattern", ["daily_note", "file_pattern"]),
            ("Extension", ["daily_note", "extension"]),
            ("Template File", ["daily_note", "template_file_rel"]),
            ("Apply Template When", ["daily_note", "apply_template_when"]),
        ]
        row = 1
        for label, key_path in fields:
            ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", padx=6, pady=4)
            var = tk.StringVar()
            entry = ttk.Entry(self, textvariable=var, width=70)
            entry.grid(row=row, column=1, sticky="we", padx=6, pady=4)
            self.fields[tuple(key_path)] = {"var": var, "entry": entry}
            if key_path[-1] == "template_file_rel":
                def browse():
                    base = _get_nested(self.cfg_ref, ["paths", "SCOUT_ROOT"], "")
                    path = filedialog.askopenfilename(initialdir=base or None)
                    if path:
                        try:
                            rel = str(Path(path).resolve().relative_to(Path(base).resolve()))
                            var.set(rel)
                        except Exception:
                            var.set(path)
                btns = ttk.Frame(self)
                btns.grid(row=row, column=2, sticky="w", padx=6, pady=4)
                ttk.Button(btns, text="Browse", command=browse).grid(row=0, column=0, padx=2)
                self._add_token_button(btns, entry).grid(row=0, column=1, padx=2)
            err = tk.Label(self, text="", fg="#E05A5A", anchor="w")
            err.grid(row=row + 1, column=1, columnspan=2, sticky="w", padx=6, pady=(0, 4))
            self.fields[tuple(key_path)]["error"] = err
            var.trace_add("write", lambda *_args, k=tuple(key_path): self._on_field_change(k))
            row += 2

        self.create_if_missing = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            self,
            text="Create daily note if missing",
            variable=self.create_if_missing
        ).grid(row=row, column=0, columnspan=2, sticky="w", padx=6, pady=4)

    def load_from_cfg(self):
        for key_path, info in self.fields.items():
            info["var"].set(_get_nested(self.cfg_ref, list(key_path), "") or "")
        self.create_if_missing.set(bool(_get_nested(self.cfg_ref, ["daily_note", "create_if_missing"], True)))
        self.validate_all()

    def save_to_cfg(self) -> bool:
        if not self.validate_all():
            return False
        for key_path, info in self.fields.items():
            _set_nested(self.cfg_ref, list(key_path), info["var"].get().strip())
        _set_nested(self.cfg_ref, ["daily_note", "create_if_missing"], bool(self.create_if_missing.get()))
        return True

    def _validate_field(self, key_path):
        info = self.fields[key_path]
        val = info["var"].get().strip()
        err = ""
        if key_path[-1] == "template_file_rel" and val:
            if not _looks_like_token(val):
                base = _get_nested(self.cfg_ref, ["paths", "SCOUT_ROOT"], "")
                candidate = Path(val)
                if not candidate.is_absolute() and base:
                    candidate = Path(base) / candidate
                if not candidate.exists():
                    err = "Template file not found."
                elif not candidate.is_file():
                    err = "Template is not a file."
        info["error"].configure(text=err)

    def validate_all(self) -> bool:
        valid = True
        for key_path in self.fields:
            self._validate_field(key_path)
            if self.fields[key_path]["error"].cget("text"):
                valid = False
        return valid

    def _on_field_change(self, key_path):
        self._validate_field(key_path)
        self._notify_valid(self.validate_all())


class LlmPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.provider = tk.StringVar()
        self.api_key = tk.StringVar()
        self.model = tk.StringVar()
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="LLM Settings", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=6, pady=(6, 10)
        )
        ttk.Label(self, text="Provider").grid(row=1, column=0, sticky="w", padx=6, pady=4)
        ttk.Combobox(
            self,
            textvariable=self.provider,
            values=["openai", "azure", "anthropic", "local", "other"],
            width=30
        ).grid(row=1, column=1, sticky="w", padx=6, pady=4)

        ttk.Label(self, text="API Key").grid(row=2, column=0, sticky="w", padx=6, pady=4)
        ttk.Entry(self, textvariable=self.api_key, show="*", width=50).grid(
            row=2, column=1, sticky="we", padx=6, pady=4
        )

        ttk.Label(self, text="Model").grid(row=3, column=0, sticky="w", padx=6, pady=4)
        ttk.Entry(self, textvariable=self.model, width=50).grid(
            row=3, column=1, sticky="we", padx=6, pady=4
        )

    def load_from_cfg(self):
        self.provider.set(_get_nested(self.cfg_ref, ["llm", "provider"], "") or "")
        self.api_key.set(_get_nested(self.cfg_ref, ["llm", "api_key"], "") or "")
        self.model.set(_get_nested(self.cfg_ref, ["llm", "model"], "") or "")

    def save_to_cfg(self) -> bool:
        _set_nested(self.cfg_ref, ["llm", "provider"], self.provider.get().strip())
        _set_nested(self.cfg_ref, ["llm", "api_key"], self.api_key.get().strip())
        _set_nested(self.cfg_ref, ["llm", "model"], self.model.get().strip())
        return True


class AnalystPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.vars = {}
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="Analyst Profile", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=6, pady=(6, 10)
        )
        fields = [
            ("Name", ["analyst_profile", "name"]),
            ("Email", ["analyst_profile", "email"]),
            ("Phone", ["analyst_profile", "phone"]),
            ("Title", ["analyst_profile", "title"]),
        ]
        row = 1
        for label, key_path in fields:
            ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", padx=6, pady=4)
            var = tk.StringVar()
            ttk.Entry(self, textvariable=var, width=50).grid(row=row, column=1, sticky="we", padx=6, pady=4)
            self.vars[tuple(key_path)] = var
            row += 1

    def load_from_cfg(self):
        for key_path, var in self.vars.items():
            var.set(_get_nested(self.cfg_ref, list(key_path), "") or "")

    def save_to_cfg(self) -> bool:
        for key_path, var in self.vars.items():
            _set_nested(self.cfg_ref, list(key_path), var.get().strip())
        return True


class UiPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.scale = tk.DoubleVar(value=0.8)
        self.title_text = tk.StringVar()
        self.subtitle_text = tk.StringVar()
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text="UI Preferences", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=6, pady=(6, 10)
        )
        ttk.Label(self, text="UI Scale").grid(row=1, column=0, sticky="w", padx=6, pady=4)
        ttk.Scale(self, from_=0.6, to=1.4, variable=self.scale, orient="horizontal").grid(
            row=1, column=1, sticky="we", padx=6, pady=4
        )
        ttk.Label(self, text="Title Text").grid(row=2, column=0, sticky="w", padx=6, pady=4)
        ttk.Entry(self, textvariable=self.title_text, width=50).grid(
            row=2, column=1, sticky="we", padx=6, pady=4
        )
        ttk.Label(self, text="Subtitle Text").grid(row=3, column=0, sticky="w", padx=6, pady=4)
        ttk.Entry(self, textvariable=self.subtitle_text, width=50).grid(
            row=3, column=1, sticky="we", padx=6, pady=4
        )

    def load_from_cfg(self):
        self.scale.set(float(_get_nested(self.cfg_ref, ["ui", "scale"], 0.8) or 0.8))
        self.title_text.set(_get_nested(self.cfg_ref, ["ui", "title", "text"], "") or "")
        self.subtitle_text.set(_get_nested(self.cfg_ref, ["ui", "subtitle", "text"], "") or "")

    def save_to_cfg(self) -> bool:
        _set_nested(self.cfg_ref, ["ui", "scale"], float(self.scale.get()))
        _set_nested(self.cfg_ref, ["ui", "title", "text"], self.title_text.get().strip())
        _set_nested(self.cfg_ref, ["ui", "subtitle", "text"], self.subtitle_text.get().strip())
        return True


class MenuPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.section_list = None
        self.button_list = None
        self.fields = {}
        self._current_section_index = None
        self._current_button_index = None
        self._build()

    def _build(self):
        self.columnconfigure(2, weight=1)
        ttk.Label(self, text="Menu Builder", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", padx=6, pady=(6, 10)
        )

        ttk.Label(self, text="Sections").grid(row=1, column=0, sticky="w", padx=6)
        self.section_list = tk.Listbox(self, height=12)
        self.section_list.grid(row=2, column=0, sticky="nsw", padx=6, pady=4)
        self.section_list.bind("<<ListboxSelect>>", self._on_section_select)

        sec_btns = ttk.Frame(self)
        sec_btns.grid(row=3, column=0, sticky="w", padx=6, pady=4)
        ttk.Button(sec_btns, text="Add Section", command=self._add_section).grid(row=0, column=0, padx=2)
        ttk.Button(sec_btns, text="Rename", command=self._rename_section).grid(row=0, column=1, padx=2)
        ttk.Button(sec_btns, text="Remove", command=self._remove_section).grid(row=0, column=2, padx=2)

        ttk.Label(self, text="Buttons").grid(row=1, column=1, sticky="w", padx=6)
        self.button_list = tk.Listbox(self, height=12, width=35)
        self.button_list.grid(row=2, column=1, sticky="nsw", padx=6, pady=4)
        self.button_list.bind("<<ListboxSelect>>", self._on_button_select)

        btn_btns = ttk.Frame(self)
        btn_btns.grid(row=3, column=1, sticky="w", padx=6, pady=4)
        ttk.Button(btn_btns, text="Add Button", command=self._add_button).grid(row=0, column=0, padx=2)
        ttk.Button(btn_btns, text="Remove", command=self._remove_button).grid(row=0, column=1, padx=2)
        ttk.Button(btn_btns, text="Move Up", command=lambda: self._move_button(-1)).grid(row=0, column=2, padx=2)
        ttk.Button(btn_btns, text="Move Down", command=lambda: self._move_button(1)).grid(row=0, column=3, padx=2)

        editor = ttk.Frame(self)
        editor.grid(row=2, column=2, sticky="nsew", padx=10, pady=4)
        editor.columnconfigure(1, weight=1)

        row = 0
        for label, field in [
            ("Label", "label"),
            ("Description", "description"),
            ("Action", "action"),
            ("Target", "target"),
            ("Icon", "icon"),
            ("Variant", "variant"),
            ("Tag", "tag"),
        ]:
            ttk.Label(editor, text=label).grid(row=row, column=0, sticky="w", pady=3)
            var = tk.StringVar()
            ttk.Entry(editor, textvariable=var, width=50).grid(row=row, column=1, sticky="we", pady=3)
            self.fields[field] = var
            if field in ("target", "icon"):
                def make_browse(field_name):
                    def browse():
                        path = filedialog.askopenfilename()
                        if path:
                            self.fields[field_name].set(path)
                    return browse
                ttk.Button(editor, text="Browse", command=make_browse(field)).grid(row=row, column=2, padx=4)
            row += 1

        ttk.Button(editor, text="Apply Changes", command=self._apply_current_button).grid(
            row=row, column=0, columnspan=2, sticky="w", pady=(8, 2)
        )

    def _menu(self):
        menu = self.cfg_ref.get("menu")
        if not isinstance(menu, list):
            menu = []
            self.cfg_ref["menu"] = menu
        return menu

    def _refresh_sections(self):
        self.section_list.delete(0, "end")
        for sec in self._menu():
            self.section_list.insert("end", sec.get("section", "Untitled"))

    def _refresh_buttons(self):
        self.button_list.delete(0, "end")
        sec = self._current_section()
        if not sec:
            return
        for btn in sec.get("buttons", []):
            self.button_list.insert("end", btn.get("label", "Untitled"))

    def _current_section(self):
        menu = self._menu()
        if self._current_section_index is None:
            return None
        if 0 <= self._current_section_index < len(menu):
            return menu[self._current_section_index]
        return None

    def _current_button(self):
        sec = self._current_section()
        if not sec:
            return None
        buttons = sec.get("buttons", [])
        if self._current_button_index is None:
            return None
        if 0 <= self._current_button_index < len(buttons):
            return buttons[self._current_button_index]
        return None

    def _on_section_select(self, _event=None):
        sel = self.section_list.curselection()
        if not sel:
            return
        self._current_section_index = sel[0]
        self._current_button_index = None
        self._refresh_buttons()
        self._load_button_fields(None)

    def _on_button_select(self, _event=None):
        sel = self.button_list.curselection()
        if not sel:
            return
        self._current_button_index = sel[0]
        self._load_button_fields(self._current_button())

    def _load_button_fields(self, btn):
        for field, var in self.fields.items():
            var.set((btn or {}).get(field, "") or "")

    def _apply_current_button(self):
        btn = self._current_button()
        if not btn:
            return
        for field, var in self.fields.items():
            btn[field] = var.get().strip()
        self._refresh_buttons()

    def _add_section(self):
        name = simpledialog.askstring("Section name", "Enter section name:")
        if not name:
            return
        self._menu().append({"section": name, "buttons": []})
        self._refresh_sections()

    def _rename_section(self):
        sec = self._current_section()
        if not sec:
            return
        name = simpledialog.askstring("Rename section", "Enter new section name:", initialvalue=sec.get("section", ""))
        if not name:
            return
        sec["section"] = name
        self._refresh_sections()

    def _remove_section(self):
        menu = self._menu()
        sec = self._current_section()
        if not sec:
            return
        if not messagebox.askyesno("Remove section", "Remove selected section and all its buttons?"):
            return
        menu.remove(sec)
        self._current_section_index = None
        self._current_button_index = None
        self._refresh_sections()
        self._refresh_buttons()
        self._load_button_fields(None)

    def _add_button(self):
        sec = self._current_section()
        if not sec:
            messagebox.showinfo("Select section", "Select a section first.")
            return
        sec.setdefault("buttons", []).append(
            {"label": "New Button", "description": "", "action": "", "target": "", "icon": "", "variant": "", "tag": ""}
        )
        self._refresh_buttons()

    def _remove_button(self):
        sec = self._current_section()
        btn = self._current_button()
        if not sec or not btn:
            return
        sec["buttons"].remove(btn)
        self._current_button_index = None
        self._refresh_buttons()
        self._load_button_fields(None)

    def _move_button(self, delta):
        sec = self._current_section()
        if not sec:
            return
        buttons = sec.get("buttons", [])
        idx = self._current_button_index
        if idx is None:
            return
        new_idx = idx + delta
        if new_idx < 0 or new_idx >= len(buttons):
            return
        buttons[idx], buttons[new_idx] = buttons[new_idx], buttons[idx]
        self._current_button_index = new_idx
        self._refresh_buttons()
        self.button_list.selection_set(new_idx)

    def load_from_cfg(self):
        self._refresh_sections()
        self._refresh_buttons()
        self._load_button_fields(None)

    def save_to_cfg(self) -> bool:
        self._apply_current_button()
        return True


class JsonPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.text = tk.Text(self, wrap="none", height=20)
        self._build()

    def _build(self):
        ttk.Label(self, text="Advanced JSON", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, sticky="w", padx=6, pady=(6, 10)
        )
        self.text.grid(row=1, column=0, sticky="nsew", padx=6, pady=4)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        btns = ttk.Frame(self)
        btns.grid(row=2, column=0, sticky="w", padx=6, pady=6)
        ttk.Button(btns, text="Apply JSON", command=self._apply_json).grid(row=0, column=0, padx=4)
        ttk.Button(btns, text="Reload from disk", command=self._reload).grid(row=0, column=1, padx=4)

    def _apply_json(self):
        raw = self.text.get("1.0", "end").strip()
        if not raw:
            return
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            messagebox.showerror("Invalid JSON", str(exc))
            return
        self.cfg_ref.clear()
        self.cfg_ref.update(data)
        messagebox.showinfo("Applied", "JSON changes applied to in-memory config.")

    def _reload(self):
        path = get_app_dir() / "config.json"
        if not path.exists():
            messagebox.showerror("Not found", f"Missing config.json at {path}")
            return
        self.cfg_ref.clear()
        self.cfg_ref.update(_read_config_file(path))
        self.load_from_cfg()

    def load_from_cfg(self):
        self.text.delete("1.0", "end")
        self.text.insert("1.0", json.dumps(self.cfg_ref, indent=2))

    def save_to_cfg(self) -> bool:
        return True


class SummaryPage(WizardPage):
    def __init__(self, master, cfg_ref: dict):
        super().__init__(master, cfg_ref)
        self.summary = tk.Text(self, height=18, wrap="word", state="disabled")
        self._build()

    def _build(self):
        ttk.Label(self, text="Summary & Validation", font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, sticky="w", padx=6, pady=(6, 10)
        )
        self.summary.grid(row=1, column=0, sticky="nsew", padx=6, pady=4)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    def load_from_cfg(self):
        issues = []
        scout_root = _get_nested(self.cfg_ref, ["paths", "SCOUT_ROOT"], "")
        obsidian_exe = _get_nested(self.cfg_ref, ["paths", "OBSIDIAN_EXE"], "")
        vault_root = _get_nested(self.cfg_ref, ["paths", "VAULT_ROOT"], "")
        if scout_root and not Path(scout_root).exists():
            issues.append(f"SCOUT_ROOT not found: {scout_root}")
        if vault_root and not Path(vault_root).exists():
            issues.append(f"VAULT_ROOT not found: {vault_root}")
        if obsidian_exe and not Path(obsidian_exe).exists():
            issues.append(f"OBSIDIAN_EXE not found: {obsidian_exe}")

        lines = ["Configuration ready for save.", ""]
        if issues:
            lines.append("Warnings:")
            lines.extend([f" - {i}" for i in issues])
        else:
            lines.append("No validation warnings.")

        self.summary.configure(state="normal")
        self.summary.delete("1.0", "end")
        self.summary.insert("1.0", "\n".join(lines))
        self.summary.configure(state="disabled")


class ConfigWizard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SCOUT Setup Wizard")
        self.geometry("1100x760")
        self.minsize(1000, 680)
        self.cfg_path = get_app_dir() / "config.json"
        if not self.cfg_path.exists():
            messagebox.showerror("Missing config.json", f"Could not find config.json at {self.cfg_path}")
            self.destroy()
            return
        self.cfg = _read_config_file(self.cfg_path)

        self._page_valid = True
        self._build_ui()
        self._show_page(0)

    def _build_ui(self):
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True, padx=8, pady=8)

        self.pages = [
            PathsPage(self.container, self.cfg),
            AppPage(self.container, self.cfg),
            DailyNotePage(self.container, self.cfg),
            LlmPage(self.container, self.cfg),
            AnalystPage(self.container, self.cfg),
            UiPage(self.container, self.cfg),
            MenuPage(self.container, self.cfg),
            JsonPage(self.container, self.cfg),
            SummaryPage(self.container, self.cfg),
        ]
        for page in self.pages:
            page.set_validation_callback(self._set_page_valid)
            page.grid(row=0, column=0, sticky="nsew")

        nav = ttk.Frame(self)
        nav.pack(fill="x", padx=8, pady=(0, 8))
        self.back_btn = ttk.Button(nav, text="Back", command=self._back)
        self.next_btn = ttk.Button(nav, text="Next", command=self._next)
        self.save_btn = ttk.Button(nav, text="Save", command=self._save)
        self.back_btn.pack(side="left")
        self.next_btn.pack(side="left", padx=6)
        self.save_btn.pack(side="right")

    def _show_page(self, index):
        if index < 0 or index >= len(self.pages):
            return
        self.page_index = index
        page = self.pages[index]
        page.load_from_cfg()
        page.tkraise()
        self._page_valid = page.validate_all()
        self._update_nav()

    def _current_page(self):
        return self.pages[self.page_index]

    def _back(self):
        if not self._current_page().save_to_cfg():
            return
        self._show_page(self.page_index - 1)

    def _next(self):
        if not self._current_page().save_to_cfg():
            return
        self._show_page(self.page_index + 1)

    def _save(self):
        if not self._current_page().save_to_cfg():
            return
        try:
            _write_config_file_with_backup(self.cfg_path, self.cfg)
            messagebox.showinfo("Saved", f"Saved config.json (backup created).")
        except Exception as exc:
            messagebox.showerror("Save failed", str(exc))

    def _set_page_valid(self, valid: bool):
        self._page_valid = bool(valid)
        self._update_nav()

    def _update_nav(self):
        self.back_btn["state"] = "normal" if self.page_index > 0 else "disabled"
        if self.page_index < len(self.pages) - 1 and self._page_valid:
            self.next_btn["state"] = "normal"
        else:
            self.next_btn["state"] = "disabled"
        self.save_btn["state"] = "normal" if self._page_valid else "disabled"


if __name__ == "__main__":
    app = ConfigWizard()
    app.mainloop()
