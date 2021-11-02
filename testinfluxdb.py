from datetime import datetime
import os
from dotenv import load_dotenv


from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()

token = os.getenv('influxKey')
org = "influxdb@roeh.ch"
bucket = "test"

with InfluxDBClient(url="https://europe-west1-1.gcp.cloud2.influxdata.com", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    data = "mem,host=host1 used_percent=83.43234543"
    write_api.write(bucket, org, data)

