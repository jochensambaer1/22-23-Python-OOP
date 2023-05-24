# main.py
import json
import geojson
from bike import Bike
from station import Station
from helpers import CustomEncoder, random, chardet
from user import User

bikes = []

for i in range(100):
    id = i + 1
    state = "available"
    borrow_time = random()
    bike = Bike(id, state, borrow_time)
    bikes.append(bike)

stations = [
    Station("Station 1", 40.7128, -74.0060),
    Station("Station 2", 51.5074, -0.1278),
    Station("Station 3", 35.6895, 139.6917)
]

for station in stations:
    for bike in bikes:
        if station.add_bike(bike):
            break

users = [
    User("John", "Doe", "Station 1", "Station 2"),
    User("Jane", "Doe", "Station 2", "Station 3"),
    User("Bob", "Smith", "Station 3", "Station 1")
]

features = []

# Loop over each user object and create a feature with its location and properties
for user in users:
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
