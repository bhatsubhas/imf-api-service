from . import client

URL_PREFIX = "/api/v1/task"


def test_get_all_todos(client):
    """
    Check if endpoint to get all the todos.
    """
    resp = client.get(f"{URL_PREFIX}/todo")
    assert 200 == resp.status_code
    json_data = resp.get_json()
    assert isinstance(json_data["todos"], list)


def test_get_single_todo(client):
    """
    Check if endpoint to get a single todo
    """
    resp = client.get(f"{URL_PREFIX}/todo/1")
    assert 200 == resp.status_code
    json_data = resp.get_json()
    assert len(json_data["task"]) != 0
    assert len(json_data["is_pending"]) != 0


def test_get_todo_not_found(client):
    """
    To test how service responds when unknown task id is passed.
    """
    id = 4
    resp = client.get(f"{URL_PREFIX}/todo/{id}")
    assert 404 == resp.status_code
    json_data = resp.get_json()
    assert f"Could not find todo with id - {id}" in json_data["error"]


def test_delete_single_todo(client):
    """
    Test delete a todo with task id passed as input.
    """
    id = 1
    resp = client.delete(f"{URL_PREFIX}/todo/{id}")
    assert 200 == resp.status_code
    json_data = resp.get_json()
    assert f"Todo with id - {id} deleted" in json_data["message"]


def test_delete_todo_not_found(client):
    """
    To Test how service responds when unknown task id is passed 
    for deletion
    """
    id = 4
    resp = client.delete(f"{URL_PREFIX}/todo/{id}")
    assert 404 == resp.status_code
    json_data = resp.get_json()
    assert f"Could not find todo with id - {id}" in json_data["error"]
