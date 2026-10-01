# SPDX-License-Identifier: CC0-1.0
from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from validator.core import SCHEMAS, deep_merge, resolve_pair, validate

ROOT = Path(__file__).resolve().parents[1]


def load(name: str) -> dict:
    return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))


class CoreContractTests(unittest.TestCase):
    def test_all_public_schemas_are_meta_valid_and_cc0_marked(self):
        ids = []
        for name, schema in SCHEMAS.items():
            Draft202012Validator.check_schema(schema)
            self.assertEqual(schema.get("$comment"), "SPDX-License-Identifier: CC0-1.0", name)
            ids.append(schema["$id"])
        self.assertEqual(len(ids), len(set(ids)))

    def test_synthetic_type_instance_and_resolved_examples_validate(self):
        typ = load("adresswechsel-melden.typ.json")
        instance = load("adresswechsel-melden.instanz.json")
        expected = load("adresswechsel-melden.resolved.json")
        self.assertEqual(validate("verfahren-typ", typ), [])
        self.assertEqual(validate("verfahren-instanz", instance), [])
        resolved = resolve_pair(typ, instance)
        self.assertEqual(validate("resolved-verfahren", resolved), [])
        self.assertEqual(resolved, expected)

    def test_merge_contract_is_deep_objects_and_full_list_replacement(self):
        result = deep_merge(
            {"object": {"a": 1, "b": 2}, "list": ["base-a", "base-b"], "primitive": 1},
            {"object": {"b": 3, "c": 4}, "list": ["local"], "primitive": 2},
        )
        self.assertEqual(result["object"], {"a": 1, "b": 3, "c": 4})
        self.assertEqual(result["list"], ["local"])
        self.assertEqual(result["primitive"], 2)

    def test_life_event_profile_accepts_synthetic_route(self):
        item = {
            "schema_version": "1.0.0",
            "life_event_id": "umzug-demo",
            "event_kind": "move",
            "titel": {"formal": "Synthetischer Umzug als LifeEvent"},
            "zweck": "Dieses vollständig synthetische Beispiel demonstriert die Orchestrierung eines Verwaltungsverfahrens.",
            "jurisdiction": "CH-LU",
            "routing_facts": [],
            "procedure_routes": [{
                "route_id": "wohnadresse",
                "procedure_id": "adresswechsel-melden",
                "instance_id": "adresswechsel-melden:lu",
                "applicability": {"mode": "always"},
                "depends_on": [],
                "source_refs": ["src-demo"],
                "reason": "Die Adressmeldung ist in diesem synthetischen Beispiel immer Teil des Umzugs.",
            }],
            "verification_status": "not_reviewed",
            "freshness_status": "not_assessed",
        }
        self.assertEqual(validate("life-event", item), [])

    def test_execution_and_view_profiles_validate_synthetic_projection(self):
        step = {
            "schema_version": "1.0.0",
            "execution_step_id": "exec:adresswechsel-melden:lu:adresse",
            "procedure_id": "adresswechsel-melden",
            "instance_id": "adresswechsel-melden:lu",
            "source_step_id": "adresse-online-melden",
            "order": 1,
            "goal": "Neue Adresse online melden",
            "action": "Öffnen Sie den synthetischen Meldeweg und übermitteln Sie dort die neue Wohnadresse.",
            "urgency": "mittel",
            "channels": ["online"],
            "outcome_verification": {
                "status": "not_modelled",
                "reason": "Das synthetische Beispiel modelliert keine behördliche Ergebnisbestätigung.",
            },
            "source_refs": ["src-demo"],
            "verification_status": "not_reviewed",
            "freshness_status": "not_assessed",
            "expected_evidence": {"status": "not_modelled", "requirements": []},
            "success_states": [{
                "state": "action_performed",
                "scope": "action_performed",
                "method": "user_attestation",
                "prompt": "Haben Sie die synthetische Adressmeldung ausgeführt?",
                "expected": True,
            }],
            "failure_routes": {"status": "not_modelled", "routes": []},
        }
        card = {
            "schema_version": "1.0.0",
            "card_id": step["execution_step_id"],
            "goal": step["goal"],
            "action": step["action"],
            "check": {
                "scope": "action_performed",
                "prompt": step["success_states"][0]["prompt"],
            },
            "fallback": {"status": "not_modelled", "items": []},
            "evidence": step["expected_evidence"],
            "source": {
                "refs": ["src-demo"],
                "verification_status": "not_reviewed",
                "freshness_status": "not_assessed",
            },
            "urgency": "mittel",
            "channels": ["online"],
            "outcome_verification_status": "not_modelled",
        }
        self.assertEqual(validate("execution-step", step), [])
        self.assertEqual(validate("step-card-view", card), [])

    def test_trust_profiles_validate_synthetic_evidence_chain(self):
        old_hash = "sha256:" + "a" * 64
        new_hash = "sha256:" + "b" * 64
        old_id = "snap:" + "a" * 64
        new_id = "snap:" + "b" * 64

        snapshot = {
            "schema_version": "1.0.0",
            "snapshot_id": new_id,
            "source_id": "src-demo",
            "captured_at": "2026-10-01T12:00:00Z",
            "content_hash": new_hash,
            "byte_length": 12,
            "storage_ref": "file:///synthetic/source.bin",
            "previous_snapshot_id": old_id,
            "source_material_executed": False,
            "extensions": {},
        }
        event = {
            "schema_version": "1.0.0",
            "event_id": "reval:" + "c" * 64,
            "source_id": "src-demo",
            "previous_snapshot_id": old_id,
            "current_snapshot_id": new_id,
            "observed_at": "2026-10-01T12:01:00Z",
            "status": "changed",
            "affected_fields": ["/naechster_schritt"],
            "requires_revalidation": True,
            "previous_hash": old_hash,
            "current_hash": new_hash,
        }
        evidence = {
            "schema_version": "1.0.0",
            "evidence_id": "ve:" + "d" * 64,
            "subject_profile": "resolved-verfahren",
            "subject_id": "adresswechsel-melden:lu",
            "validated_at": "2026-10-01T12:02:00Z",
            "validator_version": "1.0.0",
            "input_hash": "sha256:" + "e" * 64,
            "report_hash": "sha256:" + "f" * 64,
            "outcome": "review",
            "source_snapshot_refs": [new_id],
            "review_state": "single_check",
            "extensions": {},
        }
        self.assertEqual(validate("source-snapshot", snapshot), [])
        self.assertEqual(validate("source-revalidation-event", event), [])
        self.assertEqual(validate("validation-evidence", evidence), [])

    def test_examples_are_explicitly_synthetic(self):
        typ = load("adresswechsel-melden.typ.json")
        self.assertEqual(typ["extensions"]["fixture_kind"], "synthetic_genericity_example")
        self.assertIn("placeholder", typ["extensions"]["warning"].lower())
        for source in typ["source_records"]:
            self.assertTrue(source["url"].startswith("https://example.org/"))

    def test_luzern_reference_proof_is_digest_only(self):
        proof = json.loads((ROOT / "reference" / "luzern-proof.json").read_text(encoding="utf-8"))
        self.assertFalse(proof["contains_personal_data"])
        self.assertFalse(proof["contains_official_source_text"])
        self.assertEqual(proof["assertion_scope"], "engineering_reproducibility_only")
        self.assertEqual(proof["workbench"]["regression_tests"], {"passed": 89, "failed": 0})
        self.assertEqual(proof["workbench"]["routed_procedures"], 7)
        self.assertEqual(proof["citizen_surface"]["execution_steps"], 7)
        self.assertRegex(proof["workbench"]["life_event_sha256"], r"^[a-f0-9]{64}$")
        self.assertRegex(proof["citizen_surface"]["bundle_sha256"], r"^[a-f0-9]{64}$")


if __name__ == "__main__":
    unittest.main()
