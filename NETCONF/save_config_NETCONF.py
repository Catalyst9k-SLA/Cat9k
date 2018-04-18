#!/usr/bin/env python

# import the ncclient library
from ncclient import manager
import sys
import xml.dom.minidom

# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
dirSpark = dirParent + "/Spark"
sys.path.insert(0, dirVariable)
sys.path.insert(1, dirSpark)


from SparkFunctions import *
from SparkVariables import *


# create a main() method
def save_config_NETCONF(usernameTFTP, passwordTFTP, ipTFTP, path, filename):
    """
    Main method that retrieves the hostname from config via NETCONF.
    """
    with manager.connect(host=switch_ip, port=switch_ssh_port, username=switch_username,
                         password=switch_password, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        m.copy_config("running", "ftp://" + usernameTFTP + ":" + passwordTFTP + "@" + ipTFTP + path + filename + "_NETCONF.cfg")

        post_message_markdown("# Kitty save config NETCONF \n"
                              "Configuration has been saved successfully! Configuration has been saved using **ftp**.\n"
                              "> " + usernameTFTP + "@" + ipTFTP + path + filename + ".cfg", roomID_SoftwareProject,
                              bearer_Bot)

if __name__ == '__main__':
    save_config_NETCONF(username_TFTP, password_TFTP, ip_TFTP, path_TFTP, filename_TFTP)