# Cat 9k Software Project of Sarah-Louise and Antoine

This repository leverages the programability features available on the Cisco Catalyst 9k. It contains multiple On-Box Python example scripts making use of the Guestshell, shows the integration with the Spark api and the use of an external server to leverage the NETCONF protocol and YANG data-models for scalability.  

## On-Box Python

Use the Embedded Event Manager (EEM) to automatically take actions when a specific event happend on the switch.  

* When interface state change, post a message on Spark
* Current interface state is cleary shown on Spark

![Interface state has changed](https://i.imgur.com/OtVRopE.png)

* Post a message on Spark when a user modifies the configuration. Script is now able to get the date, time, line mode and user who did the change, and post it into the spark group.

![config change](https://i.imgur.com/Yag4Wj8.png)


## Spark bot 

* Adding bot integration (Kitty), who is able to detect message and answer
* Save the configuration from the Spark room. Do __@Bot save config__ and the configuration will be backed up to a TFTP server (parameters on SparkVariables.py)

![save config](https://i.imgur.com/gxZNulb.png)


# Getting started

## Enabling the Guestshell

We show how to enable the Guestshell on a Catalyst 9300 running IOS-XE 16.8.1. A guestshell interface has to be configured in the app-hosting interface prior to the activation of the Guestshell as following:

```
#conf t
(config)#interface GigabitEthernet0/0
(config-if)#vrf forwarding Mgmt-vrf
(config-if)#ip address dhcp
(config-if)#speed 1000
(config-if)#negotiation auto
(config-if)#end

#guestshell enable
#conf t
(config)#app-hosting appid guestshell 
(config-app-hosting)#vnic managementc guest-interface 0 guest-ipaddress 10.8.0.102 netmask 255.255.255.0 gateway 10.8.0.254 name-server 208.677.222.222d
(config-app-hosting)#end

```

## Embedded Event Manager applet examples

The EEM is enabled on the switch though EEM applets. Configuration changes are monitored by executing following CLI configuration:

```
cat9k#config t
cat9k(config)#event manager applet GUESTSHELL-CONFIG-CHANGE-TO-SPARK
cat9k(config-applet)#event syslog pattern "%SYS-5-CONFIG_I: Configured from"
cat9k(config-applet)#action 0.0 cli command "en"
cat9k(config-applet)#action 1.0 info type syslog history
cat9k(config-applet)#action 2.0 info type routername
cat9k(config-applet)#action 3.0 cli command "guestshell run python /home/guestshell/SoftwareProject/Cat9k/Spark/configuration_change.py $_info_syslog_hist_msg_32 $_info_routername"
cat9k(config-applet)#exit
cat9k(config)#exit

```

Interface change monitoring:

```
cat9k#config t
cat9k(config)#event manager applet GUESTSHELL-INT-STATE-UPDOWN
cat9k(config-applet)#event syslog pattern "%LINK-3-UPDOWN:"
cat9k(config-applet)#action 0   cli command "enable"
cat9k(config-applet)#action 1.0 info type syslog history
cat9k(config-applet)#action 2.0 info type routername
cat9k(config-applet)#action 3.0 cli command "guestshell run python /home/guestshell/SoftwareProject/Cat9k/Spark/intState_change.py $_info_syslog_hist_msg_32 $_info_routername"
cat9k(config-applet)#exit
cat9k(config)#exit

```

## Adding the listening bot

```python
./ngrok http 8080
cc
# Getting the URL from ngrok
# Take this URL, and add it to SparkVariables.py
# Add '/webhook' at the end of the URL

# Example :
webhook_URL = "https://e18e3287.ngrok.io/webhook"
** Don't forget the "/webhook" at the end **

# Run the below command everytime you have a new URL URL
python postwebhook.py

# To run the listening bot
python webhookapp.py
```

More info about the Spark Webhooks :

> https://developer.ciscospark.com/resource-webhooks.html
