import time
import random
import geojson
from enum import Enum

# Define BikeState enumeration
class BikeState(Enum):
    AVAILABLE = 'available'
    BORROWED = 'borrowed'
    OVERDUE = 'overdue'
    MAINTENANCE = 'maintenance'

# Define Bike class
class Bike:
    def __init__(self, id, state, location):
        self.id = id
        self.state = state
        self.location = location
        self.borrow_time = None

    def borrow(self, user):
        if self.state == BikeState.AVAILABLE:
            self.state = BikeState.BORROWED
            self.user = user
            self.borrow_time = time.time()
            return True
        else:
            raise Exception("Bike is not available for borrowing")

    def return_to_station(self, station):
        if self.state == BikeState.BORROWED and station.add_bike(self):
            self.state = BikeState.AVAILABLE
            self.user = None
            self.station = station
            elapsed_time = time.time() - self.borrow_time
            self.borrow_time = None
            if elapsed_time >= 30:
                self.state = BikeState.OVERDUE
            elif elapsed_time >= 5:
                self.state = BikeState.MAINTENANCE
            return True
        else:
            raise Exception("Bike cannot be returned to this station")

    def to_geojson(self):
        return geojson.Feature(geometry=geojson.Point(self.location), properties={
            'id': self.id,
            'state': self.state.value,
            'borrow_time': self.borrow_time
        })

# Create a list of bikes
bike_list = []
for i in range(100):
    bike_id = i+1
    bike_state = BikeState.AVAILABLE
    bike_location = (random.uniform(-90, 90), random.uniform(-180, 180))
    bike_borrow_time = 0
    bike = Bike(id=bike_id, state=bike_state, location=bike_location)
    bike_list.append(bike)

# Convert bikes to geojson and save to file
features = []
for bike in bike_list:
    feature = bike.to_geojson()
    features.append(feature)

feature_collection = geojson.FeatureCollection(features)
with open('static/bikes.geojson', 'w') as f:
    with open('static/bikes.geojson', 'w') as f:
        geojson.dump(feature_collection, f)
