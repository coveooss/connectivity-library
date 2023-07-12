# Indexing AppDirect Using the REST API Connector

## Use Case
This example shows how to add products from AppDirect.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create and configure a REST API source](https://docs.coveo.com/en/1896/) using the example in [SourceJSONConfig.json](https://github.com/coveooss/connectivity-library/blob/master/APP%20Direct/SourceJSONConfig.json). This JSON configuration contains one Endpoint, which gets a list of all products, and one Subquery, which gets more details on the product. Adjust it to your own needs.
2. Make sure you've changed all placeholders in the configuration with your own values.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
4. [Write an indexing pipeline extension](https://docs.coveo.com/en/1645/) based on the example in [`IPE.py`](https://github.com/coveooss/connectivity-library/blob/master/APP%20Direct/IPE.py).
5. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Limitation
Permissions can't be indexed.

## Reference
[AppDirect API documentation](https://help.appdirect.com/develop/useAppDirectAPI.html)
