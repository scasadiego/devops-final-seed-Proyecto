# Seguridad

## Herramientas

El proyecto usa dos herramientas para verificar seguridad del código y las dependencias:

| Herramienta | Propósito |
|-------------|-----------|
| `ruff` | Linting y análisis estático del código Python |
| `pip-audit` | Auditoría de dependencias contra bases de datos de CVEs |

Ambas están declaradas en `dev-requirements.txt` y se ejecutan en el pipeline CI/CD.

## Linting con ruff

La configuración está en `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "UP"]
ignore = ["E501"]
```

Reglas activas:

- `E` / `W`: errores y advertencias de estilo (pycodestyle)
- `F`: detección de bugs comunes (pyflakes): variables no usadas, imports no usados
- `I`: orden de imports (isort)
- `B`: detección de patrones problemáticos (flake8-bugbear)
- `UP`: sugerencias de sintaxis moderna (pyupgrade)

Verificar linting:

```bash
ruff check src/ tests/
```

Verificar formato:

```bash
ruff format --check src/ tests/
```

## Auditoría de dependencias con pip-audit

Escanea las dependencias declaradas en `requirements.txt` contra la base de datos de vulnerabilidades de PyPI (OSV).

```bash
pip-audit -r requirements.txt
```

Durante el desarrollo se detectaron y corrigieron dos CVEs:

| Paquete | Versión vulnerable | CVE | Versión corregida |
|---------|--------------------|-----|-------------------|
| flask | 3.0.0 | CVE-2026-27205 | 3.1.3 |
| pytest | 8.3.5 | CVE-2025-71176 | 9.0.3 |

Ambas dependencias fueron actualizadas antes de commitear.

## Script de verificación

El archivo `scripts/security-check.sh` ejecuta todas las verificaciones en un solo paso:

```bash
bash scripts/security-check.sh
```

Pasos que ejecuta:

1. `ruff check src/ tests/` — linting
2. `ruff format --check src/ tests/` — verificación de formato
3. `pip-audit -r requirements.txt` — auditoría de dependencias

## Integración en CI/CD

El pipeline en `.github/workflows/ci-cd.yml` ejecuta linting y auditoría como etapas obligatorias. Si alguna falla, el pipeline se detiene y el merge no puede proceder.

## Dependencias de desarrollo

```
ruff==0.11.12
pip-audit==2.9.0
```

Declaradas en `dev-requirements.txt`.
