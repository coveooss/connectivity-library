# Indexing Azure DevoOps Using the Generic REST API Connector

## Use Case
This example shows how to index Azure DevOps.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Make sure you have an Azure DevOps account that has access to everything.
2. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your credentials.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Azure%20DevOps/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses a forced basic authentication. It also contains one endpoint and multiple nested subitems. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Azure DevOps Services REST API Reference](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1)
