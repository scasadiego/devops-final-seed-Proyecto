# Pipeline CI/CD

## Estado

Implementado parcialmente.

El proyecto incluye un workflow de GitHub Actions en:

- `.github/workflows/ci-cd.yml`

## Que hace actualmente

El pipeline se ejecuta en eventos `push` y `pull_request` hacia la rama `main`.

Incluye las siguientes etapas:

1. Descargar el repositorio con `actions/checkout`.
2. Configurar Python 3.11 con `actions/setup-python`.
3. Instalar dependencias de desarrollo desde `dev-requirements.txt`.
4. Ejecutar linting con Ruff:

   ```bash
   ruff check src/ tests/
   ```

5. Verificar formato con Ruff:

   ```bash
   ruff format --check src/ tests/
   ```

6. Ejecutar pruebas automatizadas con Pytest:

   ```bash
   pytest --junitxml=reports/tests.xml
   ```

7. Ejecutar auditoria de dependencias con `pip-audit`:

   ```bash
   pip-audit -r requirements.txt -f json -o reports/pip-audit.json
   ```

8. Subir reportes como artefactos de GitHub Actions.
9. Construir la imagen Docker:

   ```bash
   docker build -t todo-api:${{ github.sha }} .
   ```

## Artefactos generados

El pipeline genera y publica como artefactos:

- `reports/tests.xml`
- `reports/pip-audit.json`

## Pendiente

- Publicar la imagen Docker en un registry como Docker Hub o GitHub Container Registry.
- Definir versionamiento semantico de imagen, por ejemplo `v1.0.0`.
- Agregar reporte de cobertura de pruebas.
- Agregar despliegue automatico a un ambiente real.
