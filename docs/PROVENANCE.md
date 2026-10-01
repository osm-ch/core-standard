# Provenance and CC0 export

Stand: 2026-10-01

## Export source

Core v1 wurde aus der OSM-CH Entwicklungs-Workbench stabilisiert:

- Source repository: `swisscomfort/Schweiz`
- geprüfter Exportstand: `e36a53ab1ffe06d47e1515580419ff56651ad232`
- Ziel: `osm-ch/core-standard`

Die exportierten v1-Schemas sind projekt-eigene Verträge aus der OSM-CH-Entwicklung. Der öffentliche Validator in diesem Repository ist eine kleine, eigenständige CC0-Referenzimplementierung für diese Verträge.

## Nicht exportiert

Nicht in den öffentlichen CC0-Core kopiert wurden:

- amtliche Luzerner Quelltexte oder vollständige Behördeninhalte;
- persönliche Routing-Antworten, Task-Status oder Falldaten;
- private Workbench-Analysen;
- Code aus Drittanbieter-Repositories oder Reuse-Kandidaten mit unklarer Lizenz;
- TypeSafe/Jev-Implementierungen;
- UI-Code aus AnspruchsRadar;
- SourceStore-/Crawler-Code aus RepoKompass.

Die Beispiele in `examples/` sind ausdrücklich synthetische Fixtures und verwenden `example.org`.

## Reuse boundaries

Engineering-Muster aus anderen Projekten haben die Architektur beeinflusst, werden hier aber nicht als fremder Code eingebettet. Dazu gehören unter anderem Action-Lifecycle-, SourceStore-, Freshness- und unabhängige Review-Muster.

## License marker

Neue normative JSON-Schemas tragen:

`"$comment": "SPDX-License-Identifier: CC0-1.0"`

Python-Dateien tragen:

`# SPDX-License-Identifier: CC0-1.0`

Die Repository-Lizenz bleibt CC0-1.0.

## Provenance gate

Ein künftiger Exportbestandteil darf nur aufgenommen werden, wenn Herkunft und Rechtebasis klar genug sind, um ihn unter der Repository-Lizenz zu veröffentlichen. Unklare Herkunft ist ein Merge-Blocker.
