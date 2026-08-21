# Credential boundary matrix

| Credential | Expo/web client | Secure device storage | Trusted API | Worker | CI/store vault | Logs |
|---|---|---|---|---|---|---|
| Public API URL | allowed | unnecessary | allowed | allowed | allowed | allowed |
| Publishable client key | allowed | usually unnecessary | allowed | optional | allowed | fingerprint only |
| User access/refresh token | runtime only | supported secure session storage | verify only | avoid unless delegated | no | never |
| AI provider secret | never | never | allowed | allowed | allowed | never |
| Database secret/service role | never | never | narrowly allowed | narrowly allowed | allowed | never |
| Webhook signing secret | never | never | allowed at receiver | allowed if receiver | allowed | never |
| Store/service-account key | never | never | rarely | never | allowed | never |
| App signing key/certificate | never | never | never | never | allowed | never |

## Review questions

- Can a client choose an arbitrary upstream URL, model, tool, or spend level?
- Is authorization based on verified identity and resource ownership?
- Can duplicate requests or webhooks repeat a charge or side effect?
- Are signed URLs short-lived and scoped?
- Do errors, analytics, or crash reports capture credentials or private prompts?
- Is rotation documented and tested without copying secret values into tickets or chat?
