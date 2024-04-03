from flask import jsonify
from . import api

@api.route("/")
def hello_world():

    response = { "data" : "Hello World" }
    return jsonify(response)