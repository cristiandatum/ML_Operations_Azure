import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "Inputs": {
        "data":
        [
          {
            "age": "55",
            "job": "technician",
            "marital": "married",
            "education": "high.school",
            "default": "no",
            "housing": "no",
            "loan": "no",
            "contact": "cellular",
            "month": "may",
            "day_of_week": "mon",
            "duration": "300",
            "campaign": "1",
            "pdays": "999",
            "previous": "1",
            "poutcome": "failure",
            "emp.var.rate": "-1.8",
            "cons.price.idx": "92.893",
            "cons.conf.idx": "-46.2",
            "euribor3m": "1.299",
            "nr.employed": "5099.1"
          },
          {
            "age": "43",
            "job": "blue-collar",
            "marital": "single",
            "education": "basic.9y",
            "default": "no",
            "housing": "yes",
            "loan": "no",
            "contact": "cellular",
            "month": "jul",
            "day_of_week": "thu",
            "duration": "982",
            "campaign": "1",
            "pdays": "999",
            "previous": "0",
            "poutcome": "nonexistent",
            "emp.var.rate": "1.4",
            "cons.price.idx": "93.918",
            "cons.conf.idx": "-42.7",
            "euribor3m": "4.963",
            "nr.employed": "5288.1"
          },
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}

body = str.encode(json.dumps(data))

url = 'http://b240a300-1c41-498a-b060-15713ad5725c.westeurope.azurecontainer.io/score'
api_key = 'fIL1AIb9AGMxH4DdDz5aG4WGbjyMHXVN' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
