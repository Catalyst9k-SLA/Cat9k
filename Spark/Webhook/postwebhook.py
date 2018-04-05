# SOURCE : https://github.com/CiscoDevNet/spark-webhooks-sample/blob/master/postwebhook.py

# import the requests and json library so we can use it to make REST calls
import requests, json
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "../Variables"
sys.path.insert(0, dirVariable)

from SparkVariables import *
from Spark.SparkFunctions import *


# the main function
def main():
    # login to developer.ciscospark.com and copy your access token here
    # Never hard-code access token in production environment
    token = "Bearer " + bearer_Bot

    # add authorization to the header
    header = {"Authorization": "%s" % token, "content-type": "application/json"}

    # disable warnings about using certificate verification
    requests.packages.urllib3.disable_warnings()

    # create request url
    post_message_url = "https://api.ciscospark.com/v1/webhooks"

    # create request body
    payload = {
        "resource": "messages",
        "event": "created",
        #"filter": "roomId=" + roomID_SoftwareProject,
        "filter": "mentionedPeople=me",
        "targetUrl": webhook_URL,
        "name": webhook_name
    }

    # send the POST request resource and do not verify SSL certificate for simplicity of this example
    api_response = requests.post(post_message_url, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    # print the status code
    print(response_status)


# run the function
main()