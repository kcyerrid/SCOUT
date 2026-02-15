---
entity_type: mitre_technique
technique_id: "T1613"
subtechnique_id: ""
technique_name: "Container and Resource Discovery"
tactic:
  - "TA0007 - Discovery"
platforms:
  - "Containers"
datasources:
  - "Pod Enumeration (DC0037)"
  - "Container Enumeration (DC0091)"
mitre_version: "17.0"
attack_spec_version: "3.2"
attack_source: Enterprise
deprecated: false
revoked: false
associated_threat_actors:
  - "[[30_CIPHER/03_Threat_Actors/G0139 - TeamTNT|TeamTNT]]"
associated_malware:
  - "[[30_CIPHER/05_Malware/S0601 - Hildegard|Hildegard]]"
  - "[[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]]"
associated_campaigns: []
related_techniques: []
detection_priority:
  - High
detection_maturity: ""
threat_score: 4
created: 2026-01-06
updated: 2026-01-06
contributors: []
tags:
  - mitre
  - technique
banner: 99_Attachments/SCOUT_Obsidian_Banner.png
banner-display: contain
banner-repeat: false
banner-height: 100
content-start: 101
---

## 1. Summary
Adversaries enumerate container resources (containers, images, pods, nodes, deployments, cluster state) to understand what exists, where to move next, and which execution/lateral movement options are available in a containerized environment.

## 2. Technical Overview
Container environments expose multiple discovery surfaces:
- **Orchestrator APIs** (e.g., Kubernetes API server) for listing pods, nodes, deployments, namespaces, RBAC objects, and cluster metadata.
- **Container runtime/daemon interfaces** (e.g., Docker daemon) for listing running containers, images, and inspecting container configs.
- **Dashboards and management planes** (e.g., Kubernetes Dashboard) that can be abused if credentials or access paths exist.

Discovery outcomes commonly enable:
- Target selection (privileged pods, nodes, sensitive namespaces)
- Credential hunting (service account tokens, mounted secrets)
- Movement decisions (exec into pods, schedule workloads, access metadata endpoints)

## 3. Subtechnique Considerations
No sub-techniques.

## 4. Procedure Examples
Observed in ATT&CK procedure examples:
- [[30_CIPHER/05_Malware/S0601 - Hildegard|Hildegard]] used scanning to find kubelets and queried the kubelet API for additional running containers.
- [[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]] enumerates Kubernetes pods in a namespace.
- [[30_CIPHER/03_Threat_Actors/G0139 - TeamTNT|TeamTNT]] checked for running containers and inspected specific container names; also searched for Kubernetes pods on the local network.

## 5. Detection Guidance
Detection focus: identify unexpected resource listing/inspection relative to the identity and workload context.
- Monitor Kubernetes API list/get calls for pods/nodes/deployments across namespaces, especially from non-admin service accounts.
- Detect spikes in enumeration verbs (list/watch/get) and broad queries (cluster-wide listing, repeated namespace traversal).
- In Docker, monitor daemon activity for frequent `ps`, `inspect`, and image listings from unusual users/process trees or remote sources.
- Correlate with suspicious follow-on actions: exec into pods, secret access, token creation, workload deployment changes, or lateral movement attempts.

High-signal patterns:
- Enumeration by identities that rarely interact with the API (new service account, compromised app identity).
- Cluster-wide discovery from a single source, quickly followed by access to secrets/config maps.
- Docker socket usage by processes not expected to manage containers (application processes, web shells).

### Data Source Notes
Required/strongly recommended telemetry:
- **Pod Enumeration (DC0037)**: Kubernetes API server audit logs capturing list/get requests against pods/deployments/nodes.
- **Container Enumeration (DC0091)**: container runtime/daemon logs capturing container listing/inspection activity (e.g., Docker daemon logs).

Operational notes:
- Enable Kubernetes audit logging with request/response metadata and user impersonation fields where possible.
- Retain identity attributes (user/serviceAccount, groups, RBAC decision context) for effective allowlisting.

## 6. Response Guidance
1. **Identify the enumerating principal**: service account/user, token source, workload/pod identity, and API client/user agent.
2. **Determine scope**: namespaces and resource types enumerated; whether secrets/config maps were accessed afterward.
3. **Containment**: revoke compromised tokens, rotate service account secrets, and restrict RBAC permissions (least privilege).
4. **Hunt follow-on behaviors**: exec/attach to pods, deployment modifications, new workloads, node-level access, metadata endpoint access.
5. **Hardening**: restrict Docker socket exposure; limit dashboard access; enforce namespace isolation; consider JIT access and stronger auth.

## 7. Related ATT&CK Content
- [[20_Entities/07_TTPs/TA0007 - Discovery/T1613 - Container and Resource Discovery|T1613]]

## 8. SOC Relevance
High relevance in container/Kubernetes-heavy organizations: discovery is often the first observable step after initial access, and it strongly predicts escalation attempts (secrets, exec, workload manipulation).

## 9. Threat Actor Usage
- [[30_CIPHER/03_Threat_Actors/G0139 - TeamTNT|TeamTNT]]

## 10. Campaign Usage
No ATT&CK procedure examples list a specific campaign for this technique.

## 11. Malware Usage
- [[30_CIPHER/05_Malware/S0601 - Hildegard|Hildegard]]
- [[30_CIPHER/05_Malware/S0683 - Peirates|Peirates]]

## 12. Mitigations
- **Limit Access to Resource Over Network (M1035)**: restrict API access to secured channels; disable unauthenticated Docker/Kubernetes API access; use TLS and network controls for API server exposure.
- **Network Segmentation (M1030)**: prevent direct remote access to internal container control planes via firewalls/gateways.
- **User Account Management (M1018)**: enforce least privilege in RBAC; avoid wildcard permissions; prefer scoped RoleBindings over ClusterRoleBindings where possible.

## 13. Testing & Validation
Safe validation ideas (lab cluster):
- Execute benign listing operations (e.g., list pods/nodes) using a low-privilege test service account; confirm audit logs capture the activity.
- Simulate “namespace traversal” enumeration from a single identity and verify alerts on volume/breadth.
- Run Docker `ps`/`inspect` from an unexpected container/process context and validate daemon logging and detections.

## 14. References
- MITRE ATT&CK. (n.d.). *Container and Resource Discovery (T1613)*. https://attack.mitre.org/techniques/T1613/
- Kubernetes. (n.d.). *The Kubernetes API*. https://kubernetes.io/docs/concepts/overview/kubernetes-api/
- Docker. (n.d.). *Docker Engine API reference*. https://docs.docker.com/engine/api/
- Palo Alto Networks Unit 42. (2021, February 3). *Hildegard: New TeamTNT cryptojacking malware targeting Kubernetes*. https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/
- Trend Micro. (n.d.). *Tracking the activities of TeamTNT*. https://documents.trendmicro.com/

## 15. Notes
- If you can only log one thing: Kubernetes API server audits (list/get/watch) with identity context and source IP.
