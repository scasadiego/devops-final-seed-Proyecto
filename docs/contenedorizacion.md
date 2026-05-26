# Contenedorización

## Archivos

```
Dockerfile
docker-compose.yml
prometheus/
└── prometheus.yml
grafana/
└── provisioning/
    ├── datasources/
    │   └── prometheus.yml
    └── dashboards/
        ├── dashboard.yml
        └── todo-api.json
```

## Dockerfile

Imagen basada en `python:3.11-slim`.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

ENV DB_PATH=/data/tasks.db
ENV PORT=5000

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

CMD ["python", "src/app.py"]
```

Decisiones de diseño:

- La base de datos SQLite se escribe en `/data`, que se monta como volumen para persistencia.
- El puerto es configurable mediante la variable de entorno `PORT`.
- El `HEALTHCHECK` usa el endpoint `/health` de la propia API para que Docker detecte si el contenedor está sano.

## docker-compose.yml

Levanta tres servicios:

### api

La aplicación Flask construida desde el `Dockerfile`.

- Puerto: `5000`
- Volumen: `db_data` montado en `/data` para persistir `tasks.db`

### prometheus

Imagen oficial `prom/prometheus:v3.4.0`.

- Puerto: `9090`
- Configuración en `prometheus/prometheus.yml`
- Raspa el endpoint `/metrics` de `api:5000` cada 15 segundos
- Datos persistidos en el volumen `prometheus_data`

### grafana

Imagen oficial `grafana/grafana:12.0.1`.

- Puerto: `3000`
- Credenciales: `admin` / `admin`
- Datasource y dashboard pre-configurados mediante provisioning en `grafana/provisioning/`
- Datos persistidos en el volumen `grafana_data`

## Variables de entorno

| Variable | Servicio | Valor por defecto | Descripción |
|----------|----------|-------------------|-------------|
| `DB_PATH` | api | `/data/tasks.db` | Ruta del archivo SQLite |
| `PORT` | api | `5000` | Puerto de escucha de Flask |
| `GF_SECURITY_ADMIN_PASSWORD` | grafana | `admin` | Contraseña del usuario admin |

## Comandos útiles

Construir y levantar todos los servicios:

```bash
docker compose up --build
```

Ver logs de la API:

```bash
docker compose logs api
```

Detener y eliminar contenedores:

```bash
docker compose down
```

Eliminar también los volúmenes de datos:

```bash
docker compose down -v
```

Construir solo la imagen sin levantar servicios:

```bash
docker build -t todo-api:latest .
```
