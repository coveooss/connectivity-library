# Indexing Spigit using the Generic REST API Connector

## Use case
This example shows how to index content from Spigit innovation management software.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Create a new App: Refer to the [API Getting Started documentation page](https://support.spigit.com/hc/en-us/articles/115001307506-API-Getting-Started) (you will need to create a Spigit account if not already done) on how to create a application. The documentation url should look like https://<<YOUR_INSTANCE_ID>>.spigit.com/docs/api/index.html.
2. Review authorization code: 
    Authenticate against your Spigit Community to retrieve the authorization code. This code will be required later by the Generic Rest API source to generate the refresh token.

    To retrieve the code, you will need to navigate to the following url:
    https://{communityName}.spigit.com/oauth/authorize?response_type=code&client_id={clientID}&client_secret={clientSecret}s&redirect_uri={redirect_uri}
    * communityName: Your Spigit community name
    * clientId: Should be found in your Application defined in Step 1
    * clientSecret: Should be found in your Application defined in Step 1
    * redircet_uri: Should be found in your Application defined in Step 1 (e.g. https://<<YOUR_INSTANCE_ID>.spigit.com/html/api/testOauthRedirectPage.html )

3. Create a Generic REST API source
4. On the authentication section, paste Client ID, Client secret and Refresh token (provided in step 2) 
5. Configure your Generic REST API source according to the example in SourceJSONConfig.json
6. Make sure you've changed all "placeholders" with your own values, and to adjust the configuration to your own needs
7. Create the appropiate fields and mappings.