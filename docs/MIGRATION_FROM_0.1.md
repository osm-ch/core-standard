# Migration from OSM-CH 0.1

Version 0.1 verwendete einen einzigen flachen `VerfahrenRecord` mit universellen Pflichtfeldern für Fristen und Hilfsoptionen.

Core v1 ersetzt dieses Modell bewusst.

## Wichtigste Änderungen

1. **Type / Instance / Resolved statt Flat Record**
   - allgemeine Verfahrenslogik in ProcedureType;
   - lokale Abweichungen und Kontakte in ProcedureInstance;
   - deterministisches Resolve zum ResolvedProcedure.

2. **Keine künstlichen Pflichtmodule**
   - Fristen, Rechtsmittel, Risiken, Hilfsoptionen und weitere bedingte Module werden nicht erfunden, nur um ein Schema zu erfüllen.
   - fehlende/ungeklärte Information bleibt über Status/DataGap sichtbar.

3. **Explizite Provenienz**
   - SourceRecord bindet Aussagen an Quellen und Felder.
   - Verification und Freshness sind getrennt.

4. **LifeEvent und Execution**
   - mehrere Procedures können als LifeEvent orchestriert werden.
   - ExecutionStep und StepCardView trennen Verfahrenswahrheit von Präsentation.

5. **Trust chain**
   - SourceSnapshot, SourceRevalidationEvent und ValidationEvidence ergänzen eine reproduzierbare Nachweiskette.

## Legacy

Das frühere Schema bleibt nur zur Nachvollziehbarkeit unter:

`schema/legacy/verfahren-0.1.schema.json`

Das frühere Beispiel liegt unter:

`examples/legacy/iv-erstanmeldung.0.1.json`

Legacy-Dateien sind nicht Teil des v1-CI-Gates und erhalten keine neuen Features.

## Keine automatische semantische Migration

Ein 0.1-Datensatz soll nicht mechanisch mit erfundenen Werten aufgefüllt werden. Die Migration muss für jedes Feld zwischen:
- tatsächlich belegt,
- nicht anwendbar,
- unbekannt,
- strittig

unterscheiden.
