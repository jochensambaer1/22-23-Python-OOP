from ast import List
from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
import logging
import geojson
import os
from enum import Enum
from datetime import datetime
from typing import List
import time




app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['JSON_SORT_KEYS'] = False
logger = logging.getLogger(__name__)



class Station:
    def __init__(self, station_id, name, slots, feature):
        properties = feature['properties']
        self.station_id = station_id
        self.object_type = properties['Objecttype']
        self.velo_type = properties['Type_velo']
        self.location = properties['Ligging']
        self.street_name = properties['Straatnaam']
        self.house_number = properties['Huisnummer']
        self.additional_info = properties['Aanvulling']
        self.district = properties['District']
        self.postal_code = properties['Postcode']
        self.object_code = properties['Objectcode']
        self.usage_status = properties['Gebruik']
        self.parking_spaces = properties['Aantal_plaatsen']
        self.name = name
        self.latitude, self.longitude = feature['geometry']['coordinates']
        self.slots = self.create_slots()

    def create_slots(self):
        """
        Create the slots for this station.
        """
        logger.info(f"Creating {self.parking_spaces} slots")
        return [Slot() for _ in range(self.parking_spaces)]


class Slot:
    # A slot is a place in which a bike can be parked
    def __init__(self, slot_id: str, bike: "Bike" = None):
        # Initialize the slot object
        self.id = slot_id
        self.bike = bike

class Bike:
    def __init__(self, id, state, borrow_time, latitude, longitude, location):
        self.id = id
        self.state = state
        self.borrow_time = borrow_time
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        self.last_state_change = datetime.now()
    def to_geojson(self):
        return geojson.Feature(geometry=geojson.Point(self.location), properties={
            'id': self.id,
            'state': self.state.value,
            'borrow_time': self.borrow_time
        })
        return json.dumps(bike_feature)

        
class BikeState(Enum):
    def __init__(self, state):
        self.state = state

    def to_dict(self):
        return {"state": self.state}

class BikeState(Enum):
    AVAILABLE = 'available'
    BORROWED = 'borrowed'
    OVERDUE = 'overdue'
    MAINTENANCE = 'maintenance'
    
class BikeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Bike):
            return obj.__dict__
        if isinstance(obj, BikeState):
            return obj.value
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class User:
    def __init__(self, first_name, last_name, current_station, destination_station, time_biking=0, total_time_biking_minutes=0, saldo=0):
        self.first_name = first_name
        self.last_name = last_name
        self.current_station = current_station
        self.destination_station = destination_station
        self.bike = None
        self.time_biking = time_biking
        self.total_time_biking_minutes = total_time_biking_minutes
        self.saldo = saldo

    def borrow_bike(self, bike):
        self.bike = bike
        self.current_station.remove_bike(bike)
        bike.borrow(self)

    def return_bike(self, station):
        self.current_station = station
        station.add_bike(self.bike)
        self.bike.returned()
        self.bike = None

    def move_bike_to_nearest_station(self, stations):
        nearest_station = self.find_nearest_station(stations)
        self.bike.move_to_station(nearest_station)
        self.current_station = nearest_station

class Transporter:
    def __init__(self, first_name, last_name, station1, station2):
        self.first_name = first_name
        self.last_name = last_name
        self.station1 = station1
        self.station2 = station2


    def redistribute_bikes(self, stations):
        for station in stations:
            if station.is_full():
                nearby_station = self.find_nearest_station(stations, station)
                bikes_to_transfer = station.get_bikes_to_transfer()
                for bike in bikes_to_transfer:
                    station.remove_bike(bike)
                    nearby_station.add_bike(bike)
            elif station.is_empty():
                nearby_station = self.find_nearest_station(stations, station)
                bikes_to_transfer = nearby_station.get_bikes_to_transfer()
                for bike in bikes_to_transfer:
                    nearby_station.remove_bike(bike)
                    station.add_bike(bike)

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



class BikeShareSystem:
    def __init__(self, geojson_data):
        self.stations = self.load_stations(geojson_data)

    def load_stations(self, geojson_data):
        features = geojson_data["features"]
        stations = []
        for feature in features:
            properties = feature["properties"]
            name = properties["Naam"]
            coordinates = feature["geometry"]["coordinates"]
            station = {"name": name, "coordinates": coordinates}
            stations.append(station)
        return stations



def generate_random_users(num_users):
    users = []
    for i in range(num_users):
        first_name = f"User {i+1}"
        last_name = f"Last Name {i+1}"
        full_name = f"{first_name} {last_name}"
        time_biking = 0
        total_time_biking_minutes = 0
        saldo = 0

        user = User(i+1, first_name, last_name, full_name, time_biking, total_time_biking_minutes, saldo)
        users.append(user)

    return users

    return users


def generate_random_bikes(num_bikes):
    # Generate a list of random bikes
    bikes = [Bike(f"Bike {i+1}", random.choice(["Available", "Unavailable"]), 0, 0, 0) for i in range(num_bikes)]
    logger.info(f"Generated {len(bikes)} random bikes")
    return bikes



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/sim')
def sim():
    return render_template('sim.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        input_int = int(request.form['input_text'])
        if 'generet users' in request.form:
            num_names = int(request.args.get('num_names', input_int))  # Default to 10 names if not specified

            with open('data/names.json', 'r', encoding='utf-8') as f:
                names_data = json.load(f)

            # Assuming names_data is a list of dictionaries, you can extract the first and last names
            first_names = names_data['first_name']
            last_names = names_data['last_name']

            # Create a list of dictionaries to store the generated names
            name_list = []

            # Generate the specified number of names and add them to the list
            for k in range(num_names):
                # Select two random names from the first_names and last_names lists
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)

                # Combine the names to create a new name
                full_name = f"{first_name} {last_name}"

                # Create a unique ID for each person
                person_id = k + 1

                # Generate random values for time biking in minutes and hours
                time_biking_minutes = random.randint(0, 59)
                time_biking_hours = random.randint(0, 10)

                # Calculate the total time biking in minutes
                total_time_biking_minutes = time_biking_minutes + (time_biking_hours * 60)

                # Generate a random saldo (account balance) with a maximum of 2 decimal places
                saldo = round(random.uniform(0, 1000), 2)

                # Create an empty bike object
                bike = {}

                # Add the new name to the list as a dictionary with additional fields
                name_dict = {
                    'id': person_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'full_name': full_name,
                    'time_biking_minutes': time_biking_minutes,
                    'time_biking_hours': time_biking_hours,
                    'total_time_biking_minutes': total_time_biking_minutes,
                    'saldo': saldo,
                    'bike': bike
                }

                # Add the new person to the name_list
                name_list.append(name_dict)

            # Store the list of names in memory
            session['name_list'] = name_list
            with open('static/name.geojson', 'w') as f:        
                            # Write the list of names to a JSON file
                            with open('static/name.geojson', 'w') as f:
                                json.dump(name_list, f)
                        
            return redirect(url_for('index'))

        elif 'generat transporters' in request.form:
            num_names = int(request.args.get('num_names', input_int))  # Default to 10 names if not specified

            with open('data/names.json', 'r', encoding='utf-8') as f:
                names_data = json.load(f)

            # Assuming names_data is a list of dictionaries, you can extract the first and last names
            first_names = names_data['first_name']
            last_names = names_data['last_name']

            # Create a list of dictionaries to store the generated names
            name_list = []

            # Generate the specified number of names and add them to the list
            for k in range(num_names):
                # Select two random names from the first_names and last_names lists
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)

                # Combine the names to create a new name
                full_name = f"{first_name} {last_name}"

                # Create a unique ID for each person
                person_id = k + 1

                # Generate random values for time biking in minutes and hours
                time_biking_minutes = random.randint(0, 59)
                time_biking_hours = random.randint(0, 10)

                # Calculate the total time biking in minutes
                total_time_biking_minutes = time_biking_minutes + (time_biking_hours * 60)

               

                # Create an empty bike object
                bike = {}

                # Add the new name to the list as a dictionary with additional fields
                name_dict = {
                    'id': person_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'full_name': full_name,
                    'time_biking_minutes': time_biking_minutes,
                    'time_biking_hours': time_biking_hours,
                    'total_time_biking_minutes': total_time_biking_minutes,
                    'bike': bike
                }

                # Add the new person to the name_list
                name_list.append(name_dict)
                name_list.append(name_dict)
            with open('static/Transporters.geojson', 'w') as f:        
            # Write the list of names to a JSON file
                with open('static/Transporters.geojson', 'w') as f:
                    json.dump(name_list, f)
            # Store the list of names in memory
            session['name_list'] = name_list

            return redirect(url_for('index'))

        elif 'generat bikes' in request.form:
            # Create a list of bikes
            bike_list = []
            for i in range(input_int):
                bike_id = i+1
                bike_state = BikeState.AVAILABLE
                bike_location = (random.uniform(-90, 90), random.uniform(-180, 180))
                bike_borrow_time = 0
                bike = Bike(id=bike_id, state=bike_state, borrow_time=0, latitude=0.0, longitude=0.0, location=bike_location)
                bike_list.append(bike)

            # Convert bikes to geojson
            features = []
            for bike in bike_list:
                feature = bike.to_geojson()
                features.append(feature)

            feature_collection = geojson.FeatureCollection(features)

            # Store the feature collection in memory
            session['bike_collection'] = feature_collection
                   # Add the new person to the name_list
            feature_collection = geojson.FeatureCollection(features)
            with open('static/bikes.geojson', 'w') as k:
                with open('static/bikes.geojson', 'w') as k:
                    geojson.dump(feature_collection, k)

            return redirect(url_for('index'))

        elif 'simulet' in request.form:
             # Load stations from velo_geojson_data
            stations = velo_geojson_data['features']
            num_stations = len(stations)

            # Create a list of User/Transporter objects
            users = [User('John', 'Doe', random.choice(stations), random.choice(stations)) for _ in range(input_int)]
            transporters = [Transporter('John', 'Doe', random.choice(stations), random.choice(stations)) for _ in range(input_int)]


            # Initialize simulation
            simulation_steps = input_int

            simulation_data = []

            for step in range(simulation_steps):
                # Simulate bike borrowing/returning by users
                for user in users:
                    if user.bike is None:
                        available_bikes = user.current_station.get_bikes()
                        if available_bikes:
                            bike = random.choice(available_bikes)
                            user.borrow_bike(bike)
                            simulation_data.append({
                                "action": "rent",
                                "user": user.full_name,
                                "bike_id": bike.id,
                                "station": user.current_station.name
                            })

                    elif user.current_station == user.destination_station:
                        user.return_bike(user.current_station)
                        simulation_data.append({
                            "action": "return",
                            "user": user.full_name,
                            "bike_id": user.bike.id,
                            "station": user.current_station.name
                        })

                    else:
                        user.move_bike_to_nearest_station(stations)

                # Simulate bike redistribution by transporter
                transporters.redistribute_bikes(stations)

            # Store the simulation data in memory
            session['simulation_data'] = simulation_data

            # Write the stations to a JSON file using the StationEncoder
            with open("stations.json", "w") as f:
                json.dump(stations, f, cls=StationEncoder)

                    
                        

            return redirect(url_for('sim'))
        else:
            return 'Unknown button clicked!'

    except ValueError:
        return 'Invalid input: not a number!'

   



if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    with open("static/velo.geojson", 'r') as file1:
        velo_geojson_data = json.load(file1)
        logger.debug("velo.geojson ingelezen en opgeslagen in het geheugen")

    with open("static/bikes.geojson", 'r') as file2:
        bike_geojson_data = json.load(file2)
        logger.debug("bikes.geojson ingelezen en opgeslagen in het geheugen")

    with open("static/name.geojson", 'r') as file3:
        user_geojson_data = json.load(file3)
        logger.debug("name.geojson ingelezen en opgeslagen in het geheugen")

    with open("static/Transporters.geojson", 'r') as file4:
        transporter_geojson_data = json.load(file4)
        logger.debug("Transporters.geojson ingelezen en opgeslagen in het geheugen")

    with open("static/simulation.geojson", 'r') as file5:
        simulation_geojson_data = json.load(file5)
        logger.debug("simulation.geojson ingelezen en opgeslagen in het geheugen")
  
    logger.info("Starting the Flask application")
    app.run(debug=True)

    logger.info("Exiting the application")



