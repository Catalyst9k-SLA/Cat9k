import sys
sys.path.insert(1, '../Variables/')
from SparkVariables import *
from SparkFunctions import *

#postMessage("Y2lzY29zcGFyazovL3VzL1JPT00vM2IzYjUyOTAtMTMxMy0xMWU4LWJlY2EtN2RlZGYwNWYxOTFh", "test from python")

print("room ID :" + roomID_SoftwareProject)

resp = post_message("Test - from the Cat9k", roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

