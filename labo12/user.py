
import json
from datetime import datetime

import geojson


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif callable(obj):
            return None
        else:
            return super().default(obj)
class user:
    def __init__(self, name, surname,home_station, werk_station):
        self.name = name
        self.surname = surname
        self.bike = None
        self.home_station = id
        self.werk_station = id

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

# Create a list to store the features
Users = [
    user("hn", "Doe", "Station A", "Station B"),
    user("ne", "Doe", "Station A", "Station B"),
    user("b", "Smith", "Station C", "Station D"),
    user("ice", "Jones", "Station E", "Station F"),
    user("hn", "Doe", "Station A", "Station B"),
    user("ne", "Doe", "Station A", "Station B"),
    user("b", "Smith", "Station C", "Station D"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("ice", "Jones", "Station E", "Station F"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("arlie", "Brown", "Station G", "Station H"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
    user("e", "Johnson", "Station I", "Station J"),
]


def get_station_coords(station):
    # Replace with code that retrieves the coordinates of a station based on its name or ID
    if station == "Station A":
        return (-115.81, 37.24)
    elif station == "Station B":
        return (-115.82, 37.25)
    elif station == "Station C":
        return (-115.83, 37.26)
    elif station == "Station D":
        return (-115.84, 37.27)
    elif station == "Station E":
        return (-115.85, 37.28)
    elif station == "Station F":
        return (-115.86, 37.29)
    elif station == "Station G":
        return (-115.87, 37.30)
    elif station == "Station H":
        return (-115.88, 37.31)
    elif station == "Station I":
        return (-115.89, 37.32)
    elif station == "Station J":
        return (-115.90, 37.33)
    else:
        return None

features = []

# Loop over each bike object and create a feature with its location and state
# Loop over each user object and create a feature with its location and properties
for user in Users:
    properties = {"name": user.name, "surname": user.surname, "home_station": user.home_station, "werk_station": user.werk_station}
    home_station_coords = get_station_coords(user.home_station)  # Replace with function that gets coordinates of a station
    werk_station_coords = get_station_coords(user.werk_station)  # Replace with function that gets coordinates of a station
    home_station_point = geojson.Point(home_station_coords)
    werk_station_point = geojson.Point(werk_station_coords)
    home_station_feature = geojson.Feature(geometry=home_station_point, properties=properties)
    werk_station_feature = geojson.Feature(geometry=werk_station_point, properties=properties)
    features.append(home_station_feature)
    features.append(werk_station_feature)




# Create a FeatureCollection with the features
feature_collection = geojson.FeatureCollection(features)

# Write the FeatureCollection to a GeoJSON file
# Write the FeatureCollection to a GeoJSON file using the CustomEncoder
with open("users.geojson", "w") as f:
    json.dump(feature_collection, f, cls=CustomEncoder)
