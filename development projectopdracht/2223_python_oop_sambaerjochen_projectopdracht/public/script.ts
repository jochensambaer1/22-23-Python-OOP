
// Create and populate the HTML table
function createTable(data: VeloData[]) {
  const table = document.getElementById("myTable");
  const headers = Object.keys(data[0]);
  
  // Create table headers
  const headerRow = document.createElement("tr");
  headers.forEach((header) => {
    const th = document.createElement("th");
    th.textContent = header;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  // Populate table rows
  data.forEach((object) => {
    const row = document.createElement("tr");
    headers.forEach((header) => {
      const cell = document.createElement("td");
      cell.textContent = object[header];
      row.appendChild(cell);
    });
    table.appendChild(row);
  });
}

// Read and parse the JSON file
async function loadJSON() {
  try {
    const response = await fetch("velo.geojson");
    const json = await response.json();
    const features = json.features;
    const veloData: VeloData[] = features.map((feature: any) => feature.properties);
    createTable(veloData);
  } catch (error) {
    console.log("Error loading JSON file:", error);
  }
}

// Load JSON and create the table
loadJSON();
