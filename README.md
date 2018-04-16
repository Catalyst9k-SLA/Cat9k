Cat 9k Software Project of Sarah-Louise and Antoine

# Working so far :

* Post a message on Spark when a user modifies the configuration. Script is now able to get the date, time, line mode and user who did the change, and post it into the spark group.
* Post a message on Spark when an interface state changes
* Adding bot integration (Kitty), who is able to detect message and answer
* Save the configuration from the Spark room. Do __@Bot save config__ and the configuration will be backed up to a TFTP server (parameters on SparkVariables.py)

# Adding the listening bot

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
