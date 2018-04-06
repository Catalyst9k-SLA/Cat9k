import sys
import cli

#intf= sys.argv[1:]
#intf = ''.join(intf[0])






print "\n\n *** Printing show cmd with 'executep' function *** \n\n"
cli.executep('show ip interface brief')

print "\n\n *** Printing show cmd with 'execute' function *** \n\n"
output= cli.execute('copy start-up config running-config')
print (output)