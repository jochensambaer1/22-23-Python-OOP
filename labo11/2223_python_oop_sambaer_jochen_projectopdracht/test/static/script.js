// Get the form and name list elements
const nameForm = document.getElementById("nameForm");
const nameList = document.getElementById("nameList");

fetch("/static/bikes.geojson")
  .then((response) => response.json())
  .then((bikeData) => {
    const bikeTableBody = document.getElementById("bikeTableBody");
    bikeData.features.forEach((feature) => {
      const properties = JSON.parse(feature); // Parse the feature string as JSON
      const id = properties.id;
      const state = properties.state;
      const borrow_time = properties.borrow_time;
      const latitude = feature.geometry.coordinates[1];
      const longitude = feature.geometry.coordinates[0];
      const location = properties.location;
      const last_state_change = new Date().toISOString();

      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${id}</td>
        <td>${state}</td>
        <td>${borrow_time}</td>
        <td>${latitude}</td>
        <td>${longitude}</td>
        <td>${location}</td>
        <td>${last_state_change}</td>
      `;
      bikeTableBody.appendChild(row);
    });
  })
  .catch((error) => console.log(error));



  // Fetch velo.geojson and populate the station table
  
fetch("/static/velo.geojson")
  .then((response) => response.json())
  .then((stationData) => {
    const stationTableBody = document.getElementById("stationTableBody");
    stationData.features.forEach((feature) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${feature.properties.OBJECTID}</td>
        <td>${feature.properties.Objecttype}</td>
        <td>${feature.properties.Type_velo}</td>
        <td>${feature.properties.Ligging}</td>
        <td>${feature.properties.Straatnaam}</td>
        <td>${feature.properties.Huisnummer}</td>
        <td>${feature.properties.Aanvulling}</td>
        <td>${feature.properties.District}</td>
        <td>${feature.properties.Postcode}</td>
        <td>${feature.properties.Objectcode}</td>
        <td>${feature.properties.Gebruik}</td>
        <td>${feature.properties.Aantal_plaatsen}</td>
        <td>${feature.properties.Naam}</td>
        <td>${feature.geometry.coordinates[1]}</td>
        <td>${feature.geometry.coordinates[0]}</td>
      `;
      stationTableBody.appendChild(row);
    });
  })
  .catch((error) => console.log(error));

fetch("/static/name.geojson")
  .then((response) => response.json())
  .then((userData) => {
    const userTableBody = document.getElementById("userTableBody");
    userData.forEach((user) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${user.id}</td>
        <td>${user.first_name}</td>
        <td>${user.last_name}</td>
        <td>${user.full_name}</td>
        <td>${user.time_biking_minutes}</td>
        <td>${user.time_biking_hours}</td>
        <td>${user.total_time_biking_minutes}</td>
        <td>${user.saldo}</td>
      `;
      userTableBody.appendChild(row);
    });
  })
  .catch((error) => console.log(error));

// Fetch transporters.geojson and populate the transporters table


  fetch("/static/Transporters.geojson")
  .then((response) => response.json())
  .then((BikeTransporter) => {
    const BikeTransporterTableBody = document.getElementById("BikeTransporterTableBody");
    BikeTransporter.forEach((BikeTransporter) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${BikeTransporter.id}</td>
        <td>${BikeTransporter.first_name}</td>
        <td>${BikeTransporter.last_name}</td>
        <td>${BikeTransporter.full_name}</td>
        <td>${BikeTransporter.time_biking_minutes}</td>
        <td>${BikeTransporter.time_biking_hours}</td>
        <td>${BikeTransporter.total_time_biking_minutes}</td>
        <td>${BikeTransporter.saldo}</td>
      `;
      BikeTransporterTableBody.appendChild(row);
    });
  })
  .catch((error) => console.log(error));

  fetch("/static/simulation.geojson")
  .then((response) => response.json())
  .then((simData) => {
    const simTableBody = document.getElementById("simTableBody");
    simData.features.forEach((feature) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${feature.properties.action}</td>
        <td>${feature.properties.user}</td>
        <td>${feature.properties.bike_id}</td>
        <td>${feature.geometry.station}</td>
        
      `;
      simTableBody.appendChild(row);
    });
  })