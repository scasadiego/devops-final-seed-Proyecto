def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "To-Do API"
    assert "version" in data
    assert "endpoints" in data


def test_list_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    payload = {"title": "Comprar leche", "description": "Entera, 2 litros"}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Comprar leche"
    assert data["description"] == "Entera, 2 litros"
    assert data["completed"] == 0
    assert "id" in data


def test_create_task_missing_title(client):
    response = client.post("/tasks", json={"description": "Sin título"})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_create_task_no_body(client):
    response = client.post("/tasks", content_type="application/json", data="")
    assert response.status_code == 400


def test_get_task(client):
    created = client.post("/tasks", json={"title": "Leer libro"}).get_json()
    task_id = created["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == task_id
    assert data["title"] == "Leer libro"


def test_get_task_not_found(client):
    response = client.get("/tasks/9999")
    assert response.status_code == 404
    assert "error" in response.get_json()


def test_update_task(client):
    created = client.post("/tasks", json={"title": "Estudiar"}).get_json()
    task_id = created["id"]

    response = client.put(f"/tasks/{task_id}", json={"completed": 1, "title": "Estudiar DevOps"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["completed"] == 1
    assert data["title"] == "Estudiar DevOps"


def test_update_task_not_found(client):
    response = client.put("/tasks/9999", json={"title": "X"})
    assert response.status_code == 404


def test_delete_task(client):
    created = client.post("/tasks", json={"title": "Borrar esto"}).get_json()
    task_id = created["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert "message" in response.get_json()

    # Verificar que ya no existe
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_delete_task_not_found(client):
    response = client.delete("/tasks/9999")
    assert response.status_code == 404


def test_list_tasks_multiple(client):
    client.post("/tasks", json={"title": "Tarea A"})
    client.post("/tasks", json={"title": "Tarea B"})
    client.post("/tasks", json={"title": "Tarea C"})

    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.get_json()
    assert len(tasks) == 3
