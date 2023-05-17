from flask import Blueprint, request

from db import factory, Todo

todo = Blueprint("todo", __name__, url_prefix="/todo/")

@todo.route("/add/")
def todo_add():
    name = request.values.get("name")
    with factory() as session:
        session.add(Todo(aufgabe=name))
        session.commit()

    return "success"

@todo.route("/set_fortschritt/<todo_id>/<fortschritt>/")
def todo_set_fortschritt(todo_id, fortschritt):
    # todo_id = request.values.get("id")
    # fortschritt = request.values.get("fortschritt")
    with factory() as session:
        todo_objekt = session.query(Todo).filter_by(id=todo_id).first()
        todo_objekt.fortschritt = fortschritt
        session.commit()

    return "success"
