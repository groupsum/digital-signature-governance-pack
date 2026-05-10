# SSOT Registry Pack Authoring Guide

This template is intentionally generic. A concrete pack should replace the placeholder ADR and SPEC with a domain-specific governance scope before publication.

## Required Decisions

- Define the governed domain in the first ADR.
- List the standards, policies, or product surfaces that are in scope.
- Keep watchlist and out-of-scope candidates visible when they are adjacent to the governed domain.
- Split detailed SPECs by behavior surface, not by implementation library.
- Avoid broad compliance claims until features, tests, claims, and evidence exist in downstream repositories.

## Required Package Updates

- Rename `src/ssot_registry_pack_template` to the import package for the new pack.
- Update `pyproject.toml` project metadata, URLs, keywords, and package-data keys.
- Update `scripts/sync_packaged_docs.py` and `scripts/bump_version.py` package paths.
- Replace manifest rows after replacing the packaged ADR and SPEC documents.
- Update tests so they verify the exact ADR and SPEC IDs shipped by the pack.

## Recommended Initial Document Set

- One ADR that defines the pack boundary and standards inclusion policy.
- One SPEC that defines target-review requirements.
- One SPEC per governed behavior surface once the target set is reviewed.
- One README section listing included ADRs and SPECs by stable SSOT ID.
