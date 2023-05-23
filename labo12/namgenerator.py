import json
import random
import chardet

# Use chardet to detect the character encoding of the JSON file
with open('names.json', 'rb') as f:
    result = chardet.detect(f.read())

# Open the JSON file with the detected character encoding
with open('names.json', 'r', encoding=result['encoding']) as f:
    names = json.load(f)

# Create a list of dictionaries to store the generated names
name_list = []

# Generate 1000 names and add them to the list
for i in range(1000):
    # Select two random names from the first_names and last_names fields
    first_name = random.choice(names['first_names'])
    last_name = random.choice(names['last_names'])

    # Combine the names to create a new name
    new_name = f"{first_name} {last_name}"

    # Add the new name to the list as a dictionary
    name_dict = {'first_name': first_name, 'last_name': last_name, 'full_name': new_name}
    name_list.append(name_dict)

# Write the list of names to a JSON file
with open('names.json', 'w') as f:
    json.dump(name_list, f)
