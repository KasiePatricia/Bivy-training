import requests


url = "https://httpbin.org/post"
filename = "downloaded_image.png"

with open(filename, "rb") as f:
    files = {"file": (filename, f, "image/png")}
    response = requests.post(url, files=files)
    response.raise_for_status()

    
print(f"File uploaded :outbox_tray:\nhttpbin is now the proud owner "
    f"of my masterpiece: {filename}  🎨 (Expect it to sell on eBay for $11.53.) ")