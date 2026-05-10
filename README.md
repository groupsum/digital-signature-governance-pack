<div align="center">

<h1>digital-signature-governance-pack</h1>

<p>
  <a href="https://github.com/groupsum/digital-signature-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fdigital--signature--governance--pack-181717?logo=github"></a>
  <a href="https://github.com/groupsum/digital-signature-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://github.com/groupsum/digital-signature-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/digital-signature-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

</div>

`digital-signature-governance-pack` is an SSOT Registry pack for digital-signature, advanced electronic signature, container, timestamping, validation, archival, and assurance-language governance.

It gives product, platform, and compliance teams a reusable ADR/SPEC starting point for repositories that need to govern `PAdES`, `XAdES`, `CAdES`, `ASiC-S`, `ASiC-E`, validation reports, timestamping, certificate and revocation handling, long-term archival evidence, and constrained eIDAS-facing claim language.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed Architecture Decision Records (ADRs) and Specifications (SPECs) for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents that downstream repositories can synchronize into their local `.ssot` registry and link to features, tests, claims, evidence, and releases.

## Domain Focus

The initial review surface is grounded in TrustSig's `signature_and_container_standards_matrix.md` and covers:

- ETSI `PAdES`, `XAdES`, `CAdES`, and `ASiC` family standards
- baseline levels `B-B`, `B-T`, `B-LT`, and `B-LTA`
- PDF signature standards and ISO PDF extensions
- W3C XML Signature and canonicalization surfaces
- CMS, timestamping, PKIX, OCSP, ERS, XMLERS, and related RFCs
- validation result and validation report modeling
- cryptographic suite policy and algorithm allowlists
- regulatory-language boundaries for eIDAS-related claims

## Included ADRs

- `adr:0900` digital-signature standards targets are reviewed before governance inclusion

## Included SPECs

- `spc:0900` digital-signature governance target review

## Proposed ADR And SPEC Set

The first detailed proposal is documented in:

[Digital Signature ADR/SPEC Proposal](docs/proposals/digital-signature-adr-spec-proposal.md)

The source standards matrix copied from TrustSig is available at:

[Signature and Container Standards Matrix](docs/standards/signature-and-container-standards-matrix.md)

## Programmatic Usage

```python
from digital_signature_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-0900-digital-signature-governance-target-review.yaml")
print(text[:120])
```

## Resources

- GitHub repository: [groupsum/digital-signature-governance-pack](https://github.com/groupsum/digital-signature-governance-pack)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
