# Contributing to OSM-CH Core

OSM-CH Core akzeptiert Änderungen an stabilen Schemas, Validator, synthetischen Beispielen und öffentlicher Dokumentation.

## Vor einem Pull Request

```bash
python3 -m pip install -r validator/requirements.txt
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. python3 -m unittest discover -s tests -v
```

## Regeln

- Keine persönlichen Daten, Fallakten, AHV-Nummern oder persönlichen Task-States.
- Keine amtlichen Behauptungen ohne klar getrennte Daten-/Quellschicht.
- Beispiele im Core müssen synthetisch sein.
- Unbekanntes nicht erraten; Lücken und Konflikte explizit halten.
- Schemaänderungen brauchen Migrationshinweis und Regressionstest.
- Listen-Merge-Semantik darf nicht still verändert werden.
- LLM/AI darf Entwürfe oder Review-Triage unterstützen, aber keine Verifikation oder DataGap-Auflösung autorisieren.
- Neue Dateien müssen mit CC0-1.0 kompatibel sein; unklare Provenienz blockiert den Merge.

## Scope

Amtliche Schweizer Verfahrensdaten gehören nicht in dieses Core-Repository. Sie können in separaten Daten-/Referenzrepos gepflegt werden, solange sie den Core-Verträgen entsprechen.

## Review

Änderungen an Identität, Provenienz, Merge-Semantik oder Validation Evidence benötigen eine unabhängige zweite Prüfung.
