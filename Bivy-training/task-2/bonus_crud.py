import requests


base_url = "https://jsonplaceholder.typicode.com/posts"

# GET
get_res = requests.get(base_url)
print("READ: First post title on HTTP request ->", get_res.json()[0]['title'])


# POST
post_data = {"title": "API Testing", "body": "This is a test post", "userId": 1}
post_res = requests.post(base_url, json=post_data)
print("CREATE: New post ID: ", post_res.json()['id'])


# PUT
put_data = {"title": "Updated Post", "body": "This is an updated api testing post", "userId": 1}
put_res = requests.put(f"{base_url}/1", json=put_data)
print("UPDATE: Updated post ID: ", put_res.json()['id'])


# DELETE
del_res = requests.delete(f"{base_url}/1")
print("DELETE status code:", del_res.status_code)