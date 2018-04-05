from ciscosparkapi import CiscoSparkAPI
import cli
# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)


from SparkVariables import *

if __name__ == '__main__':
    # Use ArgParse to retrieve command line parameters.
    from argparse import ArgumentParser

    #parser = ArgumentParser("Spark Check In")
    ## Retrieve the Spark Token and Destination Email
    #parser.add_argument(
    #    "-t", "--token", help="Spark Authentication Token", required=True
    #)
    ## Retrieve the Spark Token and Destination Email
    #parser.add_argument(
    #    "-e", "--email", help="Email to Send to", required=True
    #)
    #args = parser.parse_args()
    #token = args.token
    #email = args.email

    output = cli.execute('show logging')
    print(output)

    message = "**Alert:** Config Changed "
    api = CiscoSparkAPI(access_token=bearer_Bot)
    #api.messages.create(toPersonEmail="sajustin@cisco.com", markdown=message)
    api.messages.create(roomId=roomID_SoftwareProject, markdown=message  )