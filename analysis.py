from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import random
import numpy as np



bucket = "hepingbb"
org = "my-org"
token = "mytoken"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

for i in range(10000):  # Run for 100 iterations
    voltage = round(random.uniform(210.0, 240.0), 2)
    temp = round(random.uniform(30.0, 50.0), 1)

    point = (
        Point("sensor_metrics")
        .tag("device", "battery-01")
        .field("voltage", voltage)
        .field("temperature", temp)
    )

    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Written -> Voltage: {voltage}, Temp: {temp}")

    #time.sleep(10)




