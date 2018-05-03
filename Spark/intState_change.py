# Importing the variable file in the dir Variable
import sys
import os
import inspect


####
# *Apr 24 10:37:49.492: %ILPOWER-7-DETECT: Interface Gi1/0/3: Power Device detected: IEEE PD
# *Apr 24 10:37:50.493: %ILPOWER-5-POWER_GRANTED: Interface Gi1/0/3: Power granted
# *Apr 24 10:37:53.493: %ILPOWER-7-DETECT: Interface Gi1/0/14: Power Device detected: IEEE PD
# *Apr 24 10:37:54.493: %ILPOWER-5-POWER_GRANTED: Interface Gi1/0/14: Power granted
# *Apr 24 10:38:36.289: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/3, changed state to up
# *Apr 24 10:38:37.289: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/3, changed state to up
# *Apr 24 10:40:24.661: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/14, changed state to up
# *Apr 24 10:40:25.662: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/14, changed state to up
# *Apr 24 12:09:03.605: %SYS-5-CONFIG_I: Configured from console by sajustin on vty1 (144.254.204.187)


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)


from SparkVariables import *
from SparkFunctions import *

arguments = sys.argv

interface = str(arguments[6])
if str(arguments[10]) == "administratively":
    state = str(arguments[10]) + " " + str(arguments[11])
    hostname = str(arguments[12])
else:
    state = str(arguments[10])
    hostname = str(arguments[11])


print("room ID :" + roomID_SoftwareProject)

resp = post_message("Interface " + interface +" state has changed on device: " + hostname + "\n" +
                    "New state is : " + state + "\n", roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

