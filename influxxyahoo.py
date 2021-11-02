import http.client
import os
from dotenv import load_dotenv
import json



from time import time, sleep

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()




token = os.getenv('influxKey')
org = "influxdb@roeh.ch"
bucket = "test"




conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': os.getenv('yahooKey')
    }

while True:
    sleep(60 - time() % 60)
    conn.request("GET", "/market/v2/get-quotes?region=US&symbols=CHFUSD=X", headers=headers) #regular market price isch spanened isch usd to chf bzw 1.1 us  * 0.91(regmp) = 1 fr

    res = conn.getresponse()
    data = res.read()
    dataJson = json.loads(data)

    print(dataJson["quoteResponse"]["result"][0]["regularMarketPrice"])


    with InfluxDBClient(url="https://europe-west1-1.gcp.cloud2.influxdata.com", token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        data = "usdChf,host=host1 exchangerate=" + str(dataJson["quoteResponse"]["result"][0]["regularMarketPrice"])
        write_api.write(bucket, org, data)
