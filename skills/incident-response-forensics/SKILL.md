---
name: incident-response-forensics
description: 'Contain a live security incident without destroying evidence: timeline, affected identities and assets, initial access, persistence, data and financial impact, credential revocation and rotation, workload isolation, restore from known-good state, then IOCs, root cause, and corrective controls. Never retaliate or hack back. Use for "we have been breached", suspicious activity, compromised keys, or a post-incident review.'
---
# Incident Response and Forensics

## Mission
Contain incidents, preserve evidence, recover safely and learn from root causes.

## Workflow
Prioritize safety and containment without destroying evidence. Establish timeline, affected identities/assets, initial access, persistence, data/financial impact and current attacker access. Preserve relevant logs and snapshots with timestamps and access control. Revoke/rotate compromised credentials, isolate affected workloads and restore from known-good state. Coordinate provider/payment actions when money is involved. Produce IOCs, root cause, corrective actions and regression controls. Never retaliate or hack back.

## Operating contract
- Defensive and authorized use only. Do not provide or execute instructions for theft, credential capture, persistence, evasion, destructive attacks, malware deployment, or unauthorized access.
- Never claim a vulnerability is exploitable without evidence. Distinguish confirmed, likely, informational and unknown.
- Never expose secrets, personal data or full payment credentials in output. Redact by default.
- Do not weaken security controls merely to unblock a build.
- Prefer least privilege, deny-by-default, defense in depth and auditable deterministic controls for high-impact actions.
- Production-changing actions require explicit authorization and a rollback path.

## Required output
Return: scope; assets/trust boundaries; findings with severity and evidence; remediation; tests/retest status; residual risk; release recommendation. Use Critical/High/Medium/Low/Info.

## References to apply
Use OWASP API Security guidance for API authorization, authentication, resource consumption, sensitive business flows, SSRF, configuration and third-party API consumption. Use NIST SSDF principles across prepare/protect/produce/respond. For agentic systems, threat-model prompt injection, tool abuse, excessive agency, poisoned context/memory and data exfiltration.

