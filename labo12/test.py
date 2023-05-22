import geojson
import os

print(os.getcwd())  # print current working directory


# Load and parse the geojson file
with open('labo12/velo.geojson') as f:
    data = geojson.load(f)


# Extract data from the features
rows = []
for feature in data['features']:
    properties = feature['properties']
    name = properties.get('name', 'unknown')

    capacity = properties.get('capacity', 'unknown')

    rows.append('<tr><td>{}</td><td>{}</td></tr>'.format(name, capacity))

# Create the HTML table
table = '<table><tr><th>Name</th><th>Capacity</th></tr>{}</table>'.format(''.join(rows))

# Write the HTML table to an output file
with open('output.html', 'w') as f:
    f.write(table)
