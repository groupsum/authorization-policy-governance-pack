"""Inspect the installed pack identity."""

from authorization_policy_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:authorization-policy"
print(metadata["origin"]["id"])
