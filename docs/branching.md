# Estrategia de Branching

## Estado

Pendiente de formalizar.

Actualmente el repositorio trabaja sobre la rama principal:

- `main`

El pipeline CI/CD esta configurado para ejecutarse cuando hay `push` o `pull_request` hacia `main`.

## Propuesta de flujo

Para este proyecto se recomienda usar un flujo simple basado en ramas cortas:

1. `main`: rama estable del proyecto.
2. `feature/<nombre>`: ramas para nuevas funcionalidades o cambios.
3. `fix/<nombre>`: ramas para correcciones.
4. `docs/<nombre>`: ramas para documentacion.

## Reglas sugeridas

- No trabajar directamente sobre `main` salvo cambios pequenos o de configuracion controlada.
- Crear un Pull Request para integrar cambios a `main`.
- Ejecutar el pipeline antes de aprobar una integracion.
- Mantener commits pequenos y descriptivos.

## Convencion de commits sugerida

Ejemplos:

```text
feat: add health endpoint
fix: correct task update validation
docs: add observability documentation
ci: add GitHub Actions workflow
test: add task deletion tests
```

## Pendiente

- Activar proteccion de rama en GitHub para `main`.
- Exigir que el workflow CI/CD pase antes de permitir merge.
- Definir responsables de revision de Pull Requests.
