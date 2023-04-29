#!/usr/bin/python3
"""Instantiate  blueprint"""
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views import app_views
from flask import request, jsonify
from models import storage

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/status', methods=['GET'])
def status():
    """
    returns the status for the staus route
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    retrieves the number of each objects by type
    """
    if request.method == 'GET':
        resp = {}
        classes = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in classes.items():
            resp[value] = storage.count(key)
        return jsonify(resp)
