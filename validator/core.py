# SPDX-License-Identifier: CC0-1.0
from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema" / "v1"

PROFILE_FILES = {
    "verfahren-typ": "verfahren-typ.schema.json",
    "verfahren-instanz": "verfahren-instanz.schema.json",
    "resolved-verfahren": "resolved-verfahren.schema.json",
    "life-event": "life-event.schema.json",
    "execution-step": "execution-step.schema.json",
    "step-card-view": "step-card-view.schema.json",
    "source-snapshot": "source-snapshot.schema.json",
    "source-revalidation-event": "source-revalidation-event.schema.json",
    "validation-evidence": "validation-evidence.schema.json",
}

SCHEMAS = {
    name: json.loads((SCHEMA_DIR / filename).read_text(encoding="utf-8"))
    for name, filename in PROFILE_FILES.items()
}

FORMAT_CHECKER = FormatChecker()
URI_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


@FORMAT_CHECKER.checks("date-time")
def _date_time(value: object) -> bool:
    if not isinstance(value, str):
        return True
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return "T" in value.upper() and parsed.tzinfo is not None and parsed.utcoffset() is not None


@FORMAT_CHECKER.checks("uri")
def _uri(value: object) -> bool:
    if not isinstance(value, str):
        return True
    if not value or any(ch.isspace() for ch in value) or not URI_SCHEME.match(value):
        return False
    from urllib.parse import urlsplit
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    return not (parsed.scheme in {"http", "https"} and not parsed.netloc)


@FORMAT_CHECKER.checks("uri-reference")
def _uri_reference(value: object) -> bool:
    if not isinstance(value, str):
        return True
    if not value or any(ch.isspace() for ch in value):
        return False
    from urllib.parse import urlsplit
    try:
        urlsplit(value)
    except ValueError:
        return False
    return True


REGISTRY = Registry().with_resources(
    (schema["$id"], Resource.from_contents(schema))
    for schema in SCHEMAS.values()
)

VALIDATORS = {
    name: Draft202012Validator(
        schema,
        registry=REGISTRY,
        format_checker=FORMAT_CHECKER,
    )
    for name, schema in SCHEMAS.items()
}

PROTECTED_OVERRIDE_FIELDS = {
    "schema_version",
    "verfahren_id",
    "verfahrensklasse",
    "basis_verfahren",
    "instanz_id",
    "zustaendigkeitsgebiet",
    "version",
    "gueltig_ab",
    "gueltig_bis",
    "kontaktstellen",
}


def validate(profile: str, data: dict[str, Any]) -> list[dict[str, str]]:
    if profile not in VALIDATORS:
        raise KeyError(f"unknown profile: {profile}")
    errors = sorted(
        VALIDATORS[profile].iter_errors(data),
        key=lambda error: list(error.absolute_path),
    )
    return [
        {
            "path": "/" + "/".join(str(part) for part in error.absolute_path)
            if error.absolute_path else "",
            "message": error.message,
        }
        for error in errors
    ]


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        elif isinstance(value, list):
            result[key] = deepcopy(value)
        else:
            result[key] = deepcopy(value)
    return result


def resolve_pair(type_record: dict[str, Any], instance_record: dict[str, Any]) -> dict[str, Any]:
    type_errors = validate("verfahren-typ", type_record)
    instance_errors = validate("verfahren-instanz", instance_record)
    if type_errors or instance_errors:
        raise ValueError({"type_errors": type_errors, "instance_errors": instance_errors})

    type_id = type_record["verfahren_id"]
    if instance_record["basis_verfahren"] != type_id:
        raise ValueError("basis_verfahren does not match verfahren_id")

    overrides = instance_record.get("overrides", {})
    forbidden = sorted(set(overrides) & PROTECTED_OVERRIDE_FIELDS)
    if forbidden:
        raise ValueError(f"protected override fields: {', '.join(forbidden)}")

    resolved = deepcopy(type_record)
    resolved.update({
        "basis_verfahren": type_id,
        "instanz_id": instance_record["instanz_id"],
        "zustaendigkeitsgebiet": instance_record["zustaendigkeitsgebiet"],
        "version": instance_record["version"],
        "gueltig_ab": instance_record["gueltig_ab"],
        "gueltig_bis": instance_record.get("gueltig_bis"),
        "kontaktstellen": deepcopy(instance_record["kontaktstellen"]),
    })
    resolved = deep_merge(resolved, deepcopy(overrides))

    errors = validate("resolved-verfahren", resolved)
    if errors:
        raise ValueError({"resolved_errors": errors})
    return resolved
