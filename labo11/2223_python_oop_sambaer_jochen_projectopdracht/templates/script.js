function runScript() {
    // create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // set the HTTP method and URL
    xhr.open("POST", "/run_script", true);

    // set the response type to text
    xhr.responseType = "text";

    // set the onload callback function
    xhr.onload = function() {
      // check if the request was successful
      if (xhr.status === 200) {
        // display the response from the server
        alert(xhr.responseText);
      } else {
        // display an error message
        alert("Error: " + xhr.statusText);
      }
    };

    // set the request header to indicate JSON content
    xhr.setRequestHeader("Content-Type", "application/json");

    // create a JSON payload with any data to pass to the script
    var payload = JSON.stringify({
      // add any data as key-value pairs
      "param1": "value1",
      "param2": "value2"
    });

    // send the request with the JSON payload
    xhr.send(payload);
  }
  ```
