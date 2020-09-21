# Indexing Spigit Using the Generic REST API Connector

## Use Case
This example shows how to index content from Spigit.

## Prerequisites
To fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Using your Spigit account, [create a new Spigit application](https://support.spigit.com/hc/en-us/articles/115001307506-API-Getting-Started). The documentation URL should be: `https://<<YOUR_INSTANCE_ID>>.spigit.com/docs/api/index.html`.
2. Get an autorization code by using the following URL: `https://{communityName}.spigit.com/oauth/authorize?response_type=code&client_id={clientID}&client_secret={clientSecret}s&redirect_uri={redirect_uri}` in which you replace:
    * `{communityName}` with your Spigit community name
    * `{clientId}` with your application client ID
    * `{clientSecret}` with your application client secret
    * `{redirect_uri}` with your application redirect URI (e.g., `https://<<YOUR_INSTANCE_ID>.spigit.com/html/api/testOauthRedirectPage.html`)
    This code will be required later by the Generic Rest API source to generate a refresh token.
3. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your application client ID, client secret, and refresh token.
4. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Spigit/SourceJSONConfig.json) as a base to build your source JSON configuration. This example has one endpoint to get the Slack channels, which includes a subquery to get the messages in each channel, and another endpoint to get the members. Adjust the configuration example to your own needs.
5. Make sure you've changed all placeholders in the configuration with your own values.
6. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
