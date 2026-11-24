"""Find a specification and its downstream path in the installed manifest."""

from digital_signature_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:digital-signature-governance-target-review"
)
assert specification["target_path"] == ".ssot/specs/SPEC-0900-digital-signature-governance-target-review.yaml"
