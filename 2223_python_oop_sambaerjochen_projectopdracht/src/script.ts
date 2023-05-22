// Read and parse the JSON file
async function loadJSON() {
  try {
    // Load the JSON file
    console.log("Loading JSON file...");
    const response = await fetch("velo.geojson");
    console.log("JSON file loaded.");
    const json = await response.json();
    const features = json.features;

    // Create the table
    console.log("Creating table...");
    const veloData: VeloData[] = features.map((feature: any) => ({
      properties: feature.properties,
    }));
    createTable(veloData);
    console.log("Table created.");
  } catch (error) {
    console.log("Error loading JSON file:", error);
  }
}