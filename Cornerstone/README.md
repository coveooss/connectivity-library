# Indexing Cornerstone using the Generic REST API Connector

## Use case
This example shows how to index Cornerstone.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Register an application: Follow the steps [here](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/info)
2. After registering the application, get the ClientID and the ClientSecret
3. Depending on your requirements, you will need to select the appropriate scopes: 
    * Here is a [complete list of the scopes](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/scopes-security-permissions) for the different endpoints.
    * You can also find the required scope on the endpoint information page like [this example](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/apidoc/59aa5211-b2c9-45af-97b1-0c0902dc4060).
4. Test the authentication on Postman:
    * https://{{YOURLMS}}-{{env}}.csod.com/services/api/oauth2/token
    * The grant type is: client_credentials (add your ClientID and ClientSecret)

5. Create a Generic REST API source
3. In the authentication section paste your credentials (ClientId, ClientsSecret)
4. Configure your Generic REST API source according to the example in SourceJSONConfig.json. This examples uses OAuth authentication and gets all the information from one endpoint. 
    * By default, the API returns a XML response, so in the headers section of your configuration, set "Accept": "application/json
    * You can pass filters in the Query Parameters: e.g. "Provider": "Technology"
    * You can find the list of available parameters on the endpoint information page: [e.g.](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/apidoc/59aa5211-b2c9-45af-97b1-0c0902dc4060)
5. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
6. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source#completion).
