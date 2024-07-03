# Indexing Cornerstone using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API source](https://docs.coveo.com/en/1896/) to index training data. Your Coveo source will use this JSON configuration to customize HTTP requests for the Cornerstone Catalog Search API and identify the specific content to extract from the responses.

## Advisory

When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites

To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

1. [Register an application](https://csod.dev/guides/bulk/quick-start.html#register-an-oauth-2-0-application).
2. Retrieve your client ID and client secret.
3. Select the appropriate scopes. See the [complete list of scopes](https://csod.dev/guides/bulk/security-permissions-scopes.html). You can also find the required scope on an endpoint information page such as [this one](https://csod.dev/reference/learning/#tag/Learning-Search/paths/~1Catalog~1GlobalSearch/get).
4. Test the authentication on Postman:
   * https://{{YOURLMS}}-{{env}}.csod.com/services/api/oauth2/token
   * The grant type is `client_credentials` (add your client ID and client secret).
5. Create a REST API source and, in the **Authorization** section, provide your client ID and client secret obtained in step 2.
6. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Cornerstone/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses OAuth 2.0 authentication and gets all information from one endpoint. Adjust it to your own needs.
   * By default, the API returns a XML response. So, in the headers section of your JSON configuration, set `"Accept": "application/json"`.
   * In the Query Parameters, you can pass filters such as `"Provider": "Technology"`.
   * You can find the list of available parameters on an endpoint information page such as [this one](https://csod.dev/reference/learning/#tag/Learning-Search/paths/~1Catalog~1GlobalSearch/get).
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

[Cornerstone API documentation](https://csod.dev/guides/learning/)
