import requests
import random
import time

API_URL = "http://localhost:5000/api/sensor-data"

plants = ["fern_1", "cactus_1", "monstera_1"]

while True:
    data = {
        "plant_id": random.choice(plants),
        "soil_moisture": random.randint(20, 80),
        "light": random.randint(100, 800),
        "temperature": random.randint(18, 30)
    }

    requests.post(API_URL, json=data)
    print("Sent:", data)

    time.sleep(5)