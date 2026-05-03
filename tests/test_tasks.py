from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "description": "Created during test"
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Test task"
    assert data["description"] == "Created during test"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_by_id():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task for get by id",
            "description": "Test description"
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Task for get by id"


def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old title",
            "description": "Old description"
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated title",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Updated title"
    assert data["completed"] is True


def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Task to delete",
            "description": "Delete test"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_get_missing_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"