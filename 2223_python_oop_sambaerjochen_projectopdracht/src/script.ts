async function loadJSON() {
    try {
      // Load the JSON file
      console.log("Loading JSON file...");
      const response = await fetch("velo.geojson");
      console.log("JSON file loaded.");
      const json = await response.json();
      // Process the JSON data
      const features = json.features;
      const veloData = features.map((feature) => ({
        properties: feature.properties,
      }));
      createTable(veloData);
      console.log("Table created.");
    } catch (error) {
      console.log("Error loading JSON file:", error);
    }
  }
  const fs = require('fs');
try {
  const jsonString = fs.readFileSync('./data.json', 'utf8');
  const data = JSON.parse(jsonString);
  console.log(data);
} catch (error) {
  console.log("Error reading JSON file:", error);
}
const fs = require('fs');
fs.readFile('./data.json', 'utf8', (err, jsonString) => {
  if (err) {
    console.log("Error reading JSON file:", err);
    return;
  }
  try {
    const data = JSON.parse(jsonString);
    console.log(data);
  } catch (error) {
    console.log("Error parsing JSON file:", error);
  }
});
function readTextFile(file, callback) {
    const rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4 && rawFile.status == "200") {
        callback(rawFile.responseText);
      }
    }
    rawFile.send(null);
  }
  
  // Usage:
  readTextFile("/path/to/data.json", function(text){
    const data = JSON.parse(text);
    console.log(data);
  });
  