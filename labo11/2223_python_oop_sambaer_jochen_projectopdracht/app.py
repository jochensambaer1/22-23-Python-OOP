import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    with open('bikes.geojson') as f:
        data = json.load(f)
    return render_template('index.html', features=data['features'])

@app.route('/transporter.html')
def transporter():
    return render_template('transporter.html')

@app.route('/bike.html')
def bike():
    return render_template('bike.html')

@app.route('/user.html')
def user():
    return render_template('user.html')

@app.route('/station.html')
def station():
    return render_template('station.html')

if __name__ == '__main__':
    app.run(debug=True)
