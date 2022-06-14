# Indexing Azure Active Directory Using the Generic REST API Connector

## Use Case
This example shows how to index Azure Active Directory users and their information using the Microsoph Graph API.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create an OAuth app and a client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). Note your client ID and the newly created client secret.
2. Under **API Permissions**, grant `User.Read.All` for the application, located under **Microsoft Graph API**. Also add `Group.Read.All` if you want to index groups. Then, click **Grant admin consent for X**.
3. [Get your tenant ID](https://o365hq.com/faq/how-to-find-your-office-365-tenant-id), as you'll need it to place in the request endpoint.
4. Create a Generic REST API source and, in the **Authorization** section, provide your client ID and client secret obtained in step 1.
5. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Azure%20Active%20Directory/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses OAuth 2.0 authentication. It also contains one Endpoint, which gets a list of the users (with Query Parameters to index the users' information), and one Subquery, which gets the user's photos. Adjust it to your own needs.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Limitation
Content [refresh](https://docs.coveo.com/en/2039/#refresh) isn't possible since the link for the next page is an URL rather than a date.

## Reference
[Azure Active Directory API documentation](https://docs.microsoft.com/en-us/graph/use-the-api)
