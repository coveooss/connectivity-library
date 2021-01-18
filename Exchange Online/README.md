# Indexing Azure Active Directory Using the Generic REST API Connector

## Use Case
This example shows how to a index Exchange Online shared mailbox or a user's mailbox using the Microsoph Graph API.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create an OAuth app and a client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). Note your client ID and the newly created client secret.
2. Under **API Permissions**, grant `Mail.Read`, located under **Microsoft Graph API**. Then, click **Grant admin consent for X**.
3. [Get your tenant ID](https://o365hq.com/faq/how-to-find-your-office-365-tenant-id), as you'll need it to place in the request endpoint.
4. Create a Generic REST API source and, in the **Authorization** section, provide your client ID and client secret obtained in step 1.
5. Use the example in [`ExchangeOnlineSourceConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Exchange%20Online/ExchangeOnlineSourceConfig.json) as a base to build your source JSON configuration. This example uses OAuth 2.0 authentication. It also contains one Endpoint, which gets all emails of a given mailbox, and one Subquery, which gets email attachments. Adjust it to your own needs.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
