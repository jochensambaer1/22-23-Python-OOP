import json
from flask import Flask, render_template

css_file = "/styles.css"
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/bikes')
def bikes():
    # Read the GeoJSON data from the file
    with open('bikes.geojson') as f:
        data = json.load(f)

    # Extract the features from the GeoJSON data
    features = data['features']

    # Prepare the bike data as a list of dictionaries
    bikes = []
    for feature in features:
        properties = feature['properties']
        geometry = feature['geometry']
        coordinates = geometry['coordinates']
        bike = {
            'type': data['type'],
            'feature_type': feature['type'],
            'geometry_type': geometry['type'],
            'latitude': coordinates[1],
            'longitude': coordinates[0],
            'id': properties['id'],
            'state': properties['state'],
            'borrow_time': properties['borrow_time']
        }
        bikes.append(bike)
    return render_template('bikes.html', css_link = css_file)
@app.route('/station')
def station():
    return render_template('station.html', css_link = css_file)
@app.route('/transporter')
def transporter():
    return render_template('transporter.html', css_link = css_file)
@app.route('/user')
def user():
    return render_template('user.html', css_link = css_file)
if __name__ == '__main__':
    app.run()
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

            return redirect(url_for('index'))

        elif 'simulet' in request.form:
            # Load stations from velo_geojson_data
            stations = velo_geojson_data['features']
            num_stations = len(stations)

            # Create a list of User objects
            users = [User(f"User {i}", "Doe", random.choice(stations), random.choice(stations)) for i in range(input_int)]

            # Create a list of Bike objects
            bikes = [Bike(i) for i in range(input_int)]

            # Create an empty list to store the simulation data
            simulation_data = []

            # Simulate bike rentals and returns
            for i in range(input_int):
                user = random.choice(users)
                bike = random.choice(bikes)
                station = random.choice(stations)
                if user.bike is None:
                    rent_message = f"{user.name} is renting bike {bike.bike_id}"
                    user.borrow_bike(bike)
                    bike.move_to_station(None)
                    simulation_data.append({
                        "action": "rent",
                        "user": user.name,
                        "bike_id": bike.bike_id,
                        "station": None
                    })
                else:
                    return_message = f"{user.name} is returning bike {user.bike.bike_id} to station {station['properties']['name']}"
                    user.return_bike(station)
                    bike_id = user.bike.bike_id if user.bike is not None else None
                    simulation_data.append({
                        "action": "return",
                        "user": user.name,
                        "bike_id": bike_id,
                        "station": station['properties']['name']
                    })

            # Store the simulation data in memory
            session['simulation_data'] = simulation_data

            return redirect(url_for('sim'))
        else:
            return 'Unknown button clicked!'

    except ValueError:
        return 'Invalid input: not a number!'

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
        
        elif 'generat bikes' in request.form:
                        
            # Create a list of bikes
            bike_list = []
            for i in range(input_int):
                bike_id = i+1
                bike_state = BikeState.AVAILABLE
                bike_location = (random.uniform(-90, 90), random.uniform(-180, 180))
                bike_borrow_time = 0
                bike = Bike(id=bike_id, state=bike_state, borrow_time=0, latitude=0.0, longitude=0.0, location=bike_location)
                bike_json = json.dumps(bike, cls=BikeEncoder)
                bike_list.append(bike)
                

            # Convert bikes to geojson and save to file
            features = []
            for bike in bike_list:
                feature = bike.to_geojson()
                features.append(feature)

            feature_collection = geojson.FeatureCollection(features)
            with open('static/bikes.geojson', 'w') as k:
                with open('static/bikes.geojson', 'w') as k:
                    geojson.dump(feature_collection, k)
     

        



            return redirect(url_for('index'))  
        
        elif 'simulet' in request.form:
            # Load stations from velo_geojson_data
            stations = velo_geojson_data['features']
            num_stations = len(stations)
            print(f"Number of stations: {len(stations)}")
            # Create a list of User objects
            users = [User(f"User {i}", "Doe", random.choice(stations), random.choice(stations)) for i in range(input_int)]

            # Create a list of Bike objects
            bikes = [Bike(i) for i in range(input_int)]
            # Create an empty list to store the simulation data
            simulation_data = []

            # Simulate bike rentals and returns
            for i in range(input_int):
                user = random.choice(users)
                bike = random.choice(bikes)
                station = random.choice(stations)
                if user.bike is None:
                    rent_message = f"{user.name} is renting bike {bike.bike_id}"
                    user.borrow_bike(bike)
                    bike.move_to_station(None)
                    simulation_data.append({
                        "action": "rent",
                        "user": user.name,
                        "bike_id": bike.bike_id,
                        "station": None
                    })
                else:
                    return_message = f"{user.name} is returning bike {user.bike.bike_id} to station {station['properties']['name']}"
                    user.return_bike(station)
                    bike_id = user.bike.bike_id if user.bike is not None else None
                    simulation_data.append({
                        "action": "return",
                        "user": user.name,
                        "bike_id": bike_id,
                        "station": station['properties']['name']
                    })

           

            # Write the stations to a JSON file using the StationEncoder
            with open("stations.json", "w") as f:
                with open("stations.json", "w") as f:
                    json.dump(stations, f, cls=StationEncoder)
            
        # Store the simulation data in memory
            session['simulation_data'] = simulation_data
              # Write the stations to a JSON file using the StationEncoder
            with open("stations.json", "w") as f:
                with open("stations.json", "w") as f:
                    json.dump(stations, f, cls=StationEncoder)

            return redirect(url_for('sim'))
        else:
            return 'Unknown button clicked!'
    except ValueError:
        return 'Invalid input: not a number!'