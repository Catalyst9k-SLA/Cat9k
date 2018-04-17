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
from kitty_help import *
from save_config import *

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

    # removing the bot name from the message and the space after the bot name
    message = message[len(botName_Kitty)+1:]

    # Ignore if the message is coming from the bot itself (avoid infinite posting loops)
    if person_id == peopleID_Kitty:
        return "from Kitty"
    else:
        # post_message("You posted a message !", roomID_SoftwareProject, bearer_Bot)

        if message == "Salut":
            post_message("Salut " + "<@personEmail:str(person_email)>", roomID_SoftwareProject, bearer_Bot)
            if person_email == "aengelen@cisco.com":
                post_message("Je préfère l'autre Antoine !")
            elif person_email == "anorsoni@cisco.com":
                post_message("C'est mon Antoine préféré !")
        elif message == "help":
            kittyHelp()
        elif message == "save config":
            # def save_config(usernameTFTP, passwordTFTP, ipTFTP, path, filename):
            save_config(username_TFTP, password_TFTP, ip_TFTP, path_TFTP, filename_TFTP)




    return "OK"

# run the application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)