# Indexing Spigit using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index communities, ideas, idea comments and stats. When you'll perform [update operations](https://docs.coveo.com/en/2039/) on your Coveo REST API | GraphQL source, it will use this JSON configuration to perform HTTP requests against the Spigit v1 API to extract content.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When searching for a system in the [**Add a source of content**](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel of the Coveo Platform, Coveo may recommend, or not, using one of these source types and the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
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
