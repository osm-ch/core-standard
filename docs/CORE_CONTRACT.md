# Core v1 contract

## Public entities

### ProcedureType

Allgemeine semantische Beschreibung eines Verwaltungsverfahrens.

### ProcedureInstance

Jurisdiktionsgebundene Instanz mit lokalen Kontakten und expliziten Overrides.

### ResolvedProcedure

Deterministisch aus Type + Instance abgeleitete vollständige Fassung.

Merge v1:
- primitive Werte: replace;
- Objekte: deep merge;
- Listen: full replacement.

Identitätsfelder dürfen nicht durch Instance-Overrides überschrieben werden.

### LifeEvent

Orchestriert mehrere Procedures. Persönliche Routing-Fakten sind nur als Fragen/Definitionen Teil des öffentlichen Katalogs; konkrete Antworten bleiben runtime-only.

### ExecutionStep

Quellengebundene Ableitung eines auszuführenden Schritts. Action completion und Authority outcome verification sind getrennt.

### StepCardView

Reine Präsentationsprojektion eines ExecutionStep; keine eigene Source of Truth.

### SourceSnapshot

Bindet einen Source-Inhalt über SHA-256 und Capture-Metadaten. Source-Material wird nicht ausgeführt.

### SourceRevalidationEvent

Dokumentiert, ob sich ein Source-Snapshot geändert hat und welche gebundenen Felder dadurch revalidiert werden müssen.

### ValidationEvidence

Bindet Subject-Hash, Validatorreport-Hash, Validatorversion, SourceSnapshot-Referenzen und optional eine unabhängige Zweitprüfung.

## Status

`verification_status` und `freshness_status` bleiben orthogonal.

Eine authentische Quelle kann veraltet sein. Ein neuer Hash beweist eine Änderung des Inhalts, aber nicht automatisch eine Änderung seiner rechtlichen oder administrativen Bedeutung.

## DataGap

Fehlende oder strittige Information bleibt explizit. `unknown`, `not_applicable` und `disputed` dürfen nicht gleichgesetzt werden.

## Non-goals

Core v1:
- entscheidet keine individuellen Rechtsansprüche;
- speichert keine Personendaten;
- ist kein Fallmanagementsystem;
- führt keine Behördentransaktion aus;
- ersetzt keine offizielle Quelle;
- macht keine LLM-Ausgabe zur Evidenz.
