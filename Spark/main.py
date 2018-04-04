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

#postMessage("Y2lzY29zcGFyazovL3VzL1JPT00vM2IzYjUyOTAtMTMxMy0xMWU4LWJlY2EtN2RlZGYwNWYxOTFh", "test from python")

print("room ID :" + roomID_SoftwareProject)

resp = post_message("Test - from the Cat9k", roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

