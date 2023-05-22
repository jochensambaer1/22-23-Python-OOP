interface VeloData {
    properties: {
        [key: string]: number | string;
      OBJECTID: number;
      Objecttype: string;
      Type_velo: string;
      Ligging: string;
      Straatnaam: string;
      Huisnummer: string;
      Aanvulling: string;
      District: string;
      Postcode: string;
      Objectcode: string;
      Gebruik: string;
      Aantal_plaatsen: number;
      Naam: string;
    };
  }

  
  
  // Function to create and populate the HTML table
  function createTable(data: VeloData[]) {
    const table = document.getElementById("myTable");
  
    if (table !== null) {
      // Create table headers
      const headers = Object.keys(data[0].properties);
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
          cell.textContent = object.properties[header].toString();
          row.appendChild(cell);
        });
        table.appendChild(row);
      });
    } else {
      console.log("Table element not found.");
    }
  }
  
  // Read and parse the JSON file
  async function loadJSON() {
    try {
      const response = await fetch("velo.geojson");
      const json = await response.json();
      const features = json.features;
      const veloData: VeloData[] = features.map((feature: any) => ({
        properties: feature.properties,
      }));
      createTable(veloData);
    } catch (error) {
      console.log("Error loading JSON file:", error);
    }
  }
  
  // Load JSON and create the table
  loadJSON();
  
  export {}; // Add an empty export statement to make it a module
  