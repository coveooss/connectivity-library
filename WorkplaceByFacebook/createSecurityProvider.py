#from datetime import datetime
import json
import requests
import time
import urllib
import zlib
import base64
import glob
import os.path
#import datetime



# Change the constants for your environment
organizationId = 'xxx'
sourceId = 'xxx'
authToken = 'xxx' 
MySecurityIdentityProviderName = "GENERIC_REST-workplacebyfacebook"

#################################################################################
# The following code creates a sample Security Identity Provider
##################################################################################

url = "https://platform.cloud.coveo.com/rest/organizations/" + organizationId + "/securityproviders/" + MySecurityIdentityProviderName

print ("Create Security Identity Provider: " + MySecurityIdentityProviderName)

# Header
headers = {
    'content-type': 'application/json',
    'Accept' : 'application/json',
    'Authorization': 'Bearer ' + authToken
}


payloadstr = """{
  "name" : "GENERIC_REST-workplacebyfacebook",
  "type": "GENERIC_REST",
  "referencedBy": [
    {
      "id": "xzbdz753uhndklv2ztkfgy",
      "type": "SOURCE"
    }
  ],
  "cascadingSecurityProviders": {
    "Email Security Provider": {
      "name": "Email Security Provider",
      "type": "EMAIL"
    }
  }
}"""


payload = json.loads(payloadstr)
payload["name"]= MySecurityIdentityProviderName
payload["referencedBy"][0]["id"]=sourceId
print(json.dumps(payload))

r = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
if r.status_code == 200:
    print ('success creating Security Identity Provider')
else:
    print (r.text)



