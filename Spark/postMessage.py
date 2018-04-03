import requests

def postMessage(roomID, message):

    if roomID is None:
        roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vM2IzYjUyOTAtMTMxMy0xMWU4LWJlY2EtN2RlZGYwNWYxOTFh"

    if message is None:
        message = "Message is None - Test message"

    bearerAntoine = "NTNlNmY1NjQtNTM4Ny00OThlLWFkMzAtZTc4YjkyYzAyZGI0OWE1ODVmY2ItODIx"
    bearerBot = "ZTRlYTY5YjQtODMxNC00NDJhLWFmM2YtZmU5OGI0MDAxN2Y1MjEyNDg0YzYtZmFi"

    url = "https://api.ciscospark.com/v1/messages"

    payload = "{" \
              "\r\n  \"roomId\" : \"" + roomID + "\"," \
              "\r\n  \"text\" : \"" + message + "\"\r\n" \
              "}"

    headers = {
        'Authorization': "Bearer " + bearerBot,
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    return 1

