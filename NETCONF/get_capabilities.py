#!/usr/bin/env python

from ncclient import manager
import sys


# the variables below assume the user is leveraging the
# lab environment and accessing csr1000v
# use the IP address or hostname of your CSR1000V device
HOST = '10.48.108.110'
# use the NETCONF port for your CSR1000V device
PORT = 830
# use the user credentials for your CSR1000V device
USER = 'netconf-user'
PASS = 'C1sco123'


def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print all NETCONF capabilities
        print('***Here are the Remote Devices Capabilities***')
        for capability in m.server_capabilities:
            print(capability.split('?')[0])


if __name__ == '__main__':
    sys.exit(main())