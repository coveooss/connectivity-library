# Indexing App Direct using the Generic REST API Connector

## Use case
This example shows how to add products from App Direct.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Create a Generic REST API source
2. Configure your Generic REST API source according to the example in SourceJSONConfig.json. This configuration contains one Endpoint, to get a list of all products, and one Subquery, to get more details on the product
3. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source#completion).

## Limitation
Permissions can't be indexed.