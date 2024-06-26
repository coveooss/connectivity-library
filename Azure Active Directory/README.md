# Indexing Azure Active Directory using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index Azure Active Directory users and their information. Your Coveo source will use this JSON configuration to customize HTTP requests for the Microsoph Graph v1.0 API and identify the specific content to extract from the responses.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) on the Coveo Platform, Coveo may recommend, or not recommend, using one of these source types along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please note that all configurations in this library, including those recommended on the Coveo Platform, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create an OAuth app and a client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). Note your client ID and the newly created client secret.
2. Under **API Permissions**, grant `User.Read.All` for the application, located under **Microsoft Graph API**. Also add `Group.Read.All` if you want to index groups. Then, click **Grant admin consent for X**.
3. [Get your tenant ID](https://o365hq.com/faq/how-to-find-your-office-365-tenant-id), as you'll need it to place in the request endpoint.
4. Create a REST API source and, in the **Authorization** section, provide your client ID and client secret obtained in step 1.
5. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Azure%20Active%20Directory/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses OAuth 2.0 authentication. It also contains one Endpoint, which gets a list of the users (with Query Parameters to index the users' information), and one Subquery, which gets the user's photos. Adjust it to your own needs.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Limitation
Content [refresh](https://docs.coveo.com/en/2039/#refresh) isn't possible since the link for the next page is an URL rather than a date.

## Reference
[Azure Active Directory API documentation](https://docs.microsoft.com/en-us/graph/use-the-api)
