import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title":"nova tarefa",
        "description":"desc nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks",json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    response_json = response.json()
    print(response_json)
    assert response.status_code == 200
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == task_id


def test_update_task():
    if tasks:
        task_id = tasks[0]
        updated_task_data = {
            "title":"tarefa atualizada",
            "description":"desc tarefa atualizada",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}",json=updated_task_data)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["message"] == "Atualizaçao realizada com sucesso"

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["message"] == "Deleçao realizada com sucesso"
        tasks.remove(task_id)
        print(tasks)
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404