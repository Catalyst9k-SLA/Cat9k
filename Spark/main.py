# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print("currentdir = " + currentdir)
dirParent = os.path.dirname(currentdir)
print("dirParent =" + dirParent)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)


from SparkVariables import *
from SparkFunctions import *


# resp = post_message_markdown(" **Test** - from the Cat9k \n"
                            # "> **test**", roomID_SoftwareProject, bearer_Bot)


