# Security Policy

## Reporting

Sicherheitslücken bitte über GitHub Private Vulnerability Reporting / Security Advisories melden, nicht als öffentliches Issue mit Exploitdetails.

## Relevante Klassen

- Validator-/Parser-Ausführung von nicht vertrauenswürdigem Source-Material;
- Provenienz-, Hash- oder Validation-Evidence-Bypass;
- unsafe URI/Path Handling;
- CI-/Supply-Chain-Probleme;
- unbeabsichtigte Aufnahme persönlicher Daten in öffentliche Artefakte.

## Design boundary

Der öffentliche Core führt Source-Material nicht aus. Persönliche Fall- und Routingdaten gehören nicht in das Repository.
