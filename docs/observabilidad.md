# Observabilidad

## Estado

Implementado parcialmente.

El proyecto incluye observabilidad basica en la aplicacion Flask y servicios de monitoreo con Prometheus y Grafana.

## Health check

La API expone el endpoint:

```http
GET /health
```

Este endpoint valida que la aplicacion pueda responder y que la base de datos SQLite este accesible.

Respuestas esperadas:

- `200`: servicio y base de datos disponibles.
- `503`: error al acceder a la base de datos.

## Metricas

La API expone metricas para Prometheus en:

```http
GET /metrics
```

Metricas principales:

- `http_requests_total`: total de requests HTTP por metodo, endpoint y estado.
- `http_request_duration_seconds`: duracion de requests HTTP por metodo y endpoint.

## Logs estructurados

La aplicacion usa logs en formato JSON mediante `python-json-logger`.

Por cada request se registra informacion como:

- Metodo HTTP.
- Ruta.
- Codigo de respuesta.
- Duracion en milisegundos.

## Prometheus

La configuracion esta en:

- `prometheus/prometheus.yml`

Prometheus esta configurado para consultar la API en:

```text
api:5000
```

## Grafana

Grafana se levanta desde `docker-compose.yml`.

El proyecto incluye:

- Datasource de Prometheus en `grafana/provisioning/datasources/prometheus.yml`.
- Dashboard en `grafana/provisioning/dashboards/todo-api.json`.

El dashboard muestra:

- Requests por segundo.
- Latencia p50 y p99.
- Errores 4xx y 5xx.
- Total de requests acumulados.

## Ejecucion local

Para levantar API, Prometheus y Grafana:

```bash
docker compose up --build
```

Servicios esperados:

- API: `http://localhost:5000`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

## Pendiente

- Agregar alertas en Prometheus o Grafana.
- Definir objetivos SLI/SLO.
- Agregar trazabilidad distribuida si el sistema crece a mas servicios.
