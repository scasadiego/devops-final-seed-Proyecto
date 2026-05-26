# CALMS

## Estado

Documentado parcialmente.

CALMS es un marco para evaluar practicas DevOps desde cinco dimensiones:

- Culture
- Automation
- Lean
- Measurement
- Sharing

## Culture

El proyecto promueve colaboracion mediante Git, Pull Requests y una rama principal estable.

Pendiente:

- Definir responsables de revision.
- Documentar acuerdos de equipo.
- Establecer reglas de comunicacion para incidentes y cambios.

## Automation

Existe automatizacion parcial:

- Pipeline CI/CD con GitHub Actions.
- Linting automatico con Ruff.
- Pruebas automaticas con Pytest.
- Auditoria de dependencias con `pip-audit`.
- Build automatico de imagen Docker.

Pendiente:

- Publicacion automatica de imagen Docker.
- Despliegue automatico.
- Proteccion de rama basada en resultados del pipeline.

## Lean

El proyecto mantiene una API pequena y enfocada, con endpoints REST simples para gestion de tareas.

Practicas recomendadas:

- Cambios pequenos.
- Pull Requests cortos.
- Feedback rapido desde el pipeline.

Pendiente:

- Definir criterios de aceptacion por cambio.
- Medir tiempo desde commit hasta validacion.

## Measurement

Existe medicion tecnica basica:

- Endpoint `/health`.
- Endpoint `/metrics`.
- Metricas Prometheus.
- Dashboard Grafana.
- Logs estructurados.

Pendiente:

- Definir SLI/SLO.
- Agregar alertas.
- Medir cobertura de pruebas.
- Registrar metricas del pipeline, como duracion y tasa de fallos.

## Sharing

El proyecto empieza a compartir conocimiento mediante:

- `README.md`
- Carpeta `docs/`
- Configuracion versionada de Docker, Prometheus, Grafana y CI/CD.

Pendiente:

- Agregar guia de contribucion.
- Documentar decisiones tecnicas importantes.
- Documentar pasos de recuperacion ante fallos.
