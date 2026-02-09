import requests

url = "http://127.0.0.1:1000/users"
data = {"name": "Riya", "age": 20}

r = requests.post(url, json=data)

print("Status:", r.status_code)
print("Response:", r.json())
