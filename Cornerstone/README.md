# Indexing Cornerstone Using the Generic REST API Connector

## Use Case
This example shows how to index Cornerstone.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Register an application](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/info).
2. Retrieve your client ID and client secret.
3. Select the appropriate scopes. See the [complete list of scopes](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/scopes-security-permissions). You can also find the required scope on an endpoint information page such as [this one](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/apidoc/59aa5211-b2c9-45af-97b1-0c0902dc4060).
4. Test the authentication on Postman:
    * https://{{YOURLMS}}-{{env}}.csod.com/services/api/oauth2/token
    * The grant type is `client_credentials` (add your client ID and client secret).
5. Create a Generic REST API source and, in the **Authorization** section, provide your client ID and client secret obtained in step 2.
6. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Cornerstone/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses OAuth 2.0 authentication and gets all information from one endpoint. Adjust it to your own needs.
    * By default, the API returns a XML response. So, in the headers section of your JSON configuration, set `"Accept": "application/json"`.
    * In the Query Parameters, you can pass filters such as `"Provider": "Technology"`.
    * You can find the list of available parameters on an endpoint information page such as [this one](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/apidoc/59aa5211-b2c9-45af-97b1-0c0902dc4060).
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Reference
[Cornerstone API documentation](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/info)
