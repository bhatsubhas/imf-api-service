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


def get_all_todos():
    return {"todos": todos}


def get_todo(tsk_id):
    if tsk_id <= 0:
        return None
    try:
        todo = todos[tsk_id - 1]
    except IndexError:
        return None
    return todo


def delete_todo(tsk_id):
    if tsk_id <= 0:
        return None
    try:
        todo = todos.pop(tsk_id - 1)
    except IndexError:
        return None
    return todo


def create_todo(json_data):
    task = json_data["task"]
    is_pending = json_data["is_pending"]
    if is_pending not in ("Yes", "No"):
        raise ValueError
    todos.append({
        "task": task,
        "is_pending": is_pending
    })
