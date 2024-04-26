import random
class Ride:
    def __init__(self, id, driver, origin, destination, time, date, seats):
        self.id = id
        self.driver = driver
        self.origin = origin
        self.destination = destination
        self.time = time
        self.date = date
        self.seats = seats
        self.ride_requests = []

    def request_ride(self, ride_request):
        if len(self.requests) < self.seats:
            self.requests.append(ride_request)

    def as_dict(self):
        return dict (
            id = self.id,
            driver = self.driver,
            origin = self.origin,
            destination = self.destination,
            time = self.time,
            date = self.date,
            seats = self.seats,
            ride_requests = self.ride_requests
        )


class RideRequest:
    def __init__(self, name):
        self.name = name

    def as_dict(self):
        return dict (
            name = self.name
        )