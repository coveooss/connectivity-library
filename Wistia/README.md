# Indexing Wistia Using the Generic REST API Connector

## Use Case
This example shows how to index content posted from Wistia, a video marketing software.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Obtain crawling credentials: [The Wistia API](https://wistia.com/support/developers/data-api) supports either Basic Authentication or an access_token API Key. The API key can be found in the API Access section from your account settings.
2. [Create a Generic REST API](https://docs.coveo.com/en/1896/) source and, in the **Authorization** section, fill in you username and the API key obtained in step 1. as the password.
3. Use the example in [`SourceJSONConfig.json`](SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs. Wistia maintains a parent/child relationship between Project and Media objects, this leads to a single endpoint to index projects along with SubItem queries to indexed the related media objects.
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
