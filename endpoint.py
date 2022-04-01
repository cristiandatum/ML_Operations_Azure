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
                "age": "0",
                "job": "example_value",
                "marital": "example_value",
                "education": "example_value",
                "default": "example_value",
                "housing": "example_value",
                "loan": "example_value",
                "contact": "example_value",
                "month": "example_value",
                "day_of_week": "example_value",
                "duration": "0",
                "campaign": "0",
                "pdays": "0",
                "previous": "0",
                "poutcome": "example_value",
                "emp.var.rate": "0",
                "cons.price.idx": "0",
                "cons.conf.idx": "0",
                "euribor3m": "0.0",
                "nr.employed": "0"
            },
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}

body = str.encode(json.dumps(data))

# URL for the web service
scoring_uri = 'http://7386b71a-601c-48fb-b109-c47416fa192a.westeurope.azurecontainer.io/score'

# If the service is authenticated, set the key or token
api_key = "7BhaMreasi8hCGNhUHRqDccnZHHyRpl1"

headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(scoring_uri, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))