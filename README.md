<div align="center">

<h1>authorization-policy-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/authorization-policy-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/authorization-policy-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/authorization-policy-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/authorization-policy-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/authorization-policy-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/authorization-policy-governance-pack.svg"></a>
  <a href="https://pypi.org/project/authorization-policy-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/authorization-policy-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/authorization-policy-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p><a href="https://github.com/groupsum/authorization-policy-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fauthorization--policy--governance--pack-181717?logo=github"></a></p>

</div>

`authorization-policy-governance-pack` is an SSOT Registry pack for authorization policy, OAuth scopes, access-token validation, permissions, entitlements, RBAC, ABAC, PBAC, ReBAC, PDP/PEP/PIP/PAP architecture, policy gateways, Cedar, OPA/Rego, XACML vocabulary, and authorization evidence.

It governs how a repository answers: can this subject perform this action on this resource in this context? Authentication facts and token claims can feed that answer, but they are not the answer by themselves.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed Architecture Decision Records (ADRs) and Specifications (SPECs) for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents that downstream repositories can synchronize into their local `.ssot` registry and link to features, tests, claims, evidence, and releases.

## Why This Pack Exists

Authorization governance fails when scopes, claims, roles, groups, entitlements, relationships, and policy decisions are treated as interchangeable. This pack separates delegated grants from runtime permissions and makes PDP/PEP boundaries, policy inputs, deny paths, and release evidence explicit.

This pack helps teams:

- distinguish scopes, claims, permissions, roles, entitlements, and policy decisions
- govern RBAC, ABAC, PBAC, ReBAC, XACML, Cedar, OPA/Rego, OpenFGA, and custom policy engines
- declare PDP, PEP, PIP, PAP, and policy gateway responsibilities
- test least privilege, deny paths, stale attributes, revoked entitlements, and tenant isolation

## Pack Metadata

- Pack ID: `pack:authorization-policy`
- PyPI package: `authorization-policy-governance-pack`
- Import package: `authorization_policy_governance_pack`
- GitHub repository: [groupsum/authorization-policy-governance-pack](https://github.com/groupsum/authorization-policy-governance-pack)
- Reservation owner: `extension-pack:authorization-policy-governance-pack`

## Domain Focus

- OAuth scopes, consent, grants, and access-token validation
- permission taxonomy and runtime permission checks
- roles, groups, and entitlements as authorization inputs
- RBAC, ABAC, PBAC, ReBAC, ACL, and capability-style modeling
- PDP, PEP, PIP, PAP, policy gateways, and app-level enforcement
- Cedar, OPA/Rego, XACML vocabulary, OpenFGA, and custom policy engines
- authorization audit, least privilege, deny-path evidence, cache behavior, and failure modes

## Authority Sources

- [OAuth 2.0 Authorization Framework, RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)
- [OAuth 2.0 Token Introspection, RFC 7662](https://www.rfc-editor.org/rfc/rfc7662)
- [OAuth 2.0 Token Exchange, RFC 8693](https://www.rfc-editor.org/rfc/rfc8693)
- [JWT Profile for OAuth 2.0 Access Tokens, RFC 9068](https://www.rfc-editor.org/rfc/rfc9068)
- [OAuth 2.0 Security Best Current Practice, RFC 9700](https://www.rfc-editor.org/rfc/rfc9700)
- [NIST SP 800-162: Guide to Attribute Based Access Control](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [NIST SP 800-207A: Zero Trust Architecture Model for Access Control](https://csrc.nist.gov/pubs/sp/800/207/a/final)
- [OASIS XACML 3.0 Core Specification](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html)
- [NIST RBAC Standards](https://csrc.nist.gov/projects/role-based-access-control/role-engineering-and-rbac-standards)
- [Cedar Policy Language](https://docs.cedarpolicy.com/)
- [Open Policy Agent Rego Policy Language](https://www.openpolicyagent.org/docs/policy-language)
- [Google Zanzibar paper](https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/)
- [OpenFGA authorization modeling](https://openfga.dev/docs/modeling/getting-started)

## Included ADRs And SPECs

This release includes 14 ADR templates and 19 SPEC templates covering authorization boundaries, OAuth scopes, access-token validation, permissions, entitlements, RBAC, ABAC, PBAC, ReBAC, PDP/PEP/PIP/PAP, policy-as-code, Cedar, OPA/Rego, XACML vocabulary, policy gateways, audit evidence, least privilege, token-to-policy mapping, and authorization failure modes.

## Install With uv

```bash
uv add authorization-policy-governance-pack
uv add ssot-registry authorization-policy-governance-pack
uvx --from ssot-registry --with authorization-policy-governance-pack ssot --help
```

## Use With The SSOT Registry CLI

```bash
uv run ssot pack inspect authorization_policy_governance_pack
uv run ssot pack preflight . authorization_policy_governance_pack --all
uv run ssot pack sync . authorization_policy_governance_pack --all --trust --yes
uv run ssot validate .
uv run ssot spec get . --id spc:pack.authorization-policy.authorization-boundary-contract
```

## Programmatic Usage

```python
from authorization_policy_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-authorization-boundary-contract.yaml")
```

## Resources

- GitHub repository: [groupsum/authorization-policy-governance-pack](https://github.com/groupsum/authorization-policy-governance-pack)
- PyPI package: [authorization-policy-governance-pack](https://pypi.org/project/authorization-policy-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
