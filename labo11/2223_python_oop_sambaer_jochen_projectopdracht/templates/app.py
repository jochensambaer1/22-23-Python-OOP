from flask import Flask, render_template, request, jsonify
import json
import random
import os
from typing import List
import argparse
import logging

app = Flask(__name__)
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
        self.slots = slots

    def create_slots(self):
        """
        create the slots for this station
        """
        log.info(f"creating {self.parking_spaces} slots")
        return [Slot() for _ in range(self.parking_spaces)]

class Slot:
    # A slot is a place in which a bike can be parked
    def __init__(self, slot_id: str, bike: "Bike" = None):
        # Initialize the slot object
        self.id = slot_id
        self.bike = bike

class Bike:
    def __init__(self, bike_id, state, borrow_time, latitude, longitude):
        self.id = bike_id
        self.state = state
        self.borrow_time = borrow_time
        self.latitude = latitude
        self.longitude = longitude
        logger.debug("Bike object was created with id %s", self.id)


class User:
    def __init__(self, first_name, last_name, full_name, time_biking, total_time_biking_minutes, saldo):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.time_biking = time_biking
        self.total_time_biking_minutes = total_time_biking_minutes
        self.saldo = saldo
        self.user_id = user_id # The user ID      
        self.bike = bike # The bike the user is currently using

        logger.debug(f"Created user {self.user_id} with name {self.full_name} and saldo {self.saldo}")

class BikeShareSystem(object):
    def __init__(self, geojson_data):
        self.stations = self.load_stations(geojson_data)
        self.users = []
        self.transporters = []

    # Load stations from JSON data
    def load_stations(self, geojson_data):
        stations = []

        for feature in geojson_data["features"]:
            properties = feature["properties"]
            station_id = properties["OBJECTID"]
            name = properties["Naam"]
            capacity = properties["Aantal_plaatsen"]
            slots = [Slot(slot_id) for slot_id in range(capacity)]
            station = Station(station_id, name, slots, feature)
            stations.append(station)

        print("Stations loaded: {}".format(len(stations)))
        return stations

class BikeTransporter(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, full_name: str):
        super().__init__(user_id, first_name, last_name, full_name)
        logger.debug("Created a BikeTransporter object")


def generate_random_users(num_users: int) -> list[User]:
    # Generate a list of random users.
    users = [User(f"User {i+1}", f"User {i+1}") for i in range(num_users)]
    # Log a message saying how many users were generated.
    logger.info(f"Generated {len(users)} users.")
    # Return the list of users.
    return users

def generate_random_transporters(num_transporters: int) -> list[BikeTransporter]:
    """
    Generate a list of random transporters.

    :param num_transporters: Number of transporters to generate.
    :return: A list of random transporters.
    """
    logger.debug(f"Generating {num_transporters} transporters")
    transporters = [BikeTransporter(f"Transporter{i+1}", f"Transporter {i+1}")
                    for i in range(num_transporters)]
    logger.debug(f"Generated {num_transporters} transporters")
    return transporters

@app.route("/stations")
def stations():
    """
    Returns a list of stations
    """
    app.logger.info("List of stations")
    return "List of stations"

@app.route("/users")
def users():
    """
    Returns a list of users
    """
    app.logger.info("List of users")
    return "List of users"

@app.route("/bikes")
def bikes():
    """
    Returns a list of bikes
    """
    app.logger.info("List of bikes")
    return "List of bikes"

@app.route('/')
def index():
    sort_param = request.args.get('sort')

    bikes = load_bike_data()
    stations = load_station_data()
    users = load_user_data()

    if sort_param == 'id':
        bikes.sort(key=lambda x: x.id)
        stations.sort(key=lambda x: x.id)
        users.sort(key=lambda x: x.user_id)
    elif sort_param == 'name':
        bikes.sort(key=lambda x: x.name)
        stations.sort(key=lambda x: x.name)
        users.sort(key=lambda x: x.full_name)
    else:
        print('sort_param is not recognized')

    return render_template('index.html', stations=stations, users=users, bikes=bikes)

def load_stations(geojson_data):
    """Loads a list of stations from geojson data."""
    stations = []
    
    for feature in geojson_data["features"]:
        properties = feature["properties"]
        station_id = properties["OBJECTID"]
        name = properties["Naam"]
        capacity = properties["Aantal_plaatsen"]
        logging.debug("Creating slots for station {0} with capacity {1}".format(station_id, capacity))
        slots = [Slot(slot_id) for slot_id in range(capacity)]
        station = Station(station_id, name, slots, feature)
        stations.append(station)
    
    return stations

def load_station_data():
        with open('velo.geojson') as file:
            geojson_data = json.load(file)
        return load_stations(geojson_data)
    stations = []
    
for feature in geojson_data["features"]:
        properties = feature["properties"]
        station_id = properties["OBJECTID"]
        name = properties["Naam"]
        capacity = properties["Aantal_plaatsen"]
        logging.debug("Creating slots for station {0} with capacity {1}".format(station_id, capacity))
        slots = [Slot(slot_id) for slot_id in range(capacity)]
        station = Station(station_id, name, slots, feature)
        stations.append(station)
        return station_data



def load_user_data():
    with open('/static/name.geojson') as file:
        data = json.load(file)
        users = []

        for user in data:
            # Get user data from json
            user_id = user['id']
            logging.debug('Starting with user_id: %d' % user_id)
            first_name = user['first_name']
            last_name = user['last_name']
            full_name = user['full_name']
            time_biking_minutes = user['time_biking_minutes']
            time_biking_hours = user['time_biking_hours']
            total_time_biking_minutes = user['total_time_biking_minutes']
            saldo = user['saldo']
            bike = user['bike']

            # Create User object and add it to list of users
            user_data = User(user_id, first_name, last_name, full_name,
                             time_biking_minutes, time_biking_hours,
                             total_time_biking_minutes, saldo, bike)
            users.append(user_data)
            logging.debug('User_id: %d is done' % user_id)

        return users

# Endpoint to generate and retrieve the specified number of names
@app.route('/generate_names')
def generate_names():
    num_names = int(request.args.get('num_names', 10))  # Default to 10 names if not specified

    with open('/static/names.json', 'r', encoding='utf-8') as f:
        names_data = json.load(f)

    # Assuming names_data is a list of dictionaries, you can extract the first and last names
    first_names = names_data['first_name']
    last_names = names_data['last_name']

    # Create a list of dictionaries to store the generated names
    name_list = []

    # Generate the specified number of names and add them to the list
    for i in range(num_names):
        # Select two random names from the first_names and last_names lists
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        # Combine the names to create a new name
        full_name = f"{first_name} {last_name}"

        # Create a unique ID for each person
        person_id = i + 1

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



    

    return jsonify(name_list)
  

def load_bike_data():
    # Open file and load data
    with open('bikes.geojson') as file:
        data = json.load(file)
        bikes = []

        # Extract data from each feature
        for feature in data['features']:
            properties = feature['properties']
            bike_id = properties['id']
            state = properties['state']
            borrow_time = properties['borrow_time']
            coordinates = feature['geometry']['coordinates']
            latitude = coordinates[1]
            longitude = coordinates[0]

            # Create bike data object and add to list
            bike_data = Bike(bike_id, state, borrow_time, latitude, longitude)
            bikes.append(bike_data)

            # Log the bike data
            logger.info('Loaded bike data: %s', bike_data)

        # Return list of bike data
        return bikes

def main():
    parser = argparse.ArgumentParser(description="Velo Bike Share System")
    parser.add_argument("-s", "--simulate", action="store_true", help="Enable simulation mode")
    args = parser.parse_args()
    app.run(debug=True)
    with open("velo.geojson") as file:
        geojson_data = json.load(file)

    bike_share_system = BikeShareSystem(geojson_data)
    users = generate_random_users(55000)
    transporters = generate_random_transporters(10)
    bike_share_system.users.extend(users)
    bike_share_system.transporters.extend(transporters)

    if args.simulate:
        simulation = Simulation(bike_share_system)
        simulation.run()
    else:
        user_id = input("Enter user id: ")
        print("User ID: {}".format(user_id))
        bike_share_system.get_user(user_id).request_bike()

if __name__ == '__main__':
    main()
   
