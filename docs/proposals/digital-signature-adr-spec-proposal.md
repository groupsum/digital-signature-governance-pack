# Digital Signature ADR/SPEC Proposal

Source basis: `docs/standards/signature-and-container-standards-matrix.md`, copied from TrustSig's `docs/signature_and_container_standards_matrix.md`.

This proposal keeps the first pack release conservative: the packaged `adr:0900` and `spc:0900` govern target review. The rows below are the proposed promotion set for a digital-signature governance pack once the standards inventory is accepted.

## Proposed ADRs

| Proposed ID | Title | Governs | Primary Targets |
| --- | --- | --- | --- |
| `adr:0901` | Advanced electronic signature families are governed separately | Treat `PAdES`, `XAdES`, `CAdES`, and `ASiC` as distinct families rather than one generic signature capability | ETSI EN 319 142-1, EN 319 132-1, EN 319 122-1, EN 319 162-1 |
| `adr:0902` | Baseline levels are explicit capability claims | Model `B-B`, `B-T`, `B-LT`, and `B-LTA` as separate governed obligations | ETSI EN 319 142-1, EN 319 132-1, EN 319 122-1, EN 319 102-1 |
| `adr:0903` | Timestamping is a shared cross-family service boundary | Keep timestamp acquisition, verification, and token-profile policy separate from signature-family parsing | RFC 3161, RFC 5816, ETSI EN 319 422 |
| `adr:0904` | Validation procedure and report model are separate from family syntax | Govern validation semantics and report payloads independently from PAdES/XAdES/CAdES parser support | ETSI EN 319 102-1, ETSI TS 119 102-2 |
| `adr:0905` | Cryptographic suite policy is centrally governed | Use one policy surface for allowed, deprecated, and rejected algorithms across all signature families | ETSI TS 119 312, RFC 5280 |
| `adr:0906` | ASiC containers are governed by container form and payload signature family | Split `ASiC-S`, `ASiC-E`, and embedded `CAdES`/`XAdES` payload obligations | ETSI EN 319 162-1, EN 319 122-1, EN 319 132-1 |
| `adr:0907` | PDF and XML syntax layers are supporting standards, not standalone conformance claims | Treat ISO PDF and W3C XML Signature references as syntax dependencies unless the product explicitly claims them | ISO 32000-2, ISO/TS 32001-32003, W3C XML Signature 1.1 |
| `adr:0908` | Long-term archival evidence is governed as retention behavior | Separate archival renewal, evidence records, and preservation obligations from ordinary validation | RFC 4998, RFC 6283, ETSI EN 319 102-1 |
| `adr:0909` | Regulatory language is bounded by evidence | Use eIDAS as an assurance-language and claim-boundary reference, not an automatic compliance assertion | Regulation (EU) No 910/2014 |
| `adr:0910` | Out-of-scope and watchlist standards remain visible | Track extended profiles, delegated validation, and adjacent standards without silently turning them into commitments | ETSI EN 319 142-2, EN 319 132-2, EN 319 122-2, EN 319 162-2, RFC 5055 |

## Proposed SPECs

| Proposed ID | Title | Requirements Surface | Primary Targets |
| --- | --- | --- | --- |
| `spc:0901` | PAdES baseline support contract | PDF signature parsing, validation inputs, baseline-level mapping, and claim boundaries for `PAdES-B-B/T/LT/LTA` | ETSI EN 319 142-1, ISO 32000-2, ISO/TS 32001, ISO/TS 32002 |
| `spc:0902` | XAdES baseline support contract | XML signature handling, canonicalization, qualifying properties, and `XAdES-B-B/T/LT/LTA` mapping | ETSI EN 319 132-1, W3C XML Signature 1.1, Exclusive XML Canonicalization |
| `spc:0903` | CAdES baseline support contract | CMS signature handling and `CAdES-B-B/T/LT/LTA` mapping | ETSI EN 319 122-1, RFC 5652 |
| `spc:0904` | ASiC container support contract | `ASiC-S`, `ASiC-E`, manifest/container validation, and embedded `XAdES`/`CAdES` payload handling | ETSI EN 319 162-1, EN 319 132-1, EN 319 122-1 |
| `spc:0905` | Baseline level obligation contract | Shared `B-B`, `B-T`, `B-LT`, and `B-LTA` requirement ladder across supported signature families | ETSI EN 319 102-1, EN 319 422, RFC 5280, RFC 6960 |
| `spc:0906` | Timestamp token contract | Timestamp request, token acceptance, token verification, ESSCertIDv2 handling, and renewal constraints | RFC 3161, RFC 5816, ETSI EN 319 422 |
| `spc:0907` | Certificate path and revocation validation contract | Certificate chain, CRL/OCSP, revocation material capture, and validation-time policy | RFC 5280, RFC 6960, ETSI EN 319 102-1 |
| `spc:0908` | Validation report contract | Machine-readable verification result, detailed validation report mapping, and failure semantics | ETSI EN 319 102-1, ETSI TS 119 102-2 |
| `spc:0909` | Cryptographic suite policy contract | Algorithm allowlist, deprecation, rejection, and evidence requirements for crypto-policy decisions | ETSI TS 119 312, RFC 5280 |
| `spc:0910` | Long-term archival evidence contract | LTA renewal, evidence record syntax, XML evidence records, and retention-period verification | RFC 4998, RFC 6283, ETSI EN 319 102-1, ETSI EN 319 422 |
| `spc:0911` | Assurance and regulatory claim-language contract | Product wording, compliance boundaries, qualified-signature caveats, and evidence gates for eIDAS-facing language | Regulation (EU) No 910/2014, ETSI TR 119 001 |
| `spc:0912` | Extended and watchlist profile tracking contract | Explicit handling for extended ETSI profiles, delegated validation, and future standards without overclaiming support | ETSI EN 319 142-2, EN 319 132-2, EN 319 122-2, EN 319 162-2, RFC 5055 |

## Promotion Order

1. Promote `adr:0901`, `adr:0902`, and `spc:0905` first so family and baseline taxonomy is stable.
2. Promote `spc:0901` through `spc:0904` next so family/container contracts can link to the shared baseline ladder.
3. Promote `spc:0906` through `spc:0910` after the shared validation, timestamping, crypto, and archival semantics are settled.
4. Promote `adr:0909`, `spc:0911`, and `spc:0912` before public compliance or extended-profile claims are made.
