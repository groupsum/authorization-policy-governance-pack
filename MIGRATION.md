# Migration

This historical package has been replaced by narrower governance packages.

| Historical document | Successor document IDs |
|---|---|
| `ADR-1000-authentication-facts-are-policy-inputs-not-authorization-decisions.yaml` | `adr:authentication-and-authorization-are-separate-governance-surfaces`, `adr:policy-inputs-use-principal-action-resource-and-context` |
| `ADR-1001-oauth-scopes-are-delegated-grants-not-complete-policy-decisions.yaml` | `adr:oauth-scopes-are-delegated-grants-not-application-permissions` |
| `ADR-1002-access-token-claims-require-resource-server-validation.yaml` | `adr:resource-servers-own-access-token-validation` |
| `ADR-1003-policy-decisions-use-explicit-pdp-pep-boundaries.yaml` | `adr:policy-decisions-use-explicit-pdp-pep-pip-pap-boundaries` |
| `ADR-1004-policy-inputs-use-subject-resource-action-and-context.yaml` | `adr:policy-inputs-use-principal-action-resource-and-context` |
| `ADR-1005-attribute-sources-are-authoritative-inputs-not-hidden-logic.yaml` | `adr:attribute-sources-are-authoritative-policy-inputs` |
| `ADR-1006-rbac-roles-are-permission-bundles-not-policy-truth.yaml` | `adr:roles-are-permission-bundles-not-policy-truth` |
| `ADR-1007-abac-pbac-policies-own-contextual-authorization.yaml` | `adr:contextual-authorization-is-owned-by-abac-pbac-policy` |
| `ADR-1008-rebac-relationships-own-graph-based-resource-authorization.yaml` | `adr:relationships-own-graph-based-resource-authorization` |
| `ADR-1009-entitlements-are-provisioned-access-facts-not-always-runtime-permissions.yaml` | `adr:entitlements-are-inputs-not-runtime-role-decisions` |
| `ADR-1010-policy-as-code-engines-must-declare-language-and-evaluation-contract.yaml` | `adr:policy-engines-declare-language-version-and-evaluation-contract` |
| `ADR-1011-xacml-is-a-reference-architecture-not-a-required-policy-language.yaml` | `adr:xacml-is-a-reference-architecture-not-a-required-language` |
| `ADR-1012-policy-gateways-are-enforcement-points-not-complete-authorization-systems.yaml` | `adr:policy-gateways-are-enforcement-points` |
| `ADR-1013-deny-paths-and-least-privilege-are-release-gated-evidence.yaml` | `adr:deny-paths-and-least-privilege-are-release-gated` |
| `SPEC-2000-authorization-boundary-contract.yaml` | `spc:authn-authz-boundary-contract`, `spc:authorization-request-and-response-contract` |
| `SPEC-2001-oauth-scope-consent-and-grant-contract.yaml` | `spc:oauth-scope-consent-and-grant-contract` |
| `SPEC-2002-oauth-access-token-validation-contract.yaml` | `spc:jwt-access-token-validation-contract`, `spc:opaque-token-introspection-contract` |
| `SPEC-2003-permission-taxonomy-and-naming-contract.yaml` | `spc:permission-action-and-resource-taxonomy-contract` |
| `SPEC-2004-entitlement-role-and-group-contract.yaml` | `spc:entitlement-role-and-group-normalization-contract`, `spc:entitlement-to-policy-input-contract` |
| `SPEC-2005-pdp-pep-pip-pap-architecture-contract.yaml` | `spc:pdp-pep-pip-pap-architecture-contract` |
| `SPEC-2006-policy-decision-request-response-contract.yaml` | `spc:authorization-request-and-response-contract` |
| `SPEC-2007-abac-pbac-policy-input-contract.yaml` | `spc:subject-resource-action-environment-attribute-contract` |
| `SPEC-2008-rbac-role-permission-contract.yaml` | `spc:rbac-core-role-permission-contract` |
| `SPEC-2009-rebac-relationship-authorization-contract.yaml` | `spc:relationship-schema-and-tuple-contract` |
| `SPEC-2010-policy-as-code-authoring-and-review-contract.yaml` | `spc:policy-authoring-and-review-contract` |
| `SPEC-2011-cedar-policy-language-boundary-contract.yaml` | `spc:cedar-policy-language-profile-contract` |
| `SPEC-2012-opa-rego-policy-language-boundary-contract.yaml` | `spc:opa-rego-policy-language-profile-contract` |
| `SPEC-2013-xacml-compatibility-and-vocabulary-contract.yaml` | `spc:xacml-language-compatibility-contract` |
| `SPEC-2014-policy-gateway-enforcement-contract.yaml` | `spc:policy-gateway-enforcement-contract` |
| `SPEC-2015-authorization-audit-and-evidence-contract.yaml` | `spc:authorization-decision-audit-contract` |
| `SPEC-2016-least-privilege-and-negative-path-test-contract.yaml` | `spc:policy-unit-negative-and-regression-test-contract` |
| `SPEC-2017-token-to-policy-context-mapping-contract.yaml` | `spc:token-to-policy-context-mapping-contract` |
| `SPEC-2018-authorization-failure-mode-and-cache-contract.yaml` | `spc:authorization-failure-cache-and-availability-contract` |

Replacement packages:

- `oauth-delegated-authorization-governance-pack`
- `access-token-validation-governance-pack`
- `rbac-governance-pack`
- `abac-pbac-governance-pack`
- `relationship-authorization-governance-pack`
- `policy-decision-architecture-governance-pack`
- `policy-as-code-governance-pack`
- `oidc-authn-authz-boundary-governance-pack`
