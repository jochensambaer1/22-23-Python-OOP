from flask import Flask, request, redirect, url_for, render_template
import json
import random
import logging
import geojson
from enum import Enum
from datetime import datetime
from typing import List
import ast
from dataclasses import dataclass, field
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
logger = logging.getLogger(__name__)

# Define BikeState enumeration
class BikeState(str, Enum):
    AVAILABLE = 'available'
    BORROWED = 'borrowed'
    OVERDUE = 'overdue'
    MAINTENANCE = 'maintenance'

class Bike:
    id: str
    state: str
    def __init__(self , id , state , borrow_time=0, latitude=None, longitude=None , location=None):
        self.id = id
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        self.last_state_change = datetime.now()
        self.current_station = None
       # self.borrow_time = None
        self.id = id
    #   self.state = state
    #   self.location = location
        self.borrow_time = borrow_time
    #   self.latitude = latitude
    #   self.longitude = longitude
        self.user = None
        self.station = None    
    #  def __init__(self, id, state, location, borrow_time=0, latitude=None, longitude=None):
 
        
    def move_to_station(self, station):
        self.state = station
        if self.current_station:
            self.current_station.remove_Bike(self)
        self.current_station = station
        station.add_Bike(self)
        print(f"Bike {self.id} has been moved to station {station.name}")
        
    def to_geojson(self):
        return geojson.Feature(geometry=geojson.Point(self.location), properties={
            'id': self.id,
            'state': self.state.value,
            'borrow_time': self.borrow_time
        })
input_int=100
# Create a list of bikes
bike_list = []
for b in range(input_int):
        bike_id = b+1
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
#etewr