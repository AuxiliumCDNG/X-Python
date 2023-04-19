import time

from flask import Flask, render_template, request

app = Flask(__name__)


data = {
    "text": "X-Python",
    "backgroundColor": "red",
    "textColor": "white"
}

@app.route("/api/text/get/")
def api_text_get():
    if request.values.get("long_poll", "true") == "false":
        return data

    old_data = data.copy()
    for i in range(30):
        if old_data != data:
            return data
        time.sleep(1)

    return data

@app.route("/api/text/change")
def test():
    data.update(request.values)
    return "lol"

@app.route("/anzeige/")
def anzeige():
    return render_template("anzeige.html")


app.run(host="0.0.0.0", port=80)
