from flask import jsonify, request, current_app
from . import task_api
from .service import get_all_todos, get_todo, delete_todo, create_todo


@task_api.get("/todo")
def get_all():
    return jsonify(get_all_todos())


@task_api.get("/todo/<int:tsk_id>")
def get_one(tsk_id):
    todo = get_todo(tsk_id)
    if todo:
        return jsonify(todo)
    return {
        "error": f"Could not find todo with id - {tsk_id}"
    }, 404


@task_api.delete("/todo/<int:tsk_id>")
def delete(tsk_id):
    todo = delete_todo(tsk_id)
    if todo:
        return jsonify(
            {
                "message": f"Todo with id - {tsk_id} deleted"
            }
        )
    return {
        "error": f"Could not find todo with id - {tsk_id}"
    }, 404


@task_api.post("/todo")
def create():
    json_data = request.get_json()
    current_app.logger.debug(f"Request Data: {json_data}")
    if json_data is None:
        return {
            "error": "Missing mandatory fields"
        }, 400
    try:
        create_todo(json_data)
    except (ValueError, KeyError):
        return {
            "error": "Incorrect input format"
        }, 400

    return jsonify(
        {"message": "Successfully created the todo"}
    ), 201
