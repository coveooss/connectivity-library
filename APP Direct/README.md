# Indexing AppDirect Using the Generic REST API Connector

## Use Case
This example shows how to add products from AppDirect.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create and configure a Generic REST API source](https://docs.coveo.com/en/1896/) using the example in [SourceJSONConfig.json](https://github.com/coveooss/connectivity-library/blob/master/APP%20Direct/SourceJSONConfig.json). This JSON configuration contains one Endpoint, which gets a list of all products, and one Subquery, which gets more details on the product. Adjust it to your own needs.
2. Make sure you've changed all placeholders in the configuration with your own values.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Limitation
Permissions can't be indexed.
