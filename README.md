# OSM-CH Core Standard

OSM-CH ist ein offener, maschinenlesbarer Kern für Schweizer Verwaltungsverfahren.

Der öffentliche Core beschreibt nicht, **welche Entscheidung eine Behörde treffen muss**. Er beschreibt nachvollziehbar und deterministisch:

- einen allgemeinen Verfahrenstyp;
- eine föderale oder lokale Instanz dieses Verfahrens;
- den daraus aufgelösten `ResolvedProcedure`;
- LifeEvents, die mehrere Verfahren orchestrieren;
- ausführbare Schritte und reine StepCard-Präsentationen;
- Source-Snapshots, Revalidation und Validation Evidence.

Der öffentliche Kern enthält **keine persönlichen Falldaten** und keine amtlichen Luzerner Inhaltskopien.

## Core v1

Normative Schemas liegen unter `schema/v1/`:

- `verfahren-typ.schema.json`
- `verfahren-instanz.schema.json`
- `resolved-verfahren.schema.json`
- `life-event.schema.json`
- `execution-step.schema.json`
- `step-card-view.schema.json`
- `source-snapshot.schema.json`
- `source-revalidation-event.schema.json`
- `validation-evidence.schema.json`

Wichtige Grundregeln:

1. Type + Instance werden deterministisch zu einem ResolvedProcedure aufgelöst.
2. Primitive Werte werden ersetzt, Objekte tief gemergt und Listen vollständig ersetzt.
3. Unbekannte Information wird nicht erfunden; DataGap und Status bleiben explizit.
4. `verification_status` und `freshness_status` sind getrennte Dimensionen.
5. Ein ausgeführter Schritt ist nicht automatisch ein bestätigtes Behördenresultat.
6. Persönliche Routing-Antworten und Task-Progress gehören nicht in den öffentlichen Katalog.
7. Source-Bytes sind Daten und werden vom Core-Validator nicht ausgeführt.
8. Probabilistische/LLM-Ausgaben sind keine Validierungs- oder Rechtsquelle.

## Synthetic quick start

Alle mitgelieferten Beispiele sind ausdrücklich synthetisch und verwenden Platzhalter-URLs.

```bash
python3 -m pip install -r validator/requirements.txt

python3 validator/validate.py \
  --type examples/adresswechsel-melden.typ.json \
  --instance examples/adresswechsel-melden.instanz.json \
  --resolved-out /tmp/adresswechsel.resolved.json

diff -u examples/adresswechsel-melden.resolved.json /tmp/adresswechsel.resolved.json
```

Ein einzelnes Artefakt kann direkt gegen sein Profil validiert werden:

```bash
python3 validator/validate.py \
  --profile resolved-verfahren \
  --validate examples/adresswechsel-melden.resolved.json
```

## Tests

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. python3 -m unittest discover -s tests -v
```

CI führt dieselbe Regression und den deterministischen Type/Instance-Resolve aus.

## Referenzimplementierung

Der öffentliche Core wird aus der privaten Entwicklungs-Workbench stabilisiert. Ein Ende-zu-Ende-Referenzfluss „Umzug nach Luzern“ wird in der Produkt-/Workbench-Schicht gepflegt und nicht als amtlicher Inhalt in dieses CC0-Kernrepo kopiert.

Siehe `docs/PROVENANCE.md`, `docs/CORE_CONTRACT.md`, `docs/MIGRATION_FROM_0.1.md` und den datensparsamen Luzern-Referenznachweis in `docs/REFERENCE_PROOF_LUZERN.md` / `reference/luzern-proof.json`.

## Contributing

Siehe `CONTRIBUTING.md`. Fehlende oder strittige amtliche Information soll als offene Lücke sichtbar bleiben, nicht durch Annahmen ersetzt werden.

## License

Dieses Repository steht unter **CC0 1.0 Universal**.

`SPDX-License-Identifier: CC0-1.0`
