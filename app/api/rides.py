import pickle, json
from flask import jsonify, request
from . import api

from .models import Ride, RideRequest

rides = []

@api.route("/rides", methods=["POST", "GET"])
def create_ride():

    if request.method == "POST":

        ride = request.json

        new_id = len(rides) + 1

        new_ride = Ride(new_id, ride['driver'], ride['origin'], ride['destination'], ride['time'], ride['date'], ride['seats'])

        rides.append(new_ride.as_dict())

        response = { "data" : "success", "ride" : new_ride.as_dict() }

        return jsonify(response)

    return jsonify(rides)

@api.route("/rides/<int:id>")
def get_ride(id):
    for ride in rides:
        if ride['id'] == id:
            return jsonify(ride)

    response = {"data" : "error"}

    return jsonify(response)

@api.route("/rides/<int:id>/request/<name>")
def request_ride(id, name):
    for ride in rides:
        if ride['id'] == id:
            ride_to_request = ride

    print(ride_to_request)

    # if ride_to_request:
    #     Request = RideRequest(name)
    #     print()

    