# SPDX-License-Identifier: CC0-1.0
"""Compatibility entry point for the OSM-CH public core validator.

Use validator/validate.py for new integrations.
"""

from validate import main

if __name__ == "__main__":
    raise SystemExit(main())
