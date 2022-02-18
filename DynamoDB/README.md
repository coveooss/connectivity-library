# Indexing DynamoDB Using the Generic REST API Connector

## Use Case
This example shows how to index DynamoDB.

## Prerequisites
In order to fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create an Amazon API gateway](https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/)to provide a REST service to your DynamoDB.
2. [Create and configure a Generic REST API source](https://docs.coveo.com/en/1896/) using the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/DynamoDB/SourceJSONConfig.json). Adjust the configuration example to your own needs.
3. Make sure you've changed all placeholders in the configuration with your own values.
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
5. When testing your source configuration, you might also find you need extra configurations such as an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to index the desired content properly.

## Reference
[DynamoDB API documentation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html)
