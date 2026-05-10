from __future__ import annotations

import json
import unittest

from ssot_registry_pack_template import load_document_manifest, read_packaged_document_text


class TemplateManifestTests(unittest.TestCase):
    def test_adr_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("adr")
        self.assertEqual(1, len(manifest))
        self.assertEqual(
            [
                "adr:0001",
            ],
            [row["id"] for row in manifest],
        )

    def test_spec_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("spec")
        self.assertEqual(1, len(manifest))
        self.assertEqual(
            [
                "spc:0001",
            ],
            [row["id"] for row in manifest],
        )

    def test_packaged_document_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0001-pack-document-contract.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0001", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])

    def test_packaged_adr_can_be_loaded(self) -> None:
        text = read_packaged_document_text("adr", "ADR-0001-pack-governance-scope-is-explicit.yaml")
        payload = json.loads(text)
        self.assertEqual("adr:0001", payload["id"])
        self.assertEqual(
            "Pack governance scope is explicit",
            payload["title"],
        )

    def test_packaged_spec_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0001-pack-document-contract.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0001", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])


if __name__ == "__main__":
    unittest.main()
