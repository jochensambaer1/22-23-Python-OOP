import geojson
import random
import sys
from abc import ABC, abstractmethod

class StationInterface(ABC):
    @abstractmethod
    def add_bike(self, bike):
        pass

class Bike:
    def __init__(self, id):
        self.id = id
        self.location = None

    @property
    def __geo_interface__(self):
        if self.location is not None:
            return {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [self.location.longitude, self.location.latitude]
                },
                'properties': {
                    'id': self.id,
                    'station_id': self.location.id,
                    'station_name': self.location.name
                }
            }
        else:
            return None

class Station(StationInterface):
    def __init__(self, id, name, longitude, latitude, numberOfPlaces):
        self.id = id
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.numberOfPlaces = min(numberOfPlaces, sys.maxsize) # Ensure that numberOfPlaces does not exceed the maximum size of a Python list
        self.bikes = []

    def add_bike(self, bike_id):
            if len(self.bikes) < self.numberOfPlaces:
                bike = Bike(bike_id)
                self.bikes.append(bike)
                bike.location = self
                return True
            return False

    def add_bikes(self, bikes):
        for bike in bikes:
            self.add_bike(bike)

    @property
    def __geo_interface__(self):
        return {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [self.longitude, self.latitude]
            },
            'properties': {
                'id': self.id,
                'name': self.name,
                'numberOfPlaces': self.numberOfPlaces
            }
        }

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

# Load bikes from bikes.geojson file
with open('bikes.geojson') as f:
    data = geojson.load(f)

bikes = [Bike(f['properties']['id']) for f in data['features']]

# Assign bikes to stations
for station in stations:
    station.add_bikes(bikes)

# Save stations to stations.geojson file
features = []
for station in stations:
    properties = {
        'OBJECTID': station.id,
        'Naam': station.name,
        'Aantal_plaatsen': station.numberOfPlaces
    }
    geometry = geojson.Point((station.longitude, station.latitude))
    feature = geojson.Feature(geometry=geometry, properties=properties)
    features.append(feature)

feature_collection = geojson.FeatureCollection(features)
with open('stations.geojson', 'w') as f:
    geojson.dump(feature_collection, f)
