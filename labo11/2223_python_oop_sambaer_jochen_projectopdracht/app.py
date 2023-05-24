import json
from flask import Flask, render_template


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
    return render_template('bikes.html')
@app.route('/station')
def station():
    return render_template('station.html')
@app.route('/transporter')
def transporter():
    return render_template('transporter.html')
@app.route('/user')
def user():
    return render_template('user.html')
if __name__ == '__main__':
    app.run()
