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


class User:
    user_id: str
    full_name: str
    borrowed_Bike: Bike = None
    def __init__(self, user_id, name, first_name, last_name, from_station, to_station, time_biking, total_time_biking_minutes, saldo, Bike):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.from_station = from_station
        self.to_station = to_station
        self.time_biking = time_biking
        self.total_time_biking_minutes = total_time_biking_minutes
        self.saldo = saldo
        self.Bike = Bike
        self.name = f"{self.first_name} {self.last_name}"
        self.name = name

    def borrow_Bike(self, Bike):
            if self.borrowed_Bike:
                return "User has already borrowed a Bike"
            if Bike.state != "available":
                return "Bike is not available"
            self.borrowed_Bike = Bike
            Bike.state = "unavailable"
            return "Bike successfully borrowed"
        
    def return_Bike(self):
            if not self.borrowed_Bike:
                return "User doesn't have a borrowed Bike"
            Bike = self.borrowed_Bike
            self.borrowed_Bike = None
            Bike.state = "available"
            return "Bike successfully returned"
        
class Slot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.state = "empty"
        self.Bike = None



        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_names.append(node.name)

        return function_names
    def create_slots(self):
        slots = []
        for i in range(self.capacity):
            slots.append(Slot(i))
        return slots


class Station:
    station_id: str
   
    capacity: int
    def __init__(self, station_id: str, name, slots: List[Slot], capacity: int, feature):
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
        self.capacity = capacity
        self.name = name
        self.latitude, self.longitude = feature['geometry']['coordinates']
        self.slots = slots
        self.slots: List[Slot] = self.create_slots()
        self.Bikes = []

    def create_slots(self):
        slots = []
        for i in range(self.capacity):
            slots.append(Slot(i))
        return slots


    def add_Bike(self, Bike):
        self.Bikes.append(Bike)

    def remove_Bike(self, Bike):
        for slot in self.slots:
            if slot.Bike == Bike:
                self.Bikes.remove(Bike)
                slot.Bike = None
                return
    


    def display_Bikes(self):
        Bike_info = []
        for i, slot in enumerate(self.slots):
            if slot.state == "occupied":
                Bike_info.append(f"Slot {i+1}: {slot.Bike.id}")
            else:
                Bike_info.append(f"Slot {i+1}: Empty")
        return Bike_info




class BikeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Bike):
            return {
                'id': obj.id,
                'state': obj.state,
                'borrow_time': obj.borrow_time,
                'latitude': obj.latitude,
                'longitude': obj.longitude,
                'location': obj.location
            }
        return super().default(obj)




def load_stations(filename):
    stations = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                station = line.strip()
                stations.append(station)
    except FileNotFoundError:
        
        print("Stations file not found.")
    except Exception as e:
       
        print("An error occurred while loading stations:", str(e))
    
    return stations


def get_user(user_id):
   
    users = {
        1: {'name': 'John Doe', 'age': 30},
        2: {'name': 'Jane Smith', 'age': 25},
        3: {'name': 'Bob Johnson', 'age': 35}
    }
    
    if user_id in users:
        return users[user_id]
    else:
        return None
def get_station(station_id):
   
    stations = {
        1: {'name': 'Station A', 'location': 'City X'},
        2: {'name': 'Station B', 'location': 'City Y'},
        3: {'name': 'Station C', 'location': 'City Z'}
    }
    
    if station_id in stations:
        return stations[station_id]
    else:
        return None      

class Transporter(User):
    id = 0
    state = "available"

    def __init__(self, first_name, last_name):
        super().__init__(Transporter.id, first_name, last_name, f"{first_name} {last_name}", 0, 0, 0)
        self.Bikes = []
        self.id = Transporter.id
        Transporter.id += 1

    def collect_Bikes(self, station):
        for i in range(station.capacity):
            if station.slots[i] is not None and station.slots[i].state == "available":
                self.Bikes.append(station.slots[i])
                station.slots[i] = None

    def distribute_Bikes(self, station):
        for i in range(len(self.Bikes)):
            if station.add_Bike(self.Bikes[i]):
                self.Bikes[i].station = station
                self.Bikes.pop(i)
                i -= 1


    def generate_random_users(self):
       
        users = []
        for i in range(10):
            user_id = f"User_{i+1}"
            full_name = f"User {i+1}"
            users.append(User(user_id, full_name))
        return users

    def generate_random_Bikes(self):
        
        Bikes = []
        for i in range(50):
            Bike_id = f"Bike_{i+1}"
            state = "available"
            Bikes.append(Bike(Bike_id, state))
        return Bikes

class BikeShareSystem:
    def __init__(self):
        self.stations = []
        self.users = []

    def add_station(self, station):
        self.stations.append(station)

    def add_user(self, user):
        self.users.append(user)

    def display_stations(self):
        for station in self.stations:
            print(station)

    def display_users(self):
        print("List of Users:")
        for user in self.users:
            print(user)


@app.route('/submit', methods=['POST'])
def submit():
    try:
        input_int = int(request.form['input_text'])
        if 'generet users' in request.form:
                    
            num_names = int(request.args.get('num_names', input_int))  

            with open('data/names.json', 'r', encoding='utf-8') as f:
                names_data = json.load(f)


          
            first_names = names_data['first_name']
            last_names = names_data['last_name']

            
            name_list = []

            
            for k in range(num_names):
                
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)

                
                full_name = f"{first_name} {last_name}"

                
                person_id = k + 1

                
                time_biking_minutes = random.randint(0, 59)
                time_biking_hours = random.randint(0, 10)

                
                total_time_biking_minutes = time_biking_minutes + (time_biking_hours * 60)

                
                saldo = round(random.uniform(0, 1000), 2)

                
                Bike = {}

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
                    'Bike': Bike
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

               

                # Create an empty Bike object
                Bike = {}

                # Add the new name to the list as a dictionary with additional fields
                name_dict = {
                    'id': person_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'full_name': full_name,
                    'time_biking_minutes': time_biking_minutes,
                    'time_biking_hours': time_biking_hours,
                    'total_time_biking_minutes': total_time_biking_minutes,
                    'Bike': Bike
                }

                # Add the new person to the name_list
                name_list.append(name_dict)
            with open('static/Transporters.geojson', 'w') as f:        
            # Write the list of names to a JSON file
                with open('static/Transporters.geojson', 'w') as f:
                    json.dump(name_list, f)
            return redirect(url_for('index'))  
        
        
        elif 'generat Bikes' in request.form:
          
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


                return redirect(url_for('index'))  
        
        elif 'simulet' in request.form:
            simulation_data = []

            with open("static/Bikes.geojson", 'r') as file2:
                Bike_geojson_data = json.load(file2)
                Bike_count = len(Bike_geojson_data['features'])
                print(f"Number of Bikes: {Bike_count}")

            with open("static/name.geojson", 'r') as file3:
                user_geojson_data = json.load(file3)
                user_count = len(user_geojson_data)
                
                stations = load_stations('velo.geojson')
                print(f"Number of stations: {len(stations)}")

            user_id = request.args.get('user_id')
            station_id = request.args.get('station_id')
            
            selected_user = get_user(user_id)
            selected_station = get_station(station_id)

            if selected_user is None:
                    print("Selected user is not found.")
                    # Perform the appropriate action for handling the case when selected_user is None
            else:
                    if 'Bike' in selected_user:
                        # Access the 'Bike' property on the selected_user object
                        if selected_user['Bike'] is None:
                            print(f"{selected_user['name']} is renting Bike {selected_Bike['Bike_id']}")
                            selected_user.borrow_Bike(selected_Bike)
                            selected_Bike.move_to_station(None)
                            simulation_data.append({
                                "action": "rent",
                                "user": selected_user['name'],
                                "Bike_id": selected_Bike['Bike_id'],
                                "station": None
                            })
                        else:
                            print(f"{selected_user['name']} is returning Bike {selected_user['Bike']['Bike_id']} to station {selected_station['name']}")
                            selected_user.return_Bike(selected_station)
                            Bike_id = selected_user['Bike']['Bike_id'] if selected_user['Bike'] is not None else None
                            simulation_data.append({
                                "action": "return",
                                "user": selected_user['name'],
                                "Bike_id": Bike_id,
                                "station": selected_station['name']
                            })
                    else:
                        print("Selected user has no 'Bike' property.")
                        # Perform the appropriate action for handling the case when selected_user does not have the 'Bike' property

            with open("static/simulation.geojson", "w") as h:
                json.dump(simulation_data, h)


                    

                
        
            return redirect(url_for('index'))  
        else:
            return 'Unknown button clicked!'
    except ValueError:
        return 'Invalid input: not a number!'

    
@app.route('/')
def index():
    # Example data
    username = 'John Doe'
    age = 30
    interests = ['Programming', 'Reading', 'Sports']

    # Passing data to the template
    return render_template('index.html', username=username, age=age, interests=interests)

@app.route('/sim')
def sim():
    return render_template('sim.html')

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = get_user(user_id)
    return render_template('user.html', user=user)

@app.route('/station/<int:station_id>')
def station_details(station_id):
    station = get_station(station_id)
    return render_template('station.html', station=station)


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

    with open("static/Bikes.geojson", 'r') as file2:
        Bike_geojson_data = json.load(file2)
        logger.debug("Bikes.geojson ingelezen en opgeslagen in het geheugen")

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
