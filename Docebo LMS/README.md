# Indexing Docebo LMS using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source to index courses, course content, and learning plans. Your Coveo source will use this JSON configuration to customize HTTP requests for the Docebo LMS v1 API and identify the specific content to extract from the responses.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source), Coveo may recommend, or not recommend, using one of these source types along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Ask Docebo administrator to create an API app for Coveo (OAuth 2.0 protocol). You'll need a client ID and a client secret. For more information, see [Activating and Managing the SSO and API App](https://www.docebo.com/knowledge-base/how-to-activate-and-manage-the-sso-and-api-app/) and [APIs Authentication](https://www.docebo.com/knowledge-base/authentication-api-ssp-app-grant-types/). **Important:** With the new 7.0 APIs (found at `<<YOUR_LMS>>.docebosaas.com/api-browser/`), the system also requires a specific user permission.
2. Try generating an access token with Postman or any other REST client. Example with "password" grant type (`<<YOUR_LMS>>.docebosaas.com/oauth2/token`).
3. Test your access token with the course endpoint `<<YOUR_LMS>>.docebosaas.com/api/learn/v1/courses`.
4. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your client ID, client secret, and credentials.
5. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Docebo%20LMS/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses two endpoints to retrieve courses and learning plans. The course endpoint uses a subquery to get course content. Adjust the configuration example to your own needs.
6. Make sure you've changed all placeholders in the configuration with your own values.
7. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
8. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Docebo LMS API documentation](https://help.docebo.com/hc/en-us/sections/360005441800-APIs)
