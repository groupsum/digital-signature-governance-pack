<div align="center">

<h1>ssot-registry-pack-template</h1>

<p>
  <a href="https://github.com/groupsum/ssot-registry-pack-template"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fssot--registry--pack--template-181717?logo=github"></a>
  <a href="https://github.com/groupsum/ssot-registry-pack-template/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://github.com/groupsum/ssot-registry-pack-template/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/ssot-registry-pack-template/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

</div>

`ssot-registry-pack-template` is a starter repository for creating installable SSOT Registry governance packs.

Use it when a governance domain needs reusable Architecture Decision Records (ADRs), Specifications (SPECs), manifests, tests, and packaging metadata that can be installed beside [`ssot-registry`](https://pypi.org/project/ssot-registry/) and synchronized into downstream repositories.

## Template Scope

This template provides:

- a Python package that exposes packaged ADR and SPEC documents
- manifest loaders for pack-aware SSOT Registry workflows
- placeholder ADR and SPEC documents that demonstrate the required shape
- tests that verify manifest rows and packaged documents stay loadable
- a document sync script for copying repo-local `.ssot` source documents into package data
- CI and publish workflow placeholders suitable for a new governance-pack repository

## Create A Pack From This Template

Create a new private repository from this template, then replace the placeholder values:

```bash
gh repo create groupsum/example-governance-pack --private --template groupsum/ssot-registry-pack-template --clone
```

Update these values before the first release:

- package name in `pyproject.toml`
- import package directory under `src/`
- package-data keys in `pyproject.toml`
- package origin values in packaged ADR and SPEC YAML files
- manifest rows under `src/<package_name>/templates/**/manifest.json`
- README domain language and included ADR/SPEC lists
- test import paths and expected document IDs

## Included Placeholder ADRs

- `adr:0001` pack governance scope is explicit

## Included Placeholder SPECs

- `spc:0001` pack document contract

## Authoring Flow

1. Author source ADRs in `.ssot/adr`.
2. Author source SPECs in `.ssot/specs`.
3. Run `python scripts/sync_packaged_docs.py` after setting the package paths for the new pack.
4. Run tests to verify manifests and packaged documents.
5. Publish the pack only after the ADR/SPEC surface is intentionally scoped.

## Programmatic Usage

```python
from ssot_registry_pack_template import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-0001-pack-document-contract.yaml")
print(text[:120])
```

## Resources

- GitHub repository: [groupsum/ssot-registry-pack-template](https://github.com/groupsum/ssot-registry-pack-template)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
