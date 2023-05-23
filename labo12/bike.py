import json
import geojson
import time
import random

class Bike:
    def __init__(self, id, state, borrow_time=0):
        self.id = id
        self.state = state
        self.user = None
        self.station = None
        self.location = None
        self.borrow_time = borrow_time
        self.start_time = None  

    def borrow(self, user):
        if self.state == "available":
            self.state = "borrowed"
            self.user = user
            self.borrow_time = 0
            self.start_time = time.time() 
            return True
        return False

    def return_to_station(self, station):
        if self.state == "borrowed" and station.add_bike(self):
            self.state = "available"
            self.user = None
            self.station = station
            elapsed_time = time.time() - self.start_time  
            self.borrow_time += elapsed_time  
            if self.maintenance():
                print(f"Bike {self.id} is now in maintenance")
            return True
        return False
    
    def maintenance(self):
        if self.borrow_time >= 3000:
            self.state = "maintenance" 
            return True
        return False

bikes = []

for i in range(100):
    id = i + 1
    state = "available"
    borrow_time = random.randint(0, 3600)
    bike = Bike(id, state, borrow_time)
    bikes.append(bike)

features = []

for bike in bikes:
    point = geojson.Point((0, 0))
    properties = {"id": bike.id, "state": bike.state, "borrow_time": bike.borrow_time}
    feature = geojson.Feature(geometry=point, properties=properties)
    features.append(feature)

feature_collection = geojson.FeatureCollection(features)

with open("bikes.geojson", "w") as f:
    geojson.dump(feature_collection, f)
# Save bikes to bikes.geojson file
features = []
for bike in bikes:
    properties = {
        'id': bike.id
    }
    geometry = bike.location
    feature = geojson.Feature(geometry=geometry, properties=properties)
    features.append(feature)


feature_collection = geojson.FeatureCollection(features)
with open('bikes.geojson', 'w') as f:
    geojson.dump(feature_collection, f)
