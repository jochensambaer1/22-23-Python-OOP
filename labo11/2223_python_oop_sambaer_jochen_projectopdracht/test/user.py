import json
import random
from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime
import chardet
import geojson
from typing import NamedTuple



class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif callable(obj):
            return None
        else:
            return super().default(obj)


class Station(NamedTuple):
    station_id: int
    name: str
    longitude: float
    latitude: float
    number_of_places: int

    def __repr__(self):
        return f"Station(station_id={self.station_id}, name={self.name}, longitude={self.longitude}, latitude={self.latitude}, number_of_places={self.number_of_places})"


class User:
    def __init__(self, name: str, surname: str, home_station: Station, work_station: Station):
        """
        Create a new User object.

        Args:
            name: The user's name.
            surname: The user's surname.
            home_station: The user's home station.
            work_station: The user's work station.
        """
        print(f"Creating user {name} with home station {home_station} and work station {work_station}")
        self.name = name
        self.surname = surname
        self.bike: Optional[Any] = None
        self.home_station = home_station
        self.work_station = work_station
        self.ouwers_bikt =0

    def borrow_bike(self, bike):
        if bike.borrow(self):
            self.bike = bike
            return True
        return False

    def return_bike(self, station):
        if self.bike is not None and self.bike.return_to_station(station):
            self.bike = None
            return True
        return False


def generate_names(num_names: int) -> List[Dict[str, str]]:
    """
    Generate a list of random names.

    Args:
        num_names: The number of names to generate.

    Returns:
        A list of dictionaries containing the generated names.
    """
    # Load names from names.json file
    with open('names.json', 'rb') as f:
        result = chardet.detect(f.read())

    # Open the JSON file with the detected character encoding
    with open('names.json', 'r', encoding=result['encoding']) as f:
        names = json.load(f)

    # Generate names and add them to the list
    name_list = [{'first_name': random.choice(names['first_names']),
                  'last_name': random.choice(names['last_names']),
                  'full_name': f"{first_name} {last_name}"}
                 for _ in range(num_names)]

    # Create a FeatureCollection with the names
    feature_collection = geojson.FeatureCollection(name_list)

    # Write the FeatureCollection to a GeoJSON file using the CustomEncoder
    with open("names.geojson", "w") as f:
        json.dump(feature_collection, f, cls=CustomEncoder)

    return name_list
class Bike:
    def __init__(self, id, state, location):
        self.id = id
        self.state = state
        self.location = location
        self.borrow_time = None

    def borrow(self, user):
        if self.state == BikeState.AVAILABLE:
            self.state = BikeState.BORROWED
            self.user = user
            self.borrow_time = time.time()
            return True
        else:
            raise Exception("Bike is not available for borrowing")

    def return_to_station(self, station):
        if self.state == BikeState.BORROWED and station.add_bike(self):
            self.state = BikeState.AVAILABLE
            self.user = None
            self.station = station
            elapsed_time = time.time() - self.borrow_time
            self.borrow_time = None
            if elapsed_time >= 30:
                self.state = BikeState.OVERDUE
            elif elapsed_time >= 5:
                self.state = BikeState.MAINTENANCE
            return True
        else:
            raise Exception("Bike cannot be returned to this station")

    def to_geojson(self):
        return geojson.Feature(geometry=geojson.Point(self.location), properties={
            'id': self.id,
            'state': self.state.value,
            'borrow_time': self.borrow_time
        })
def load_bikes(filename: str) -> List[Bike]:
    """
    Load bikes from a GeoJSON file.

    Args:
        filename: The name of the GeoJSON file.

    Returns:
        A list of Bike objects.
    """
    with open(filename) as f:
        data = geojson.load(f)

    bikes = []
    for feature in data['features']:
        properties = feature['properties']
        bike_id = properties.get('bike_id')
        bikes.append(Bike(bike_id))

    return bikes


class StationEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Station):
            return {
                "station_id": obj.station_id,
                "name": obj.name,
                "longitude": obj.longitude,
                "latitude": obj.latitude,
                "number_of_places": obj.number_of_places
            }
        return super().default(obj)


def get_station_coords(station: Station) -> Tuple[float, float]:
    longitude = station.longitude
    latitude = station.latitude
    return longitude, latitude


def load_stations(filename: str) -> List[Station]:
    """
    Load stations from a GeoJSON file.

    Args:
        filename: The name of the GeoJSON file.

    Returns:
        A list of Station objects.
    """
    with open(filename) as f:
        data = geojson.load(f)
    
    print(f"Found {len(data['features'])} features in GeoJSON file")

    stations = []
    for feature in data['features']:
        properties = feature['properties']
        station_id = properties.get('station_id')
        bikes = [Bike(i) for i in range(100)]
        name = properties.get('name', f"Station {station_id}")
        number_of_places = properties.get('number_of_places', 0)
        longitude, latitude = feature['geometry']['coordinates']
        stations.append(Station(station_id, name, longitude, latitude, number_of_places))

    print(f"Loaded {len(stations)} stations")
    return stations


# Load stations from stations.geojson file
stations = load_stations('velo.geojson')
print(f"Number of stations: {len(stations)}")

# Create a list of User objects
users = [User(f"User {i}", "Doe", random.choice(stations), random.choice(stations)) for i in range(1000)]

# Create a list of Bike objects
bikes = [Bike(i) for i in range(100)]
# Create an empty list to store the simulation data
simulation_data = []

# Simulate bike rentals and returns
for i in range(10000):
    user = random.choice(users)
    bike = random.choice(bikes)
    station = random.choice(stations)
    if user.bike is None:
        print(f"{user.name} is renting bike {bike.bike_id}")
        user.borrow_bike(bike)
        bike.move_to_station(None)
        simulation_data.append({
            "action": "rent",
            "user": user.name,
            "bike_id": bike.bike_id,
            "station": None
        })
    else:
        print(f"{user.name} is returning bike {user.bike.bike_id} to station {station.name}")
        user.return_bike(station)
        bike_id = user.bike.bike_id if user.bike is not None else None
        simulation_data.append({
            "action": "return",
            "user": user.name,
            "bike_id": bike_id,
            "station": station.name
        })

# Write the simulation data to a JSON file
with open("simulation.json", "w") as f:
    json.dump(simulation_data, f)

    
# Write the stations to a JSON file using the StationEncoder
with open("stations.json", "w") as f:
    json.dump(stations, f, cls=StationEncoder)

