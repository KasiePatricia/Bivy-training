import requests

# Task 2 – POST Request with JSON Data
url = "https://httpbin.org/post"

payload = {
        "username": "bami",
        "email": "bami@example.com"
    }

response = requests.post(url, json=payload)
response.raise_for_status()

# print(response.json())

print(f"POST complete ✅\nServer says: \"Welcome {payload['email']}!\" ")
print(f"Warning: Your password is still '123456'… HR is already crying. 😭🔐")