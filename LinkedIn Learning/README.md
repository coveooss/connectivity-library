# Indexing LinkedIn Learning Using the Generic REST API Connector

## Use Case
This example shows how to index LinkedIn Learning.

## Prerequisites
In order to fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Ensure you have access to LinkedIn Learning APIs. They are available for organizations that have purchased LinkedIn Learning site licenses.
2. Get your client ID and client secret.
3. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your client ID and client secret.
4. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/LinkedIn%20Learning/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust the configuration example to your own needs.
5. Make sure you've changed all placeholders in the configuration with your own values.
6. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
