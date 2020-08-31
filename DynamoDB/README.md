# Indexing Dynamo DB using the Generic REST API Connector

## Use case
This example shows how to index Dynamo DB

## Pre-requisites
In order to fully understand and use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Follow this procedure to create a REST service to your DynamoDB: [Create Amazon API Gateway](https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/)
2. Create a Generic REST API source
3. Configure your Generic REST API source according to the example in SourceJSONConfig.json. 
4. Make sure you've changed all "placeholders" with your own values, and to adjust the configuration to your own needs
5. Create the appropiate fields and mappings.