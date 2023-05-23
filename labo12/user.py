import json
from datetime import datetime
import geojson
import random
import chardet
import psycopg2
from get_station_coords import get_station_coords


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif callable(obj):
            return None
        else:
            return super().default(obj)


class User:
    def __init__(self, name, surname, home_station, werk_station):
        self.name = name
        self.surname = surname
        self.bike = None
        self.home_station = home_station
        self.werk_station = werk_station

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


# Load stations from stations.geojson file
with open('velo.geojson') as f:
    data = geojson.load(f)

stations = []
for feature in data['features']:
    properties = feature['properties']
    id = properties['OBJECTID']
    name = properties.get('Naam', 'unknown')
    numberOfPlaces = properties.get('Aantal_plaatsen', 0)
    geometry = feature['geometry']
    longitude, latitude = geometry['coordinates']
    stations.append(Station(id, name, longitude, latitude, numberOfPlaces))


features = []

# Loop over each user object and create a feature with its location and properties
for user in Users:
    properties = {"name": user.name, "surname": user.surname, "home_station": user.home_station, "werk_station": user.werk_station}
    try:
        home_station_coords = get_station_coords(user.home_station)
        werk_station_coords = get_station_coords(user.werk_station)
        home_station_point = geojson.Point(home_station_coords)
        werk_station_point = geojson.Point(werk_station_coords)
        home_station_feature = geojson.Feature(geometry=home_station_point, properties=properties)
        werk_station_feature = geojson.Feature(geometry=werk_station_point, properties=properties)
        features.append(home_station_feature)
        features.append(werk_station_feature)
    except Exception as e:
        print(f"Error fetching station coordinates: {e}")


# Create a FeatureCollection with the features
feature_collection = geojson.FeatureCollection(features)

# Write the FeatureCollection to a GeoJSON file using the CustomEncoder
with open("users.geojson", "w") as f:
    json.dump(feature_collection, f, cls=CustomEncoder)


# Use chardet to detect the character encoding of the JSON file
with open('names.json', 'rb') as f:
    result = chardet.detect(f.read())

# Open the JSON file with the detected character encoding
with open('names.json', 'r', encoding=result['encoding']) as f:
    names = json.load(f)

# Create a list of dictionaries to store the generated names
name_list = []

# Generate 1000 names and add them to the list
for i in range(1000):
    # Select two random names from the first_names and last_names fields
    first_name = random.choice(names['first_names'])
    last_name = random.choice(names['last_names'])

    # Combine the names to create a new name
    new_name = f"{first_name} {last_name}"

    # Add the new name to the list as a dictionary
    name_dict = {'first_name': first_name, 'last_name': last_name, 'full_name': new_name}
    name_list.append(name_dict)

# Write the list of names to a JSON file using the CustomEncoder
with open('names.json', 'w') as f:
    json.dump(name_list, f, cls=CustomEncoder)
