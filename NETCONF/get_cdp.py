"""
    Netconf python example by yang-explorer (https://github.com/CiscoDevNet/yang-explorer)

    Installing python dependencies:
    > pip install lxml ncclient

    Running script: (save as example.py)
    > python example.py -a 10.48.108.110 -u netconf-user -p C1sco123 --port 830
"""

import lxml.etree as ET
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

HOST = '10.48.108.110'
# use the NETCONF port for your CSR1000V device
PORT = 830
# use the user credentials for your CSR1000V device
USER = 'netconf-user'
PASS = 'C1sco123'

payload = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <cdp-neighbor-details xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-cdp-oper">
    <cdp-neighbor-detail>
      <device-id/>
      <device-name/>
      <capability/>
      <version/>
    </cdp-neighbor-detail>
  </cdp-neighbor-details>
</filter>
"""

if __name__ == '__main__':


    # connect to netconf agent
    with manager.connect(host=HOST,
                         port=PORT,
                         username=USER,
                         password=PASS,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'iosxe'}) as m:

        # execute netconf operation
        try:
            response = m.get(payload).xml
            data = ET.fromstring(response)
        except RPCError as e:
            data = e._raw

        # beautify output
        print(ET.tostring(data, pretty_print=True))