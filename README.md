# authorization-policy-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>authorization-policy-governance-pack</strong></p>
<p align="center">Deprecated historical compatibility package; use the specialist governance packages.</p>
<p align="center">
<a href="https://pypi.org/project/authorization-policy-governance-pack/"><img alt="pypi: authorization-policy-governance-pack unpublished" src="https://img.shields.io/static/v1?label=pypi&amp;message=authorization-policy-governance-pack%20unpublished&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: deprecated" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=deprecated&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/authorization-policy-governance-pack/"><img alt="pypi downloads: authorization-policy-governance-pack: unpublished" src="https://img.shields.io/static/v1?label=pypi%20downloads&amp;message=authorization-policy-governance-pack%3A%20unpublished&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/README.md"><img alt="README hits: authorization-policy-governance-pack" src="https://hits.sh/github.com/groupsum/authorization-policy-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

> Deprecated historical compatibility package. Do not use for new governance work. See the [Migration guide](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md).

Deprecated historical compatibility package; normative ownership moved to specialist governance packages.

### Why This Package

The historical package preserves its manifest and document identifiers for reproducibility.

### When to Use

Use this checkout to reproduce a historical registry state.

### Features

**Included ADRs**

- [`adr:authentication-facts-are-policy-inputs-not-authorization-decisions`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1000-authentication-facts-are-policy-inputs-not-authorization-decisions.yaml) — Authentication Facts Are Policy Inputs Not Authorization Decisions
- [`adr:oauth-scopes-are-delegated-grants-not-complete-policy-decisions`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1001-oauth-scopes-are-delegated-grants-not-complete-policy-decisions.yaml) — OAuth Scopes Are Delegated Grants Not Complete Policy Decisions
- [`adr:access-token-claims-require-resource-server-validation`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1002-access-token-claims-require-resource-server-validation.yaml) — Access Token Claims Require Resource Server Validation
- [`adr:policy-decisions-use-explicit-pdp-pep-boundaries`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1003-policy-decisions-use-explicit-pdp-pep-boundaries.yaml) — Policy Decisions Use Explicit PDP PEP Boundaries
- [`adr:policy-inputs-use-subject-resource-action-and-context`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1004-policy-inputs-use-subject-resource-action-and-context.yaml) — Policy Inputs Use Subject Resource Action And Context
- [`adr:attribute-sources-are-authoritative-inputs-not-hidden-logic`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1005-attribute-sources-are-authoritative-inputs-not-hidden-logic.yaml) — Attribute Sources Are Authoritative Inputs Not Hidden Logic
- [`adr:rbac-roles-are-permission-bundles-not-policy-truth`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1006-rbac-roles-are-permission-bundles-not-policy-truth.yaml) — RBAC Roles Are Permission Bundles Not Policy Truth
- [`adr:abac-pbac-policies-own-contextual-authorization`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1007-abac-pbac-policies-own-contextual-authorization.yaml) — ABAC PBAC Policies Own Contextual Authorization
- [`adr:rebac-relationships-own-graph-based-resource-authorization`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1008-rebac-relationships-own-graph-based-resource-authorization.yaml) — ReBAC Relationships Own Graph Based Resource Authorization
- [`adr:entitlements-are-provisioned-access-facts-not-always-runtime-permissions`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1009-entitlements-are-provisioned-access-facts-not-always-runtime-permissions.yaml) — Entitlements Are Provisioned Access Facts Not Always Runtime Permissions
- [`adr:policy-as-code-engines-must-declare-language-and-evaluation-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1010-policy-as-code-engines-must-declare-language-and-evaluation-contract.yaml) — Policy As Code Engines Must Declare Language And Evaluation Contract
- [`adr:xacml-is-a-reference-architecture-not-a-required-policy-language`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1011-xacml-is-a-reference-architecture-not-a-required-policy-language.yaml) — XACML Is A Reference Architecture Not A Required Policy Language
- [`adr:policy-gateways-are-enforcement-points-not-complete-authorization-systems`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1012-policy-gateways-are-enforcement-points-not-complete-authorization-systems.yaml) — Policy Gateways Are Enforcement Points Not Complete Authorization Systems
- [`adr:deny-paths-and-least-privilege-are-release-gated-evidence`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/adr/ADR-1013-deny-paths-and-least-privilege-are-release-gated-evidence.yaml) — Deny Paths And Least Privilege Are Release Gated Evidence

**Included SPECs**

- [`spc:authorization-boundary-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2000-authorization-boundary-contract.yaml) — Authorization Boundary Contract
- [`spc:oauth-scope-consent-and-grant-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2001-oauth-scope-consent-and-grant-contract.yaml) — OAuth Scope Consent And Grant Contract
- [`spc:oauth-access-token-validation-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2002-oauth-access-token-validation-contract.yaml) — OAuth Access Token Validation Contract
- [`spc:permission-taxonomy-and-naming-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2003-permission-taxonomy-and-naming-contract.yaml) — Permission Taxonomy And Naming Contract
- [`spc:entitlement-role-and-group-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2004-entitlement-role-and-group-contract.yaml) — Entitlement Role And Group Contract
- [`spc:pdp-pep-pip-pap-architecture-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2005-pdp-pep-pip-pap-architecture-contract.yaml) — PDP PEP PIP PAP Architecture Contract
- [`spc:policy-decision-request-response-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2006-policy-decision-request-response-contract.yaml) — Policy Decision Request Response Contract
- [`spc:abac-pbac-policy-input-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2007-abac-pbac-policy-input-contract.yaml) — ABAC PBAC Policy Input Contract
- [`spc:rbac-role-permission-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2008-rbac-role-permission-contract.yaml) — RBAC Role Permission Contract
- [`spc:rebac-relationship-authorization-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2009-rebac-relationship-authorization-contract.yaml) — ReBAC Relationship Authorization Contract
- [`spc:policy-as-code-authoring-and-review-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2010-policy-as-code-authoring-and-review-contract.yaml) — Policy As Code Authoring And Review Contract
- [`spc:cedar-policy-language-boundary-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2011-cedar-policy-language-boundary-contract.yaml) — Cedar Policy Language Boundary Contract
- [`spc:opa-rego-policy-language-boundary-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2012-opa-rego-policy-language-boundary-contract.yaml) — OPA Rego Policy Language Boundary Contract
- [`spc:xacml-compatibility-and-vocabulary-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2013-xacml-compatibility-and-vocabulary-contract.yaml) — XACML Compatibility And Vocabulary Contract
- [`spc:policy-gateway-enforcement-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2014-policy-gateway-enforcement-contract.yaml) — Policy Gateway Enforcement Contract
- [`spc:authorization-audit-and-evidence-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2015-authorization-audit-and-evidence-contract.yaml) — Authorization Audit And Evidence Contract
- [`spc:least-privilege-and-negative-path-test-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2016-least-privilege-and-negative-path-test-contract.yaml) — Least Privilege And Negative Path Test Contract
- [`spc:token-to-policy-context-mapping-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2017-token-to-policy-context-mapping-contract.yaml) — Token To Policy Context Mapping Contract
- [`spc:authorization-failure-mode-and-cache-contract`](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates/specs/SPEC-2018-authorization-failure-mode-and-cache-contract.yaml) — Authorization Failure Mode And Cache Contract

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

#### uv

<!-- readme-standards:begin installation.uv -->
`authorization-policy-governance-pack` is not declared published. From the source checkout:

```bash
uv pip install .
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
`authorization-policy-governance-pack` is not declared published. From the source checkout:

```bash
python -m pip install .
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
`authorization-policy-governance-pack` is not declared published. From a separate Poetry project, replace the path with your checkout:

```bash
poetry add /path/to/authorization-policy-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from authorization_policy_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:authorization-policy"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:authorization-policy` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/examples/usage.py).

```python
"""Inspect the historical specification inventory without syncing it."""

from authorization_policy_governance_pack import load_document_manifest

specifications = load_document_manifest("spec")
assert specifications
assert all(specification["status"] == "superseded" for specification in specifications)
```
<!-- readme-standards:end example.usage -->

Review the [Migration guide](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md) before changing a downstream registry.

### Configuration

Select the installed import package `authorization_policy_governance_pack` in SSOT Registry. Review reservation owner `extension-pack:authorization-policy-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Historical records for Authorization Policy Governance. See the [Migration guide](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md) for current normative owners.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `authorization_policy_governance_pack` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/authorization-policy-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Migration guide](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md), [changelog](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/src/authorization_policy_governance_pack/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/authorization-policy-governance-pack)
- [Issues](https://github.com/groupsum/authorization-policy-governance-pack/issues)
- [Repository](https://github.com/groupsum/authorization-policy-governance-pack)
- [pypi: authorization-policy-governance-pack](https://pypi.org/project/authorization-policy-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/authorization-policy-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:authorization-policy`. The pack's reservation owner is `extension-pack:authorization-policy-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

Review the [governance documentation](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md) and the primary references carried by the individual records.

### Lifecycle and Migration

Follow the [Migration guide](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/MIGRATION.md) to identify replacement packages.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/authorization-policy-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
