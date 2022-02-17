# Indexing Stack Overflow Using the Generic REST API Connector

## Use Case
This example shows how to index Stack Overflow tagged Questions and Answers.

## Prerequisites
To fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Get your access token credentials](https://api.stackexchange.com/docs/authentication) using the explicit OAuth 2.0 flow.
2. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, under **API key**, enter your access token.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Stackoverflow/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses the main endpoint to get the questions and retrieves the answers as subitems. The main endpoint targets questions with the tags specified in the query parameters. Adjust the configuration example to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Reference
[Stack Overflow API documentation](https://api.stackexchange.com/docs)
