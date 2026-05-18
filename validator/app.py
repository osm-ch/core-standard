# SPDX-License-Identifier: CC0-1.0

import json
import argparse
import sys
from jsonschema import validate, ValidationError

SCHEMA_PATH = "schema/v1/verfahren.schema.json"

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_validation(target_file):
    print(f"OSM-CH Validator 0.1\nTarget: {target_file}\n")
    schema = load_json(SCHEMA_PATH)
    target_data = load_json(target_file)
    
    try:
        validate(instance=target_data, schema=schema)
        print("[PASS] Hard Fail Conditions bestanden. JSON ist strukturell konform.")
        sys.exit(0)
    except ValidationError as e:
        print(f"[FAIL] Hard Fail: {e.message}")
        print(f"Pfad: /{'/'.join([str(x) for x in e.path])}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSM-CH Compliance Validator")
    parser.add_argument("--validate", required=True, help="Pfad zur JSON-Datei")
    args = parser.parse_args()
    run_validation(args.validate)
