import requests, json, time

for each in range(10):
    requests.post("http://localhost:5000/recieve_events",json={'K':each})
    time.sleep(1)