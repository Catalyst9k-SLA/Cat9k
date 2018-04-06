import cli
# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)


# intf= sys.argv[1:]
# intf = ''.join(intf[0])

from SparkFunctions import *
from SparkVariables import *


def save_config():

    print "\n\n *** Printing show cmd with 'execute' function *** \n\n"
    output = cli.execute('copy startup-config ftp://Administrator:C1sco123@10.9.15.3/Temp/SoftwareProjectSLA/config_backup.cfg')
    print (output)

    post_message_markdown("Configuration has been saved !", roomID_SoftwareProject, bearer_Bot)

if __name__ == "__main__":
    save_config()
