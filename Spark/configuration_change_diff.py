# This script requires the following EEM environment variables to be defined:
#
# spark_token : Bearer token for your Spark user/bot
# spark_room  : Spark room name to which messages will be sent
# device_name : Device name from which the messages will be sent
#
# E.g.:
#
# event manager environment spark_token Bearer 1234abd...
# event manager environment spark_room Network Operators
# event manager environment device_name C3850
#

import eem
import re
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)

from SparkVariables import *
from SparkFunctions import *

CFG_BAK_PY = '/flash/running-config.bak'
CFG_BAK_IOS = 'flash:/running-config.bak'


# Get a CLI handle
# cli = eem.cli_open()
eem.cli_exec(cli, 'enable')
eem.cli_write(cli, 'copy runn {}'.format(CFG_BAK_IOS))

print("OK")

#
#
# if not os.path.isfile(CFG_BAK_PY):
#     try:
#         eem.cli_write(cli, 'copy runn {}'.format(CFG_BAK_IOS))
#         prom = eem.cli_read_pattern(cli, '(filename|#)')
#         if re.search(r'filename', prom):
#             eem.cli_exec(cli, '\r')
#     except Exception as e:
#         eem.action_syslog('Failed to backup configuration to {}: {}'.format(
#             CFG_BAK_IOS, e), priority='3')
#         sys.exit(1)
#     # First time through, only save the current config
#     eem.cli_close(cli)
#     sys.exit(0)
#
# res = None
# try:
#     res = eem.cli_exec(
#         cli, 'show archive config diff {} system:running-config'.format(CFG_BAK_IOS))
#     os.remove(CFG_BAK_PY)
#     eem.cli_write(cli, 'copy runn {}'.format(CFG_BAK_IOS))
#     prom = eem.cli_read_pattern(cli, 'filename')
#     if re.search(r'filename', prom):
#         eem.cli_exec(cli, '\r')
# except Exception as e:
#     eem.action_syslog(
#         'Failed to get config differences: {}'.format(e), priority='3')
#     sys.exit(1)
#
# eem.cli_close(cli)
#
# diff_lines = re.split(r'\r?\n', res)
# if re.search('No changes were found', res):
#     # No differences found
#     sys.exit(0)
#
# device_name = arr_envinfo['device_name']
# msg = '### Alert: Config changed on ' + device_name + '\n'
# msg += 'Configuration differences between the running config and last backup:\n'
# msg += '```{}```'.format('\n'.join(diff_lines[:-1]))
#
#
# resp = post_message_markdown(msg, roomID_SoftwareProject, bearer_Bot)
#
# print("resp = " + resp.text)
