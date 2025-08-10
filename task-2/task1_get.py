import requests

# Task 1 – GET Request with Query Parameters
name = "Bami"
url = "https://api.agify.io"
params = {"name": name}

# Send GET request with query parameters
response = requests.get(url, params=params)

# Raise an exception if the request was not successful
response.raise_for_status()

# Parse the response as JSON
data = response.json()


# print(data)

# Print the result
print(f"Hello {data['name']}! Agify says you're {data['age']} years old… ")
print(f"but after debugging all day you feel like 80 💀☠️")

