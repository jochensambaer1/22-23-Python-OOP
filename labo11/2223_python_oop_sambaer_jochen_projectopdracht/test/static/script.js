// Get the form and name list elements
const nameForm = document.getElementById('nameForm');
const nameList = document.getElementById('nameList');


// Fetch bikes.geojson and populate the bike table
fetch("/static/bikes.geojson")
  .then((response) => response.json())
  .then((bikeData) => {
    const bikeTableBody = document.getElementById('bikeTableBody');
    bikeData.features.forEach((feature) => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${feature.properties.id}</td>
        <td>${feature.properties.state}</td>
        <td>${feature.properties.borrow_time || ''}</td>
        <td>${feature.geometry.coordinates[1]}</td>
        <td>${feature.geometry.coordinates[0]}</td>
      `;
      bikeTableBody.appendChild(row);
    });
  })
  // Fetch velo.geojson and populate the station table
  .catch((error) => console.log(error));
  fetch("/static/velo.geojson")
  .then((response) => response.json())
  .then((stationData) => {
    const stationTableBody = document.getElementById('stationTableBody');
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
    const userTableBody = document.getElementById('userTableBody');
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
.then((userData) => {
  const BikeTransporterTableBody = document.getElementById('BikeTransporterTableBody');
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
    BikeTransporterTableBody.appendChild(row);
  });
})
.catch((error) => console.log(error));

// Function to fetch the names JSON file and generate a random name
async function generateRandomNames(count) {
  try {
    console.log('Fetching names...');
    const response = await fetch('/static/names.json');
    console.log('Got names!');
    const data = await response.json();

    const randomNames = [];
    for (let i = 0; i < count; i++) {
      const randomFirstNameIndex = Math.floor(Math.random() * data.first_name.length);
      const randomFirstName = data.first_name[randomFirstNameIndex];

      const randomLastNameIndex = Math.floor(Math.random() * data.last_name.length);
      const randomLastName = data.last_name[randomLastNameIndex];

      const fullName = randomFirstName + ' ' + randomLastName;
      randomNames.push(fullName);
    }

    // Create a data blob with the random names
    const dataBlob = new Blob([JSON.stringify(randomNames)], { type: 'application/json' });

    // Create a download link
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(dataBlob);
    downloadLink.download = 'random_names.json';

    // Append the download link to the document body and trigger the click event
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  } catch (error) {
    console.error('Error fetching names: ' + error);
    throw new Error('Error fetching names: ' + error);
  }
}

