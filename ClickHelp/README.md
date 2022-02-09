# Indexing ClickHelp Using the Generic REST API Connector

## Use Case
This example shows how to index Projects and Articles created from ClickHelp, a cloud-based documentation tool for teams. 

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Generate an [API Key](https://clickhelp.com/software-documentation-tool/user-manual/api-authentication.html) from ClickHelp. To do so, simply navigate your profile and click on "RESET API KEY".
2. [Create a Generic REST API](https://docs.coveo.com/en/1896/) source and, in the **Authorization** section, fill in you username and the API key obtained in step 1. as the password.
3. Use the example in [`SourceJSONConfig.json`](SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs. ClickHelp maintains a parent/child relationship between Project and Articles objects, this leads to a single endpoint to index projects along with SubItem queries to indexed the related Articles objects.
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Reference
[ClickHelp API documentation](https://clickhelp.com/software-documentation-tool/user-manual/clickhelp-api.html)
