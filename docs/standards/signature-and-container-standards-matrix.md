# TrustSig Signature and Container Standards Matrix

_Last updated: 2026-05-10_

This document consolidates the standards and specifications discussed for TrustSig's signature, container, timestamping, validation, archival, and compliance surfaces. Each detailed table row includes linked source material.

## Category Summary

| Category | Covered Standards / Specs | Notes |
| --- | --- | --- |
| Core ETSI ENs | `EN 319 142-1`, `EN 319 142-2`, `EN 319 132-1`, `EN 319 132-2`, `EN 319 122-1`, `EN 319 122-2`, `EN 319 162-1`, `EN 319 162-2` | Family-level standards for `PAdES`, `XAdES`, `CAdES`, `ASiC-S`, and `ASiC-E` |
| ETSI validation / policy / crypto specs | `EN 319 102-1`, `TS 119 102-2`, `EN 319 422`, `TS 119 312`, `TR 119 001` | Validation procedure, validation report, timestamping, crypto suites, terminology |
| ISO / ISO-TS | `ISO 32000-2`, `ISO/TS 32001`, `ISO/TS 32002`, `ISO/TS 32003` | Primarily relevant to `PAdES` and PDF handling |
| W3C | `XML Signature 1.1`, XML Signature overview, Exclusive XML Canonicalization | Primarily relevant to `XAdES` |
| IETF / RFCs | `RFC 5652`, `RFC 3161`, `RFC 5816`, `RFC 5280`, `RFC 6960`, `RFC 4998`, `RFC 6283`, `RFC 3275`, `RFC 3076`, `RFC 5055` | CMS, timestamps, PKI, revocation, archival evidence, XML signature |
| Regulatory / legal framework | `Regulation (EU) No 910/2014` (`eIDAS`) | Relevant to product claims, not automatic conformance |
| Baseline timestamp / long-term levels | `B-B`, `B-T`, `B-LT`, `B-LTA` | Applies across `PAdES`, `XAdES`, and `CAdES` families |
| XAdES baselines | `XAdES-B-B`, `XAdES-B-T`, `XAdES-B-LT`, `XAdES-B-LTA` | XML signature baseline ladder |
| CAdES baselines | `CAdES-B-B`, `CAdES-B-T`, `CAdES-B-LT`, `CAdES-B-LTA` | CMS signature baseline ladder |
| PAdES baselines | `PAdES-B-B`, `PAdES-B-T`, `PAdES-B-LT`, `PAdES-B-LTA` | PDF signature baseline ladder |
| ASiC baselines | `ASiC-S`, `ASiC-E`, plus `ASiC` with `XAdES` or `CAdES` payloads | Container baseline forms rather than the `B-B/B-T/B-LT/B-LTA` ladder |

## Core ETSI ENs

| Standard / Spec | Scope | TrustSig Relevance | Source |
| --- | --- | --- | --- |
| `ETSI EN 319 142-1` | PAdES baseline signatures | Core standard for `PAdES` support and verification claims | [ETSI EN 319 142-1 V1.2.1](https://www.etsi.org/deliver/etsi_EN/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf) |
| `ETSI EN 319 142-2` | PAdES additional profiles | Relevant if TrustSig claims beyond baseline `PAdES` | [ETSI work item](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=TRUE&WKI_ID=73781&butExpertSearch=Search&curItemNr=142&includeNonActiveTB=FALSE&includeSubProjectCode=&optDisplay=100000&qCLUSTER=19&qCLUSTER_BOOLEAN=&qEND_CURRENT_STATUS_CODE=11+WI%3BM58&qETSI_ALL=&qFREQUENCIES_BOOLEAN=&qINCLUDE_MOVED_ON=&qINCLUDE_SUB_TB=&qKEYWORD_BOOLEAN=&qREPORT_TYPE=&qSORT=TB&qSTOPPING_OUTDATED=&qSTOP_FLG=N&totalNrItems=299) |
| `ETSI EN 319 132-1` | XAdES baseline signatures | Core standard for `XAdES` support and baseline levels | [ETSI EN 319 132-1 V1.3.1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf) |
| `ETSI EN 319 132-2` | XAdES extended signatures | Relevant if TrustSig claims extended XML-signature behavior | [ETSI EN 319 132-2 V1.1.1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913202/01.01.01_60/en_31913202v010101p.pdf) |
| `ETSI EN 319 122-1` | CAdES baseline signatures | Core standard for `CAdES` support and baseline levels | [ETSI EN 319 122-1 V1.3.1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf) |
| `ETSI EN 319 122-2` | CAdES extended signatures | Relevant if TrustSig claims extended CMS-signature behavior | [ETSI EN 319 122-2 V1.1.1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912202/01.01.01_60/en_31912202v010101p.pdf) |
| `ETSI EN 319 162-1` | ASiC baseline containers | Core standard for `ASiC-S` and `ASiC-E` support | [ETSI EN 319 162-1 V1.1.1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf) |
| `ETSI EN 319 162-2` | ASiC additional container profiles | Relevant if TrustSig claims beyond baseline `ASiC` support | [ETSI work item](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=39488) |

## ETSI Validation / Policy / Crypto Specs

| Standard / Spec | Scope | TrustSig Relevance | Source |
| --- | --- | --- | --- |
| `ETSI EN 319 102-1` | Procedures for creation and validation of AdES signatures | Central for validation semantics across `PAdES`, `XAdES`, and `CAdES` | [ETSI EN 319 102-1 V1.4.1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf) |
| `ETSI TS 119 102-2` | Signature validation report | Relevant to TrustSig verification result and report modeling | [ETSI TS 119 102-2 V1.2.1](https://www.etsi.org/deliver/etsi_TS/119100_119199/11910202/01.02.01_60/ts_11910202v010201p.pdf) |
| `ETSI EN 319 422` | Time-stamping protocol and token profiles | Directly relevant to `B-T`, `B-LT`, and `B-LTA` claims | [ETSI EN 319 422 V1.1.1](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |
| `ETSI TS 119 312` | Cryptographic suites and algorithms | Relevant to algorithm support and crypto-policy claims | [ETSI TS 119 312 V1.5.1](https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.05.01_60/ts_119312v010501p.pdf) |
| `ETSI TR 119 001` | Definitions and terminology | Useful vocabulary anchor for assurance and compliance language | [ETSI TR 119 001 V1.2.1](https://www.etsi.org/deliver/etsi_tr/119000_119099/119001/01.02.01_60/tr_119001v010201p.pdf) |

## ISO / ISO-TS

| Standard / Spec | Scope | TrustSig Relevance | Source |
| --- | --- | --- | --- |
| `ISO 32000-2:2017` | PDF 2.0 | Base document format standard under `PAdES` | [ISO 32000-2](https://www.iso.org/standard/63534.html) |
| `ISO/TS 32001:2022` | PDF hash algorithm extensions | Relevant if TrustSig claims newer PDF-signature hash support | [ISO/TS 32001](https://www.iso.org/standard/45874.html) |
| `ISO/TS 32002:2022` | PDF digital-signature extensions | Relevant for advanced `PAdES` algorithm support claims | [ISO/TS 32002](https://www.iso.org/standard/45875.html) |
| `ISO/TS 32003:2023` | PDF AES-GCM extensions | Adjacent to secure PDF handling | [ISO/TS 32003](https://www.iso.org/standard/45876.html) |

## W3C

| Standard / Spec | Scope | TrustSig Relevance | Source |
| --- | --- | --- | --- |
| `XML Signature Syntax and Processing 1.1` | XML digital signature syntax and processing | Base syntax layer under `XAdES` | [W3C XML Signature 1.1](https://www.w3.org/TR/xmldsig-core/) |
| `XML Signature family overview` | Historical and ecosystem overview | Supporting reference for XML-signature context | [W3C XML Signature page](https://www.w3.org/2000/09/xmldsig) |
| `Exclusive XML Canonicalization` | XML canonicalization rules | Relevant to `XAdES` interoperability and verification | [W3C Recommendation notice](https://www.w3.org/news/2002/exclusive-xml-canonicalization-is-a-w3c-recommendation/) |

## IETF / RFCs

| Standard / Spec | Scope | TrustSig Relevance | Source |
| --- | --- | --- | --- |
| `RFC 5652` | Cryptographic Message Syntax (CMS) | Base syntax layer under `CAdES` | [RFC 5652](https://www.rfc-editor.org/info/rfc5652) |
| `RFC 3161` | Time-Stamp Protocol | Core timestamping standard for `B-T` and above | [RFC 3161](https://www.rfc-editor.org/info/rfc3161) |
| `RFC 5816` | RFC 3161 update for `ESSCertIDv2` | Important timestamping/profile update | [RFC 5816](https://www.rfc-editor.org/info/rfc5816) |
| `RFC 5280` | PKIX certificate and CRL profile | Core certificate and revocation-validation standard | [RFC 5280](https://www.ietf.org/rfc/rfc5280.html) |
| `RFC 6960` | Online Certificate Status Protocol (OCSP) | Core revocation-checking standard for `LT` and `LTA` validation | [RFC 6960](https://www.rfc-editor.org/info/rfc6960) |
| `RFC 4998` | Evidence Record Syntax (ERS) | Important for long-term archival evidence | [RFC 4998](https://www.rfc-editor.org/info/rfc4998) |
| `RFC 6283` | XML Evidence Record Syntax (XMLERS) | XML archival evidence equivalent | [RFC 6283](https://www.rfc-editor.org/info/rfc6283) |
| `RFC 3275` | XML-Signature Syntax and Processing | Historical IETF XML signature reference | [RFC 3275](https://www.rfc-editor.org/info/rfc3275) |
| `RFC 3076` | Canonical XML | Relevant to XML-signature normalization | [RFC 3076](https://www.rfc-editor.org/info/rfc3076) |
| `RFC 5055` | SCVP | Adjacent if validation is delegated or centralized | [RFC 5055](https://www.rfc-editor.org/info/rfc5055) |

## Regulatory / Legal Framework

| Standard / Spec | Scope | TrustSig Relevance | Source |
| --- | --- | --- | --- |
| `Regulation (EU) No 910/2014` (`eIDAS`) | EU trust services and electronic identification framework | Relevant to compliance language and claim boundaries, not automatic conformance | [EUR-Lex consolidated eIDAS text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32014R0910) |

## Shared Baseline Timestamp and Long-Term Levels

| Level | Meaning | What It Adds | Primary Standards | Sources |
| --- | --- | --- | --- | --- |
| `B-B` | Baseline Basic | Core valid signature structure | `EN 319 142-1`, `EN 319 132-1`, `EN 319 122-1` | [PAdES](https://www.etsi.org/deliver/etsi_EN/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf), [XAdES](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [CAdES](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf) |
| `B-T` | Baseline with Timestamp | Trusted timestamp token over signature or signature data | `RFC 3161`, `RFC 5816`, `EN 319 422` | [RFC 3161](https://www.rfc-editor.org/info/rfc3161), [RFC 5816](https://www.rfc-editor.org/info/rfc5816), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |
| `B-LT` | Baseline Long Term | Validation material needed later, typically cert and revocation data | `EN 319 102-1`, `RFC 5280`, `RFC 6960` | [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 5280](https://www.ietf.org/rfc/rfc5280.html), [RFC 6960](https://www.rfc-editor.org/info/rfc6960) |
| `B-LTA` | Baseline Long Term Archival | Archival protection and timestamp renewal over long retention periods | `EN 319 102-1`, `RFC 4998`, `RFC 6283`, `EN 319 422` | [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 4998](https://www.rfc-editor.org/info/rfc4998), [RFC 6283](https://www.rfc-editor.org/info/rfc6283), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |

## XAdES Baselines

| Baseline Level | Meaning | Primary Standards | Sources |
| --- | --- | --- | --- |
| `XAdES-B-B` | Baseline basic XML advanced electronic signature | `EN 319 132-1`, `XML Signature 1.1` | [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [W3C XML Signature 1.1](https://www.w3.org/TR/xmldsig-core/) |
| `XAdES-B-T` | `B-B` plus trusted timestamp | `EN 319 132-1`, `RFC 3161`, `RFC 5816`, `EN 319 422` | [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [RFC 3161](https://www.rfc-editor.org/info/rfc3161), [RFC 5816](https://www.rfc-editor.org/info/rfc5816), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |
| `XAdES-B-LT` | `B-T` plus long-term validation data | `EN 319 132-1`, `EN 319 102-1`, `RFC 5280`, `RFC 6960` | [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 5280](https://www.ietf.org/rfc/rfc5280.html), [RFC 6960](https://www.rfc-editor.org/info/rfc6960) |
| `XAdES-B-LTA` | `B-LT` plus archival protection and renewal | `EN 319 132-1`, `EN 319 102-1`, `RFC 4998`, `RFC 6283`, `EN 319 422` | [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 4998](https://www.rfc-editor.org/info/rfc4998), [RFC 6283](https://www.rfc-editor.org/info/rfc6283), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |

## CAdES Baselines

| Baseline Level | Meaning | Primary Standards | Sources |
| --- | --- | --- | --- |
| `CAdES-B-B` | Baseline basic CMS advanced electronic signature | `EN 319 122-1`, `RFC 5652` | [ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf), [RFC 5652](https://www.rfc-editor.org/info/rfc5652) |
| `CAdES-B-T` | `B-B` plus trusted timestamp | `EN 319 122-1`, `RFC 3161`, `RFC 5816`, `EN 319 422` | [ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf), [RFC 3161](https://www.rfc-editor.org/info/rfc3161), [RFC 5816](https://www.rfc-editor.org/info/rfc5816), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |
| `CAdES-B-LT` | `B-T` plus long-term validation material | `EN 319 122-1`, `EN 319 102-1`, `RFC 5280`, `RFC 6960` | [ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf), [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 5280](https://www.ietf.org/rfc/rfc5280.html), [RFC 6960](https://www.rfc-editor.org/info/rfc6960) |
| `CAdES-B-LTA` | `B-LT` plus archival maintenance and evidence preservation | `EN 319 122-1`, `EN 319 102-1`, `RFC 4998`, `EN 319 422` | [ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf), [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 4998](https://www.rfc-editor.org/info/rfc4998), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |

## PAdES Baselines

| Baseline Level | Meaning | Primary Standards | Sources |
| --- | --- | --- | --- |
| `PAdES-B-B` | Baseline basic PDF advanced electronic signature | `EN 319 142-1`, `ISO 32000-2` | [ETSI EN 319 142-1](https://www.etsi.org/deliver/etsi_EN/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf), [ISO 32000-2](https://www.iso.org/standard/63534.html) |
| `PAdES-B-T` | `B-B` plus trusted timestamp | `EN 319 142-1`, `RFC 3161`, `RFC 5816`, `EN 319 422` | [ETSI EN 319 142-1](https://www.etsi.org/deliver/etsi_EN/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf), [RFC 3161](https://www.rfc-editor.org/info/rfc3161), [RFC 5816](https://www.rfc-editor.org/info/rfc5816), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |
| `PAdES-B-LT` | `B-T` plus embedded long-term validation material | `EN 319 142-1`, `EN 319 102-1`, `RFC 5280`, `RFC 6960` | [ETSI EN 319 142-1](https://www.etsi.org/deliver/etsi_EN/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf), [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 5280](https://www.ietf.org/rfc/rfc5280.html), [RFC 6960](https://www.rfc-editor.org/info/rfc6960) |
| `PAdES-B-LTA` | `B-LT` plus archival timestamping and long-term archival maintenance | `EN 319 142-1`, `EN 319 102-1`, `RFC 4998`, `EN 319 422` | [ETSI EN 319 142-1](https://www.etsi.org/deliver/etsi_EN/319100_319199/31914201/01.02.01_60/en_31914201v010201p.pdf), [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.01_60/en_31910201v010401p.pdf), [RFC 4998](https://www.rfc-editor.org/info/rfc4998), [ETSI EN 319 422](https://www.etsi.org/deliver/etsi_en/319400_319499/319422/01.01.01_60/en_319422v010101p.pdf) |

## ASiC Baselines

| Baseline Form | Meaning | Primary Standards | Sources |
| --- | --- | --- | --- |
| `ASiC-S` | Baseline single-object container | One signed data object or one signature object associated with one data object | `EN 319 162-1` | [ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf) |
| `ASiC-E` | Baseline extended container | Multiple files or signatures in one container with manifest structure | `EN 319 162-1` | [ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf) |
| `ASiC-S` with `CAdES` | Baseline containerized CAdES | `ASiC-S` carrying `CAdES` signature material | `EN 319 162-1`, `EN 319 122-1`, `RFC 5652` | [ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf), [ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf), [RFC 5652](https://www.rfc-editor.org/info/rfc5652) |
| `ASiC-S` with `XAdES` | Baseline containerized XAdES | `ASiC-S` carrying `XAdES` signature material | `EN 319 162-1`, `EN 319 132-1`, `XML Signature 1.1` | [ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf), [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [W3C XML Signature 1.1](https://www.w3.org/TR/xmldsig-core/) |
| `ASiC-E` with `CAdES` | Baseline extended containerized CAdES | `ASiC-E` carrying multi-file or richer package `CAdES` signing flows | `EN 319 162-1`, `EN 319 122-1`, `RFC 5652` | [ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf), [ETSI EN 319 122-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31912201/01.03.01_60/en_31912201v010301p.pdf), [RFC 5652](https://www.rfc-editor.org/info/rfc5652) |
| `ASiC-E` with `XAdES` | Baseline extended containerized XAdES | `ASiC-E` carrying multi-file or richer package `XAdES` signing flows | `EN 319 162-1`, `EN 319 132-1`, `XML Signature 1.1` | [ETSI EN 319 162-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31916201/01.01.01_60/en_31916201v010101p.pdf), [ETSI EN 319 132-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31913201/01.03.01_60/en_31913201v010301p.pdf), [W3C XML Signature 1.1](https://www.w3.org/TR/xmldsig-core/) |

## TrustSig Pack Context

This governance pack currently ships a target-review ADR and SPEC under `src/digital_signature_governance_pack/templates`.
Future pack rows should be authored in that package template tree, then linked by stable SSOT ID after the governed surface is accepted.

Candidate downstream contract IDs for future rows include:

| TrustSig Surface | Candidate Contract ID |
| --- | --- |
| `PAdES` family support | `spc:1010` |
| `XAdES` family support | `spc:1011` |
| `CAdES` family support | `spc:1012` |
| `ASiC-S` and `ASiC-E` family support | `spc:1013` |
| Verification result model | `spc:1007` |
| Assurance/compliance language policy | `spc:1001` |

The pack does not yet explicitly model each baseline level such as `PAdES-B-T`, `XAdES-B-LT`, or `CAdES-B-LTA` as separate governed SSOT rows.
