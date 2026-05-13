<div align="center">

<h1>digital-signature-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/digital-signature-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/digital-signature-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/digital-signature-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/digital-signature-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/digital-signature-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/digital-signature-governance-pack.svg"></a>
  <a href="https://pypi.org/project/digital-signature-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/digital-signature-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/digital-signature-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/digital-signature-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/digital-signature-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/digital-signature-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/digital-signature-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fdigital--signature--governance--pack-181717?logo=github"></a>
</p>

</div>

`digital-signature-governance-pack` is an SSOT Registry pack for digital-signature, advanced electronic signature, container, timestamping, validation, archival, and assurance-language governance.

It gives product, platform, and compliance teams a reusable ADR/SPEC starting point for repositories that need to govern `PAdES`, `XAdES`, `CAdES`, `ASiC-S`, `ASiC-E`, validation reports, timestamping, certificate and revocation handling, long-term archival evidence, and constrained eIDAS-facing claim language.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed Architecture Decision Records (ADRs) and Specifications (SPECs) for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents that downstream repositories can synchronize into their local `.ssot` registry and link to features, tests, claims, evidence, and releases.

## Why This Pack Exists

Digital-signature governance crosses technical standards, cryptographic evidence, validation semantics, archival policy, and assurance wording. Teams need one reviewed source for the decisions and requirements that shape signature-family support, timestamping, validation reports, certificate and revocation handling, long-term evidence, and regulated claim language.

This pack helps teams:

- apply reviewed digital-signature governance requirements across projects
- distinguish signature family, baseline level, container, validation, timestamping, and archival requirements
- keep assurance and regulatory language tied to explicit evidence boundaries
- give product, platform, compliance, and implementation teams stable ADR and SPEC IDs
- connect downstream features, tests, claims, evidence, and releases to shared governance records

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

## Install With uv

Install the pack into a project environment:

```bash
uv add digital-signature-governance-pack
```

Install it alongside the SSOT Registry CLI:

```bash
uv add ssot-registry digital-signature-governance-pack
```

Run without adding dependencies to a project:

```bash
uvx --from ssot-registry --with digital-signature-governance-pack ssot --help
```

## Install With The SSOT Registry Pack CLI

Pack-enabled SSOT Registry environments can install and synchronize packs through the pack command surface:

```bash
uvx --from ssot-registry ssot pack install digital-signature-governance-pack
uvx --from ssot-registry ssot pack sync . digital-signature-governance-pack
```

## Use With The SSOT Registry CLI

After the pack is installed in the same environment as `ssot-registry`, synchronize ADRs and SPECs into a target repository:

```bash
uv run ssot adr sync .
uv run ssot spec sync .
```

Review the synchronized governance surface:

```bash
uv run ssot adr list .
uv run ssot spec list .
uv run ssot spec get . --id spc:0900
```

Use the IDs from this pack when linking project features, tests, claims, and release evidence in your local `.ssot` registry.

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
- PyPI package: [digital-signature-governance-pack](https://pypi.org/project/digital-signature-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
