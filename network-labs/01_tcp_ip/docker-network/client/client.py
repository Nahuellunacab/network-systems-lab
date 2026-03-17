import requests
import time

while True:
    try:
        response = requests.get("http://api:8000")
        print("Response:", response.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(5)