from subprocess import check_output

@app.route("/run_script", methods=["POST"])
def run_script():
    # get the JSON payload from the request
    data = request.json

    # extract any parameters from the payload
    param1 = data.get("param1")
    param2 = data.get("param2")

    # execute the Python script with the parameters
    output = check_output(["python", "my_script.py", param1, param2])

    # write the output to a file
    with open("output.txt", "w") as f:
        f.write(output.decode())

    # return a success message
    return "Script executed successfully"
