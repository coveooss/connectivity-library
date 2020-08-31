# Indexing Azure Active Diriectory using the Generic REST API Connector

## Use case
This example shows how to index Azure Active Directory users and their information using the Microsoph Graph API.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Create an OAuth app: Use [this documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) to create the OAuth app and a Client Secret. Note the Client ID and the newly created Client Secret
2. Assign permissions: Under API Permissions, you'll have to grand User.Real.All, located under Microsoft Graph API. Also, add Group.Read.All if you want to also index groups. Then, click on "Grant admin consent for X"
3. Get the tenant ID: You'll need the tenant ID to place in the request endpoint. Use [this doc](https://o365hq.com/faq/how-to-find-your-office-365-tenant-id) to find it

4. Create a Generic REST API source
5. On the authorization section paste your Client ID and Client Secret (provided in step 1)
6. Configure your Generic REST API source according to the example in SourceJSONConfig.json. This configuration uses OAuth2 authentication, one Endpoint to get the users (with Query Parameters to include the required user's information), and one Subquery to get the user's photos. 
7. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
8. Create the appropiate fields and mappings

## Limitations
Incremental refresh won't be possible since the link for the next page is an URL and not a date.