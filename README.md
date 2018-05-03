# Cat 9k Software Project of Sarah-Louise and Antoine

This repository leverages the programability features available on the Cisco Catalyst 9k. It contains multiple On-Box Python example scripts, shows the intergration with the Spark api and the use of an external server to leverage the NETCONF protocol and YANG data-models for scalability.  

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
##Adding the listening bot

```python
./ngrok http 8080

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
