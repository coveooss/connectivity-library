# Indexing Vidyard Using the REST API Connector

## Use Case
This example shows how to index content posted from Vidyard, a screen recorder software.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Obtain crawling credentials: [The Vidyard API](https://developer.vidyard.com/) will allow you to authenticate with the token. The API Token can be found from the side menu, select Admin > API Tokens
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, fill in you username and the API Token obtained in step 1. as the password.
3. Use the example in [`SourceJSONConfig.json`](SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs. 
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
5. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Vidyard API documentation](https://developer.vidyard.com/)
