import time

from flask import Blueprint, request, render_template

text_api = Blueprint("text_api", __name__)


data = {
    "text": "X-Python",
    "backgroundColor": "red",
    "textColor": "white"
}

@text_api.route("/api/text/get/")
def api_text_get():
    if request.values.get("long_poll", "false") == "false":
        return data

    old_data = data.copy()
    for i in range(15):
        print("check")
        if old_data != data:
            return data
        time.sleep(2)

    return data

@text_api.route("/api/text/change/")
def test():
    data.update(request.values)
    return "lol"

@text_api.route("/anzeige/")
def anzeige():
    return render_template("anzeige.html")

