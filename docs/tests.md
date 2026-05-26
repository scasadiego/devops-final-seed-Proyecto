# Tests Unitarios

## Ubicación

Los tests se encuentran en la carpeta `tests/`:

```
tests/
├── __init__.py
├── conftest.py
└── test_app.py
```

## Framework

Se usa **pytest** como framework de testing. La configuración está en `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

## Fixture de base de datos

El archivo `tests/conftest.py` define un fixture `client` que:

- Crea una base de datos SQLite temporal por cada test (usando `tmp_path` de pytest).
- Inyecta esa ruta en la variable `DB_PATH` del módulo de la app.
- Llama a `init_db()` para crear las tablas en la DB temporal.
- Entrega un cliente de test de Flask (`app.test_client()`).
- Limpia el estado al finalizar cada test.

Esto garantiza aislamiento total entre tests: ningún test comparte estado con otro.

## Casos de prueba

El archivo `tests/test_app.py` contiene 12 tests que cubren todos los endpoints de la API:

| Test | Descripción |
|------|-------------|
| `test_index` | `GET /` retorna nombre, versión y endpoints |
| `test_list_tasks_empty` | `GET /tasks` devuelve lista vacía al inicio |
| `test_create_task` | `POST /tasks` crea una tarea y retorna 201 |
| `test_create_task_missing_title` | `POST /tasks` sin `title` retorna 400 |
| `test_create_task_no_body` | `POST /tasks` sin body retorna 400 |
| `test_get_task` | `GET /tasks/<id>` retorna la tarea correcta |
| `test_get_task_not_found` | `GET /tasks/9999` retorna 404 |
| `test_update_task` | `PUT /tasks/<id>` actualiza campos correctamente |
| `test_update_task_not_found` | `PUT /tasks/9999` retorna 404 |
| `test_delete_task` | `DELETE /tasks/<id>` elimina y confirma con 404 posterior |
| `test_delete_task_not_found` | `DELETE /tasks/9999` retorna 404 |
| `test_list_tasks_multiple` | `GET /tasks` refleja N tareas creadas |

## Ejecución

Con el entorno virtual activo:

```bash
pytest tests/ -v
```

Desde el pipeline CI/CD, los resultados se guardan en formato JUnit:

```bash
pytest --junitxml=reports/tests.xml
```

## Dependencias de desarrollo

```
pytest==9.0.3
```

Declarado en `dev-requirements.txt`.
