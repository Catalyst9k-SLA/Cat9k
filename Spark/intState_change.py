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

arguments = sys.argv

interface = str(arguments[6])
state = str(arguments[10]) + " " + str(arguments[11])
hostname = str(arguments[12])

print("room ID :" + roomID_SoftwareProject)

resp = post_message("Interface " + interface +" state has changed on device: " + hostname + "\n" +
                    "New state is : " + state + "\n", roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

