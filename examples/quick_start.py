"""Inspect the installed pack identity."""

from digital_signature_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:digital-signature-governance"
print(metadata["origin"]["id"])
