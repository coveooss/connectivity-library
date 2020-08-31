# Indexing Azure DevoOps using the Generic REST API Connector

## Use case
This example shows how to index Azure DevOps.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Make sure you have a username that has access to everything.

2. Create a Generic REST API source
3. On the authorization section paste your Username and Password (from the usename with access to everything as mentioned in step 1)
4. Configure your Generic REST API source according to the example in SourceJSONConfig.json. This configuration uses a forced basic authentication, one endpoint and multiple nested subitems. Make sure to change all "placeholders" with your own values. 
    * **Important note:** There can be an almost infinite depth of recursivity, so you would have to copy paste until you reach the desired level of depth
5. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
6. Create the appropiate fields and mappings

**References:**
https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-server-rest-5.0