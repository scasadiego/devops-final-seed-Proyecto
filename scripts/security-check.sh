#!/usr/bin/env bash
set -euo pipefail

echo "=== Linting (ruff) ==="
ruff check src/ tests/
echo "OK"

echo ""
echo "=== Formato (ruff format) ==="
ruff format --check src/ tests/
echo "OK"

echo ""
echo "=== Auditoría de dependencias (pip-audit) ==="
pip-audit -r requirements.txt
echo "OK"

echo ""
echo "Todas las verificaciones de seguridad pasaron."
