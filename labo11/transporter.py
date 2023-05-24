import geojson

class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Transporter(User):
    id = 0
    state = "available"

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.bikes = []
        self.id = Transporter.id
        Transporter.id += 1

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

if __name__ == '__main__':
    # Create a list of Transporter objects
    transporters = []
    for i in range(10):
        transporter = Transporter("John", "Doe")
        transporters.append(transporter)

    # Create a list to store the features
    features = []

    # Loop over each Transporter object and create a feature with its location and state
    for transporter in transporters:
        point = geojson.Point((0, 0))  # Replace with actual coordinates
        properties = {"id": transporter.id, "state": transporter.state}
        feature = geojson.Feature(geometry=point, properties=properties)
        features.append(feature)

    # Create a FeatureCollection with the features
    feature_collection = geojson.FeatureCollection(features)

    # Write the FeatureCollection to a GeoJSON file
    with open("Transporters.geojson", "w") as f:
        geojson.dump(feature_collection, f)
