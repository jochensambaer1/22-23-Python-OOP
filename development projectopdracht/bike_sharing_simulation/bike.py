class Bike:
    def __init__(self, id, state):
        self.id = id
        self.state = state
        self.user = None
        self.station = None

    def borrow(self, user):
        # Bike can only be borrowed if it's available
        if self.state == "available":
            self.state = "borrowed"
            self.user = user
            return True
        return False

    def return_to_station(self, station):
        # Bike can only be returned if it's borrowed and the station has room for it
        if self.state == "borrowed" and station.add_bike(self):
            self.state = "available"
            self.user = None
            self.station = station
            return True
        return False