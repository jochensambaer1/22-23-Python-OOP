class Transporter(User):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.bikes = []

    def collect_bikes(self, station):
        for i in range(station.capacity):
            if station.slots[i] is not None and station.slots[i].state == "available":
                self.bikes.append(station.slots[i])
                station.slots[i] = None

    def distribute_bikes(self, station):
        for i in range(len(self.bikes)):
            if station.add_bike(self.bikes[i]):
                self.bikes[i].station = station
                self.bikes.pop(i)
                i -= 1