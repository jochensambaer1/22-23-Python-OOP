import requests

url = "https://lexica.art/api/v1/search"
params = {"q": "apples"}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.content.decode()

    # Write the response data to a file
    with open("output.txt", "w") as f:
        f.write(data)
else:
    print(f"API call failed with status code {response.status_code}")
