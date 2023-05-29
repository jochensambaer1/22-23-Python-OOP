from flask import Flask, request, redirect, url_for, render_template
import json
import random
import logging
import geojson
import os



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
    def __init__(self, bike_id, state, borrow_time, latitude, longitude):
        self.id = bike_id
        self.state = state
        self.borrow_time = borrow_time
        self.latitude = latitude
        self.longitude = longitude
        logger.debug("Bike object was created with id %s", self.id)


class User:
    def __init__(self, user_id, first_name, last_name, full_name, time_biking, total_time_biking_minutes, saldo):
        self.user_id = user_id  # The user ID
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.time_biking = time_biking
        self.total_time_biking_minutes = total_time_biking_minutes
        self.saldo = saldo
        self.bike = None

        logger.debug(f"Created user {self.user_id} with name {self.full_name} and saldo {self.saldo}")
class Transporter(User):
    id = 0
    state = "available"

    def __init__(self, first_name, last_name):
        super().__init__(Transporter.id, first_name, last_name, f"{first_name} {last_name}", 0, 0, 0)
        self.bikes = []
        self.id = Transporter.id
        Transporter.id += 1


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

        logger.info("Stations loaded: {}".format(len(stations)))
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
            with open('static/Transporters.geojson', 'w') as f:        
            # Write the list of names to a JSON file
                with open('static/Transporters.geojson', 'w') as f:
                    json.dump(name_list, f)
            return redirect(url_for('index'))  
        else:
            return 'Unknown button clicked!'
    except ValueError:
        return 'Invalid input: not a number!'
    
   

if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    with open("static/velo.geojson") as file:
        velo_geojson_data = json.load(file)
    with open("static/bikes.geojson") as file:
         bike_geojson_data = json.load(file)
    with open("static/name.geojson") as file:
        user_geojson_data = json.load(file)
    with open("static/Transporters.geojson") as file:
        transporter_geojson_data = json.load(file)

    bike_share_system = BikeShareSystem(velo_geojson_data)
   
    app.run(debug=True)


