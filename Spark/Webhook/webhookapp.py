# import Flask
from flask import Flask, request
# import  custom-made modules
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent_Spark = os.path.dirname(currentdir)
dirParent_Variables = os.path.dirname(os.path.dirname(currentdir))
dirVariable = dirParent_Variables + "/Variables"
sys.path.insert(1, dirVariable)
sys.path.insert(2, dirParent_Spark)

from argparse import ArgumentParser
from SparkVariables import *
from SparkFunctions import *

# Create an instance of Flask
app = Flask(__name__)

# Index page will trigger index() function
@app.route('/')
def index():
    return 'Hello World'

# Webhook page will trigger webhooks() function
@app.route("/webhook", methods=['POST'])
def webhooks():

    # Get the json data
    json = request.json

    # parse the message id, person id, person email, and room id
    message_id = json["data"]["id"]
    person_id = json["data"]["personId"]
    person_email = json["data"]["personEmail"]
    room_id = json["data"]["roomId"]

    # convert the message id into readable text
    message = get_message(message_id, bearer_Bot)


    if person_id == peopleID_Kitty:
        return "OK"
    else:
        post_message("You posted a message !", roomID_SoftwareProject, bearer_Bot)

        if message == "Kitty Salut":
            post_message("Salut " + str(person_email), roomID_SoftwareProject, bearer_Bot)

    return "OK"

# run the application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)