#!/usr/bin/python3
"""
starts a Flask api
"""

from flask import Flask, render_template
from models import *
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import request, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)

# flask server environmental setup
host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5000)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    resp = {"error": "Not found"}
    return jsonify(resp)


if __name__ == '__main__':
    app.run(host, port, threaded=True)
