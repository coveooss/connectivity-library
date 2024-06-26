# Indexing Azure DevOps using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) | [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index wiki pages. Your Coveo source will use this JSON configuration to customize HTTP requests for the Azure DevOps REST API and identify the specific content to extract from the responses.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) on the Coveo Platform, Coveo may recommend, or not recommend, using one of these source types along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Coveo specifically recommends the REST API Azure DevOps example JSON configuration provided herein

However, please note that all configurations in this library, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Make sure you have an Azure DevOps account that has access to everything.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your credentials.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Azure%20DevOps/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses a forced basic authentication. It also contains one endpoint and multiple nested subitems. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Azure DevOps Services REST API Reference](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1)
