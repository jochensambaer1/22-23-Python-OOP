class fietsstations {
  constructor(id, type, bikeType, location, street, houseNumber, addition, district, postalCode, objectCode, usage, numberOfPlaces, name, longitude, latitude) {
    this.id = id;
    this.type = type;
    this.bikeType = bikeType;
    this.location = location;
    this.street = street;
    this.houseNumber = houseNumber;
    this.addition = addition;
    this.district = district;
    this.postalCode = postalCode;
    this.objectCode = objectCode;
    this.usage = usage;
    this.numberOfPlaces = numberOfPlaces;
    this.name = name;
    this.longitude = longitude;
    this.latitude = latitude;
  }
}
console.log("fietsstations: " + fietsstations);

let fietsstations = [];

for (let i = 0; i < velo.features.length; i++) {
  let feature = velo.features[i];
  let station = new Fietsstation(
    feature.properties.OBJECTID,
    feature.properties.Objecttype,
    feature.properties.Type_velo,
    feature.properties.Ligging,
    feature.properties.Straatnaam,
    feature.properties.Huisnummer,
    feature.properties.Aanvulling,
    feature.properties.District,
    feature.properties.Postcode,
    feature.properties.Objectcode,
    feature.properties.Gebruik,
    feature.properties.Aantal_plaatsen,
    feature.properties.Naam,
    feature.geometry.coordinates[0],
    feature.geometry.coordinates[1]
  );
  console.log("station: " + station);
  fietsstations.push(station);
}

console.log("fietsstations: " + fietsstations);