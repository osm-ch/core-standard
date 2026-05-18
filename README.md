# OSM-CH 0.1 – Offenlegungsstandard Schweiz

Barrierefreiheit (Accessibility) ist inkomplett ohne maschinenlesbare Handlungsfähigkeit (Actionability). Behördenportale, die Formulare als unstrukturierte PDFs oder reine Text-Webseiten digitalisieren, digitalisieren das Papier, nicht den Prozess. 

**OSM-CH** ist ein kanonisches Datenmodell (JSON-Schema) und ein Compliance-Regelwerk. Es zwingt staatliche Stellen dazu, Verfahrenslogiken – insbesondere Fristen, Risiken, Verzweigungen und Hilfsangebote – deterministisch und maschinenlesbar offenzulegen.

Dieser Standard ist Public Domain (CC0). Er ist als Open-Source-Drop konzipiert. Civic-Tech-Entwickler, NGOs und Architekten sind aufgerufen, dieses Schema zu nutzen, um kantonalen Vollzug auditierbar zu machen.

## Architektur-Prinzipien
1. **Deterministische Actionability:** Ein Verfahren ohne maschinenlesbaren nächsten Schritt, dokumentierte Rechtsfolgen bei Fristversäumnis und explizite Minimalhandlungen ist nicht konform (Hard Fail).
2. **Shift-Left Validierung:** Validierung passiert im CI/CD-Prozess der Behörden.
3. **Föderaler Namespace:** Kollisionsfreie Identifikatoren durch eCH-kompatible URNs (z.B. `urn:osm-ch:ch-zh:iv-erstanmeldung:v1`).

## Quick Start (Validator)
```bash
pip install -r validator/requirements.txt
python validator/app.py --validate examples/iv-erstanmeldung.minimal.json
```
