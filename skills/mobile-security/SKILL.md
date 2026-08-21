---
name: mobile-security
description: 'Secure React Native/Expo, iOS, and Android clients on the assumption the device and app bundle are attacker-controlled: no privileged server secrets in the bundle, platform-secure token storage with minimal lifetime and scope, deep/universal link and auth redirect validation, release signing, update channels, debug flags, and third-party SDK data collection. Backend enforces all financial and authorization rules. Use for mobile app security or a pre-submission security review.'
---
# Mobile Security

## Mission
Secure React Native/Expo, iOS and Android clients.

## Workflow
Assume the client device and application bundle are attacker-controlled. Never embed privileged server/API secrets. Store user tokens with platform-secure mechanisms where appropriate; minimize token lifetime and scope. Validate deep/universal links, auth redirects and backend authorization. Protect sensitive local data, logs and screenshots where warranted. Review release signing, update channels, debug flags and third-party SDK collection. Backend must enforce all financial and authorization rules.

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

