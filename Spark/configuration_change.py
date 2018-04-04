# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)

from argparse import ArgumentParser
from SparkVariables import *
from SparkFunctions import *


parser = ArgumentParser("Spark Check In")
parser.add_argument(
    "-w", "--who", help="Spark Authentication Token", required=True
)

args = parser.parse_args()
who = args.who

print("room ID :" + roomID_SoftwareProject)

resp = post_message("Configuration has changed. Made by " + who, roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

