# bike.py
import time
import random
import geojson

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
