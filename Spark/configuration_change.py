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
print("arguments =" + str(arguments))


date = ""
date += str(arguments[1]) + " " + str(arguments[2])
date = date[1:]

time = ""
time += str(arguments[3])
time = time[0:8]

hostname = ""
hostname += str(arguments[13])

print("room ID :" + roomID_SoftwareProject)

resp = post_message_markdown("# Configuration has changed ! \n", roomID_SoftwareProject, bearer_Bot)
resp = post_message_markdown("* **Date** : " + date + "\n"
                             "* **Time** : " + time, roomID_SoftwareProject, bearer_Bot)
resp = post_message_markdown("> Changes were made by **" + str(arguments[9]) + "** using **" + str(arguments[7]) + "**" + " on device **" + hostname +"**", roomID_SoftwareProject, bearer_Bot)

resp = post_message_markdown()

print("resp = " + resp.text)



