import json
import random

# Read the JSON file
with open('names.json', 'r', encoding='utf-8') as f:
    names_data = json.load(f)

# Assuming names_data is a list of dictionaries, you can extract the first and last names
first_names = names_data['first_name']
last_names = names_data['last_name']

# Create a list of dictionaries to store the generated names
name_list = []

# Generate 1000 names and add them to the list
for i in range(1000):
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
    name_list.append(name_dict)

# Write the list of names to a JSON file
with open('name.geojson', 'w') as f:
    json.dump(name_list, f)
