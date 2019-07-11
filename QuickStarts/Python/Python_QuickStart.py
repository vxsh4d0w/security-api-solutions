# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. 
# --------------------------------------------------------------------------

## Visit https://aka.ms/graphsecuritydocs for the Microsoft Graph Security API documention.

import json
import urllib.request
import urllib.parse
import requests 

## Register an Azure Active Directory application with the 'SecurityEvents.ReadWrite.All' Microsoft Graph Permission.
## Get your Azure AD tenant administrator to grant administration consent to your application. This is a one-time activity unless permissions change for the application. 
appId = 'Enter_Your_App_ID_Here'
appSecret = 'Enter_Your_App_Secret_Here' 
tenantId = 'Enter_Your_Tenant_ID_Here'

# Azure Active Directory token endpoint.
url = "https://login.microsoftonline.com/%s/oauth2/v2.0/token" % (tenantId)
body = {
    'client_id' : appId,
    'client_secret' : appSecret,
    'grant_type' : 'client_credentials',
    'scope': 'https://graph.microsoft.com/.default'
}

## authenticate and obtain AAD Token for future calls
data = urllib.parse.urlencode(body).encode("utf-8") # encodes the data into a 'x-www-form-urlencoded' type
req = urllib.request.Request(url, data)

response = urllib.request.urlopen(req)

jsonResponse = json.loads(response.read().decode())
# Grab the token from the response then store it in the headers dict.
aadToken = jsonResponse["access_token"]
headers = { 
    'Content-Type' : 'application/json',
    'Accept' : 'application/json',
    'Authorization' : "Bearer " + aadToken
}
api_root = "https://graph.microsoft.com/v1.0/" 
if len(aadToken) > 0:
    print("Access token acquired.")


def make_request(url):
    """
    Makes a GET request.

    :param url: Url of the request.
    :returns: json response.
    :raises HTTPError: raises an exception
    """
    url_sanitized = urllib.parse.quote( url , safe="%/:=&?~#+!$,;'@()*[]") # Url encode spaces 
    req = urllib.request.Request(url_sanitized, headers=headers)
    print()
    print("########################################################################################")
    print("Calling the Microsoft Graph Security API...")
    print()
    print('GET "%s"' % url_sanitized)
    print()
    print("Headers :")
    print(json.dumps(headers, indent=4))
    print("########################################################################################")

    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        raise e

    jsonResponse = json.loads(response.read().decode())
    print()
    print("Response :")
    print(json.dumps(jsonResponse, indent=4))
    return jsonResponse

print("Sample Microsoft Graph Security API code loaded")

##### Uncomment the code below to get the most recent high severity alert from each provider.
# alert_url = "https://graph.microsoft.com/v1.0/security/alerts?$filter=severity eq 'high'&$top=1"
# make_request(alert_url)

##### Uncomment the code below to get an alert by id
# alert_url = "https://graph.microsoft.com/v1.0/security/alerts/58766702-02A8-4E64-BC2F-418EAA25D7A6"
# make_request(alert_url)


def update_alert(alertid=None, alertbody=None):
    """
    Makes a PATCH request to update an alert.

    :param alertid: Id of the alert to be updated.
    :param alertbody: Body of the PATCH request.
    :returns: json response.
    :raises ValueError: raises an exception
    """
    alert_url = "https://graph.microsoft.com/v1.0/security/alerts/%s" % alertid
    
    if alertbody == None:
        raise ValueError ('Request body cannot be empty')

    # Add the 'Prefer' header in order to get the updated alert back from the API after the PATCH. This is optional.
    patch_headers = headers
    patch_headers['Prefer'] = "return=representation"
    
    # vendorInformation is required by the API when PATCHing alerts, 
    # so we first make a call to GET the alert that we would like to PATCH.
    oldalert = requests.get(alert_url, headers=headers).json()
    # Then add 'vendorInformation' to the PATCH body.
    alertbody["vendorInformation"] = oldalert["vendorInformation"]

    print()
    print("########################################################################################")
    print("Calling the Microsoft Graph Security API...")
    print()
    print('PATCH "%s"' % alert_url)
    print()
    print("Headers :")
    print(json.dumps(headers, indent=4)) 
    print()   
    print("Body :")
    print(json.dumps(alertbody, indent=4))    
    print("########################################################################################")
    print()   
    
    # Make the PATCH request.
    response = requests.patch(alert_url, json.dumps(alertbody), headers=patch_headers)
    if response.status_code == 200:
        # if the response returned a 200, convert it to json
        response = response.json()
        print("Response :")
        print(json.dumps(response, indent=4))
    else:
        print("Response : Status Code", response.status_code)
        response = {}

    return response

##### Uncomment the code below to update an alert
# data = {"comments": ["Testing"]}
# update_alert(alertid="58766702-02A8-4E64-BC2F-418EAA25D7A6", alertbody=data)
