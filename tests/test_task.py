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


def test_get_all_pending_todos(client):
    """
    Test if endpoint to get all the pending todos.
    """
    resp = client.get(f"{URL_PREFIX}/todo?is_pending=Yes")
    assert 200 == resp.status_code
    pending_todos = resp.get_json()["todos"]
    assert isinstance(pending_todos, list)
    for todo in pending_todos:
        assert todo["is_pending"] == "Yes"


def test_get_all_completed_todos(client):
    """
    Test if endpoint to get all the pending todos.
    """
    resp = client.get(f"{URL_PREFIX}/todo?is_pending=No")
    assert 200 == resp.status_code
    pending_todos = resp.get_json()["todos"]
    assert isinstance(pending_todos, list)
    for todo in pending_todos:
        assert todo["is_pending"] == "No"


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


def test_get_todo_with_zero_id(client):
    """
    To test how service responds when unknown task id is passed.
    """
    id = 0
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


def test_delete_todo_with_zero_id(client):
    """
    To Test how service responds when unknown task id is passed
    for deletion
    """
    id = 0
    resp = client.delete(f"{URL_PREFIX}/todo/{id}")
    assert 404 == resp.status_code
    json_data = resp.get_json()
    assert f"Could not find todo with id - {id}" in json_data["error"]


def test_create_todo_item(client):
    """
    To test how service responds when new todo item creation is requested.
    """
    resp = client.post(f"{URL_PREFIX}/todo", json={
        "task": "Test sample task",
        "is_pending": "Yes"
    })
    assert 201 == resp.status_code
    json_data = resp.get_json()
    assert "Successfully created the todo" in json_data["message"]


def test_create_no_data(client):
    """
    To test how service responds when no data is provided
    for todo item creation.
    """
    resp = client.post(f"{URL_PREFIX}/todo", json={})
    assert 400 == resp.status_code
    json_data = resp.get_json()
    assert "Incorrect input format" in json_data["error"]


def test_create_using_non_json_data(client):
    """
    To test how service responds when no data is provided
    for todo item creation.
    """
    resp = client.post(f"{URL_PREFIX}/todo", data="test")
    assert 415 == resp.status_code
    json_data = resp.get_json()
    assert "Unsupported Media Type" in json_data["Error"]


def test_create_invalid_data(client):
    """
    To test how service responds when invalid data is provided
    for todo item creation.
    """
    resp = client.post(f"{URL_PREFIX}/todo", json={
        "item": "Test sample task",
        "is_pending": "Yes"
    })
    assert 400 == resp.status_code
    json_data = resp.get_json()
    assert "Incorrect input format" in json_data["error"]


def test_create_invalid_pending_status(client):
    """
    To test how service responds when incorrect is_pending status
    is provided for todo item creation.
    """
    resp = client.post(f"{URL_PREFIX}/todo", json={
        "task": "Test sample task",
        "is_pending": "True"
    })
    assert 400 == resp.status_code
    json_data = resp.get_json()
    assert "Incorrect input format" in json_data["error"]
