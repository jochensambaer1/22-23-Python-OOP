class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.bike = None

    def borrow_bike(self, bike):
        if bike.borrow(self):
            self.bike = bike
            return True
        return False

    def return_bike(self, station):
        if self.bike is not None and self.bike.return_to_station(station):
            self.bike = None
            return True
        return False

