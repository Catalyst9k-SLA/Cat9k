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

arguments = sys.argv


print("room ID :" + roomID_SoftwareProject)

resp = post_message("Configuration has changed. Changes are : \n"
                    " " + str(arguments), roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

