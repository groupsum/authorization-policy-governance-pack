"""Inspect the historical specification inventory without syncing it."""

from authorization_policy_governance_pack import load_document_manifest

specifications = load_document_manifest("spec")
assert specifications
assert all(specification["status"] == "superseded" for specification in specifications)
