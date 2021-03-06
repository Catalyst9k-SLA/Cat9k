import cli
# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)


from SparkFunctions import *
from SparkVariables import *


def save_config(usernameTFTP, passwordTFTP, ipTFTP, path, filename):

    print "\n\n *** Printing show cmd with 'execute' function *** \n\n"
    output = cli.execute("copy startup-config ftp://" + usernameTFTP + ":" + passwordTFTP + "@" + ipTFTP + path + filename + ".cfg")
    print (output)

    post_message_markdown("# Kitty save config \n"
                          "Configuration has been saved successfully! Configuration has been saved using **ftp**.\n"
                          "> " + usernameTFTP + "@" + ipTFTP + path + filename + ".cfg", roomID_SoftwareProject, bearer_Bot)

if __name__ == "__main__":
    save_config(username_TFTP, password_TFTP, ip_TFTP, path_TFTP, filename_TFTP)

