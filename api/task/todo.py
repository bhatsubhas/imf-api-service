from flask import jsonify
from . import task_api

todos = [
    {
        "task": "Sample task",
        "is_pending": "Yes"
    },
    {
        "task": "Another sample task",
        "is_pending": "No"
    }
]


@task_api.route("/todo")
def get_all():
    return jsonify({"todos": todos}), 200


@task_api.route("/todo/<int:id>")
def get_one_todo(id):
    try:
        if id <= 0:
            raise IndexError
        todo = todos[id - 1]
    except IndexError:
        return {
            "error": f"Could not find todo with id - {id}"
        }, 404
    return jsonify(todo), 200


@task_api.route("/todo/<int:id>", methods=["DELETE"])
def delete_one_todo(id):
    try:
        if id <= 0:
            raise IndexError
        todo = todos.pop(id - 1)
        if todo:
            return jsonify(
                {
                    "message": f"Todo with id - {id} deleted"
                }
            ), 200
    except IndexError:
        return {
            "error": f"Could not find todo with id - {id}"
        }, 404
