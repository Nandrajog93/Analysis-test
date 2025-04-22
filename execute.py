
from influxdb_client import InfluxDBClient


bucket = "hepingbb"
org = "my-org"
token = "mytoken"
url = "http://localhost:8086"



query = f'''
from(bucket: "{bucket}")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "sensor_metrics")
'''
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()
tables = query_api.query(query)

for table in tables:
    for row in table.records:
        print(f"{row.get_time()} | {row.get_field()} = {row.get_value()}")


        