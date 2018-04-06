import sys
import cli

#intf= sys.argv[1:]
#intf = ''.join(intf[0])





print "\n\n *** Automatic backup to TFTP server *** \n\n"
output= cli.execute('copy startup-config ftp://Administrator:C1sco123@10.9.15.3/Temp/SoftwareProjectSLA/config_backup.cfg')
print (output)