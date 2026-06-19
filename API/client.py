import requests, logging
logging.basicConfig(level=logging.INFO)
resp = requests.get("http://localhost:8001/data")
logging.info(f" {resp.status_code} – {resp.json()}")