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
    import json
import geojson

# Define a list of Bike objects
bikes = [
    Bike(1, "available"),
    Bike(2, "available"),
    Bike(3, "borrowed"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(4, "available"),
    Bike(5, "borrowed")
]

# Create a list to store the features
features = []

# Loop over each bike object and create a feature with its location and state
for bike in bikes:
    point = geojson.Point((0, 0))  # Replace with actual coordinates
    properties = {"id": bike.id, "state": bike.state}
    feature = geojson.Feature(geometry=point, properties=properties)
    features.append(feature)

# Create a FeatureCollection with the features
feature_collection = geojson.FeatureCollection(features)

# Write the FeatureCollection to a GeoJSON file
with open("bikes.geojson", "w") as f:
    geojson.dump(feature_collection, f)
