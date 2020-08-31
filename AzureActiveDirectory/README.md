Indexing is done using the Generic REST API. Everything is available in the Microsoft Graph API to index users with their information.

Create an OAuth app
Use this documentation to create the OAuth app and a secret. Note the client ID and the newly created secret. https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app

Assign permissions
Under API Permissions, you'll have to grand User.Real.All, located under Microsoft Graph API.

Also, add Group.Read.All if you want to also index groups.

Then, click on "Grant admin consent for X".

Incremental Refresh
Incremental refresh won't be possible since the link for the next page is an URL, not a date.

Get the tenant ID
You'll need the tenant ID to place in the request endpoint. Use this doc to find it https://o365hq.com/faq/how-to-find-your-office-365-tenant-id