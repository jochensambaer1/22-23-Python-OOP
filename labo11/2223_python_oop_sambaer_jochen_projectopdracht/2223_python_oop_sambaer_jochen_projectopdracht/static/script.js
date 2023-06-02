const nameForm = document.getElementById("nameForm");
const nameList = document.getElementById("nameList");

nameForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const inputId = document.getElementById("inputId").value;

  if (!isNaN(inputId) && inputId > 0) {
    window.location.href = `/station/${inputId}`;
  } else {
    alert("Please enter a valid ID.");
  }
});

fetch("/static/bikes.geojson")
  .then((response) => response.json())
  .then((bikeData) => {
    const bikeTableBody = document.getElementById("bikeTableBody");
    bikeData.features.forEach(({ properties, geometry }) => {
      const { id, state, borrow_time } = properties;
      const latitude = geometry.coordinates[1];
      const longitude = geometry.coordinates[0];
      const location = ""; // Update this with the actual location if available
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
  .catch((error) => console.error("Error fetching bike data:", error));

fetch("/static/simulation.geojson")
  .then((response) => response.json())
  .then((simulationData) => {
    const simulationTableBody = document.getElementById("simulationTableBody");
    simulationData.forEach(({ action, user, bike_id, station }) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${action}</td>
        <td>${user}</td>
        <td>${bike_id || ""}</td>
        <td>${station || ""}</td>
      `;
      simulationTableBody.appendChild(row);
    });
  })
  .catch((error) => console.error("Error fetching simulation data:", error));

fetch("/static/velo.geojson")
  .then((response) => response.json())
  .then((stationData) => {
    const stationTableBody = document.getElementById("stationTableBody");
    stationData.features.forEach(({ properties, geometry }) => {
      const {
        OBJECTID,
        Objecttype,
        Type_velo,
        Ligging,
        Straatnaam,
        Huisnummer,
        Aanvulling,
        District,
        Postcode,
        Objectcode,
        Gebruik,
        Aantal_plaatsen,
        Naam,
      } = properties;
      const latitude = geometry.coordinates[1];
      const longitude = geometry.coordinates[0];

      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${OBJECTID}</td>
        <td>${Objecttype}</td>
        <td>${Type_velo}</td>
        <td>${Ligging}</td>
        <td>${Straatnaam}</td>
        <td>${Huisnummer}</td>
        <td>${Aanvulling}</td>
        <td>${District}</td>
        <td>${Postcode}</td>
        <td>${Objectcode}</td>
        <td>${Gebruik}</td>
        <td>${Aantal_plaatsen}</td>
        <td>${Naam}</td>
        <td>${latitude}</td>
        <td>${longitude}</td>
      `;
      stationTableBody.appendChild(row);
    });
  })
  .catch((error) => console.error("Error fetching station data:", error));

fetch("/static/name.geojson")
  .then((response) => response.json())
  .then((userData) => {
    const userTableBody = document.getElementById("userTableBody");
    userData.forEach(({ id, first_name, last_name, full_name, time_biking_minutes, time_biking_hours, total_time_biking_minutes, saldo }) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${id}</td>
        <td>${first_name}</td>
        <td>${last_name}</td>
        <td>${full_name}</td>
        <td>${time_biking_minutes}</td>
        <td>${time_biking_hours}</td>
        <td>${total_time_biking_minutes}</td>
        <td>${saldo}</td>
      `;
      userTableBody.appendChild(row);
    });
  })
  .catch((error) => console.error("Error fetching user data:", error));

fetch("/static/Transporters.geojson")
  .then((response) => response.json())
  .then((transporterData) => {
    const transporterTableBody = document.getElementById("transporterTableBody");
    transporterData.forEach(({ id, first_name, last_name, full_name, time_biking_minutes, time_biking_hours, total_time_biking_minutes, saldo }) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${id}</td>
        <td>${first_name}</td>
        <td>${last_name}</td>
        <td>${full_name}</td>
        <td>${time_biking_minutes}</td>
        <td>${time_biking_hours}</td>
        <td>${total_time_biking_minutes}</td>
        <td>${saldo}</td>
      `;
      transporterTableBody.appendChild(row);
    });
  })
  .catch((error) => console.error("Error fetching transporter data:", error));
