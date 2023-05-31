from flask import Blueprint, request
from db import factory, Todo

todo = Blueprint("todo", __name__, url_prefix="/todo/")


@todo.route("/add/")
def todo_add():
    name = request.values.get("name")

    with factory() as session:
        session.add(Todo(aufgabe=name))
        session.commit()

    return "Aufgabe hinzugefügt"


@todo.route("/set_fortschritt/")
def todo_set_fortschritt():
    todo_id = request.values.get("id")
    fortschritt = request.values.get("fortschritt")

    with factory() as session:
        todo_objekt = session.query(Todo).filter_by(id=todo_id).first()
        todo_objekt.fortschritt = fortschritt
        session.commit()

    return "Fortschritt verändert"


@todo.route("/aufgabe_beenden/")
def todo_aufgabe_beenden():
    todo_id = request.values.get("id")

    with factory() as session:
        todo_objekt = session.query(Todo).filter_by(id=todo_id).first()
        todo_objekt.fertig = True
        session.commit()

    return "Aufgabe beendet"


@todo.route("/aufgabe_fortsetzen/")
def todo_aufgabe_fortsetzen():
    todo_id = request.values.get("id")

    with factory() as session:
        todo_objekt = session.query(Todo).filter_by(id=todo_id).first()
        todo_objekt.fertig = False
        session.commit()

    return "Aufgabe neu gestartet"


@todo.route("/uebersicht/")
def todo_uebersicht_anzeigen():
    with factory() as session:
        if "nur_fertige" in request.values.keys():
            todo_objekte = session.query(Todo).filter_by(fertig=1).all()
        else:
            todo_objekte = session.query(Todo).all()

    ausgabe = []

    for todo in todo_objekte:
        ausgabe.append({"aufgabe": todo.aufgabe, "fortschritt": todo.fortschritt})

    return ausgabe
