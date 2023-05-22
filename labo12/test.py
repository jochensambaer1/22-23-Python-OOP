import geojson
import os

print(os.getcwd())  # print current working directory

# Load and parse the geojson file
with open('velo.geojson') as f:
    data = geojson.load(f)

# Extract data from the features
rows = []
for feature in data['features']:
    properties = feature['properties']
    location_name = properties.get('Naam', 'unknown')
    num_places = properties.get('Aantal_plaatsen', 'unknown')
    location_type = properties.get('Objecttype', 'unknown')
    location_use = properties.get('Gebruik', 'unknown')
    location_street = properties.get('Straatnaam', 'unknown')
    location_number = properties.get('Huisnummer', 'unknown')
    location_district = properties.get('District', 'unknown')
    location_postcode = properties.get('Postcode', 'unknown')
    geometry = feature.get('geometry', 'unknown')
    type = feature.get('type', 'unknown')
    coordinates = geometry.get('coordinates', 'unknown')

    rows.append('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(
        location_name, num_places, location_type, location_use, location_street, location_number, location_district, location_postcode))

# Create the HTML table
table = '<table><tr><th>Name</th><th>Capacity</th><th>Type</th><th>Use</th><th>Street</th><th>Number</th><th>District</th><th>Postcode</th></tr>{}</table>'.format(''.join(rows))

# Write the HTML table to an output file
with open('output.html', 'w') as f:
    f.write(table)
