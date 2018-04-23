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

with manager.connect(host=switch_ip, port=switch_netconf_port, username=switch_username,
                         password=switch_password, hostkey_verify=False,
                         device_params={'name': 'csr'},
                         allow_agent=False, look_for_keys=False) as m:


    config = m.get_config("running")

    config_pretty = xml.dom.minidom.parseString(config.xml).toprettyxml()

    print(config_pretty)


    

    with open("./SavedConfigs/%s.xml" % "config_backup_SLA_NETCONF", 'w') as f:
         f.write(config_pretty)

    # print(result)

