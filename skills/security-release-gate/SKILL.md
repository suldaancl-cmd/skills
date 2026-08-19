---
name: security-release-gate
description: 'Make an evidence-based ship or no-ship decision: requires passing tests, reviewed migrations, secret scan, dependency and container scan, authorization/RLS tests, API abuse tests, and applicable payment and agent checks. Outputs PASS, CONDITIONAL PASS, or BLOCK with evidence and exact remediation and retest criteria. Use before a production deploy or an App Store submission.'
---
# Security Release Gate

## Mission
Make an evidence-based production release decision.

## Workflow
Require passing tests, reviewed migrations, secret scan, dependency/container scan, authorization/RLS tests, API abuse tests and applicable payment/agent checks. Block on confirmed critical issues, exposed production secrets, missing tenant isolation, unsafe payment authorization or unrestricted privileged agent tools. High findings require explicit documented risk acceptance by an authorized owner. Output PASS, CONDITIONAL PASS or BLOCK with evidence and exact remediation/retest criteria.

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

