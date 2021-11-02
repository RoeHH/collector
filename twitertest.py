import http.client
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

headers = {
    'Authentication': "Basic "
    }

conn.request("GET", "/market/v2/get-quotes?region=US&symbols=CHFUSD=X", headers=headers) #regular market price isch spanened isch usd to chf bzw 1.1 us  * 0.91(regmp) = 1 fr

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))