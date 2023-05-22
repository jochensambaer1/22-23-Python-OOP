// Function to create and populate the HTML table
function createTable(data: any[]) {
    const table = document.getElementById("myTable");
  
    // Create table headers
    const headers = Object.keys(data[0]);
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
  function loadJSON(callback: (data: any[]) => void) {
    const file = new XMLHttpRequest();
    file.overrideMimeType("application/json");
    file.open("GET", "data.json", true);
    file.onreadystatechange = function () {
      if (file.readyState === 4 && file.status == 200) {
        callback(JSON.parse(file.responseText));
      }
    };
    file.send(null);
  }
  
  // Load JSON and create the table
  loadJSON(function (data) {
    createTable(data);
  });
  