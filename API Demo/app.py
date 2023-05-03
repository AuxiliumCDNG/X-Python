from flask import Flask
import db
from blueprints.text import text_api

app = Flask(__name__)

app.register_blueprint(text_api)

app.run(host="0.0.0.0", port=80)
