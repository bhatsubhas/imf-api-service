from flask import jsonify, request, current_app
from . import task_api
from .service import get_all_todos, get_todo, delete_todo, create_todo


@task_api.get("/todo")
def get_all():
    is_pending = request.args.get("is_pending")
    return jsonify(get_all_todos(is_pending))


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
    try:
        tsk_id = create_todo(json_data)
    except (ValueError, KeyError):
        return {
            "error": "Incorrect input format"
        }, 400

    return jsonify(
        {"message": f"Successfully created the todo with id - {tsk_id}"}
    ), 201
