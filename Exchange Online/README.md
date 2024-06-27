# Indexing Azure Active Directory using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API](https://docs.coveo.com/en/1896/) source to index Exchange Online user or shared mailbox emails and their attachments. Your Coveo source will use this JSON configuration to customize HTTP requests for the Microsoph Graph API and identify the specific content to extract from the responses.

## Disclaimer
When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create an OAuth app and a client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app). Note your client ID and the newly created client secret.
2. Under **API Permissions**, grant `Mail.Read`, located under **Microsoft Graph API**. Then, click **Grant admin consent for X**.
3. [Get your tenant ID](https://o365hq.com/faq/how-to-find-your-office-365-tenant-id), as you'll need it to place in the request endpoint.
4. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your client ID and client secret obtained in step 1.
5. Use the example in [`ExchangeOnlineSourceConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Exchange%20Online/ExchangeOnlineSourceConfig.json) as a base to build your source JSON configuration. This example uses OAuth 2.0 authentication. It also contains one `Endpoint`, which gets all emails of a given mailbox, and one `Subquery`, which gets email attachments. Adjust the configuration to your own needs.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[API documentation](https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/office-365-rest-apis-for-mail-calendars-and-contacts)
