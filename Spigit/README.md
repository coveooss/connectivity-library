# Indexing Spigit using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source to index communities, ideas, idea comments and stats. Your Coveo source will use this JSON configuration to customize HTTP requests for the Spigit v1 API and identify the specific content to extract from the responses.

## Disclaimer
When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Using your Spigit account, [create a new Spigit application](https://support.spigit.com/hc/en-us/articles/115001307506-API-Getting-Started). The documentation URL should be: `https://<<YOUR_INSTANCE_ID>>.spigit.com/docs/api/index.html`.
2. Get an autorization code by using the following URL: `https://{communityName}.spigit.com/oauth/authorize?response_type=code&client_id={clientID}&client_secret={clientSecret}s&redirect_uri={redirect_uri}` in which you replace:
    * `{communityName}` with your Spigit community name
    * `{clientId}` with your application client ID
    * `{clientSecret}` with your application client secret
    * `{redirect_uri}` with your application redirect URI (e.g., `https://<<YOUR_INSTANCE_ID>.spigit.com/html/api/testOauthRedirectPage.html`)
    This code will be required later by the REST API source to generate a refresh token.
3. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your application client ID, client secret, and refresh token.
4. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Spigit/SourceJSONConfig.json) as a base to build your source JSON configuration. This example has one endpoint to get the Slack channels, which includes a subquery to get the messages in each channel, and another endpoint to get the members. Adjust the configuration example to your own needs.
5. Make sure you've changed all placeholders in the configuration with your own values.
6. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
7. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.
