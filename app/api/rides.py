import pickle, json
from flask import jsonify, request
from . import api

from .models import Ride

rides = []

@api.route("/rides", methods=["POST"])
def create_ride():

    ride = request.get_json()

    print(ride)

    new_ride = Ride(ride['driver'], ride['origin'], ride['destination'], ride['time'], ride['date'], ride['seats'])

    rides.append(new_ride)

    response = { "data" : "success", "ride" : json.dumps(new_ride.__dict__) }

    return jsonify(response)

@api.route("/rides")
def get_rides():
    return json.dumps(rides)