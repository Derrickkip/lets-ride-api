class Ride:
    def __init__(self, driver, origin, destination, time, date, seats):
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