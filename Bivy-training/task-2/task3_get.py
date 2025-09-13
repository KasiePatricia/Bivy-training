import requests

# Task 3 – Custom Headers
url = "https://httpbin.org/headers"

response = requests.get(url, headers={
    "Authorization": "Bearer pizzatoken",
    "X-App-Version": "42.0"
})

response.raise_for_status()
received_headers = response.json()["headers"]


print("My request is so fancy it wore a tuxedo. 🤵")
print("Here are my headers:", received_headers)