import requests


url = "https://httpbin.org/image/png"
filename = "downloaded_image.png"


response = requests.get(url)
response.raise_for_status()
with open(filename, "wb") as file:
    file.write(response.content)


print(f"Image downloaded! 🖼️\nOpen '{filename}' to reveal… "
      "the world's least interesting stock photo. 📸😆")