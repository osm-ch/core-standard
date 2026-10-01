# Luzern reference proof

Stand: 2026-10-01

This document publishes only reproducibility metadata for the private end-to-end reference implementation. It does **not** publish official procedural content or personal data.

## Workbench

- Repository: `swisscomfort/Schweiz` (private)
- Commit: `e36a53ab1ffe06d47e1515580419ff56651ad232`
- Community gate: 89/89 tests passed
- Root schemas meta-validated: 12
- JSON artifacts parsed by the gate: 36
- Reference LifeEvent: `examples/p2-luzern/umzug-nach-luzern.life-event.json`
- LifeEvent SHA-256: `4ccdf92e29d62d84f02bef59de7b807bf280f2807cf4f558cfd4d496e1d8c4e4`
- Routed procedures: 7
- Derived execution steps in the citizen bundle: 7

## Citizen surface

- Repository: `swisscomfort/anspruchsradar-schweiz` (private)
- Commit: `ef8d4bb047ea6e785b15c417948fd407619afb1e`
- Generated bundle: `src/data/osm-luzern-reference.json`
- Bundle SHA-256: `4405766353bde18f26e72ea571079d3ec58987eca28015c2849c7ef5da286ac0`
- Bundle source commit recorded internally: `e36a53ab1ffe06d47e1515580419ff56651ad232`

The citizen bundle is generated deterministically from the workbench contracts and contains no personal routing answers or task progress.

## Boundary

The public Core does not depend on access to either private repository. These digests document that the published contracts have been exercised end-to-end against a real federal/cantonal/municipal reference flow while keeping official source material and private product code outside this CC0 repository.

This proof is an engineering attestation, not a legal certification of the underlying administrative content.
