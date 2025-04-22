from flask import Flask, render_template, Response
from influxdb_client import InfluxDBClient
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd
import io
import base64

app = Flask(__name__)

bucket = "hepingbb"
org = "my-org"
token = "mytoken"
url = "http://localhost:8086"

def fetch_data():
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -1h)
      |> filter(fn: (r) => r._measurement == "sensor_metrics")
    '''
    client = InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()
    tables = query_api.query(query)

    rows = []
    for table in tables:
        for row in table.records:
            rows.append(row.values)
    return pd.DataFrame(rows)

@app.route('/')
def index():
    df = fetch_data()

    x = pd.to_datetime(df['_time'])
    y = df['_value']

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Sensor Metrics")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    img = io.BytesIO()
    plt.tight_layout()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('index.html', plot_url=plot_url)
    #return render_template('index.html', plot_url=plot_url)

