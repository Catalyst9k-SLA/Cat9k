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

def kittyHelp():
    post_message_markdown("# Kitty Help \n"
                          "Usage : @" + botName_Kitty + " instruction1 instruction2 ... \n"
                          "Here is what I can do : \n"
                          "* **help** : print those inscructions\n"
                          "* **Salut** : greetings (in French !)\n"
                          "* **save config** : backup the configturation on the TFTP server\n"
                          "* **last config** : information about the last config changes", roomID_SoftwareProject, bearer_Bot)
    return "OK"