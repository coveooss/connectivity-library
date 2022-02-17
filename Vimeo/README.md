# Indexing Vimeo Using the Generic REST API Connector

## Use Case
This example shows how to index Vimeo videos.

## Prerequisites
To fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create an application](https://developer.vimeo.com/api/guides/start) and get an access token.
2. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, under **API key**, enter your access token.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Vimeo/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust the configuration example to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Reference
[Vimeo API documentation](https://developer.vimeo.com/api/guides/start)
