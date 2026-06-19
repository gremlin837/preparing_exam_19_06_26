import requests

BASE = "http://localhost:5000"

# POST — передаём value как query-параметр
resp = requests.post(f"{BASE}/add?value=hello")
print(resp.status_code, resp.json())

# GET
data = requests.get(f"{BASE}/get").json()
print(data)