import requests
response = requests.get("https://api.catboys.com/ping")
print(response.json())
