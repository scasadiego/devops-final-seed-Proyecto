# Kubernetes

Manifests basicos para desplegar la API To-Do en Kubernetes.

## Recursos

- `namespace.yaml`: namespace `todo-api`.
- `pvc.yaml`: volumen persistente para SQLite.
- `deployment.yaml`: despliegue de la API con probes de salud.
- `service.yaml`: servicio interno tipo `ClusterIP`.
- `kustomization.yaml`: agrupacion de recursos con Kustomize.

## Aplicar manifests

```bash
kubectl apply -k k8s/
```

## Verificar despliegue

```bash
kubectl get all -n todo-api
kubectl get pvc -n todo-api
```

## Probar localmente con port-forward

```bash
kubectl port-forward -n todo-api service/todo-api 5000:5000
```

Luego abrir:

```text
http://localhost:5000/health
```

## Imagen

Por defecto los manifests usan:

```text
todo-api:latest
```

Para usar una imagen versionada:

```bash
kubectl set image deployment/todo-api todo-api=<registry>/todo-api:<tag> -n todo-api
```

## Pendiente

- Publicar la imagen en un registry externo.
- Agregar Ingress si se requiere acceso externo.
- Agregar manifests para Prometheus y Grafana dentro del cluster.
