from datetime import datetime
from random import uniform
import requests
import json
import time

while True:
    load = {
        'temperature': round(uniform(-20, 50),2),
        'humidity': round(uniform(-20, 100),2),
        'luminosity': round(uniform(0, 150),2),
        'date': datetime.now().strftime("%Y-%m-%d"),
        'time': datetime.now().strftime("%H:%M:%S"),
    }

    print(load)

    # PUT API
    requests.post(url=f'http://127.0.0.1:8080/data/', json=load)
    time.sleep(10)