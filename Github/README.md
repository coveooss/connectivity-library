# Indexing Github Using the Generic REST API Connector

## Use Case
This example shows how to index GitHub repositories and other content types.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Follow the [Web Application Flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) steps to get an OAuth 2.0 token.
2. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your token.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Github/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Further Reading
[GitHub REST API v3](https://developer.github.com/v3/)
