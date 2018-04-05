# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)


from SparkVariables import *
from SparkFunctions import *

print("room ID :" + roomID_SoftwareProject)

resp = post_message_markdown(" > Test - from the Cat9k", roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

