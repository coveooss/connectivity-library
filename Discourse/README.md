# Indexing Discourse using the Generic REST API Connector

## Use case
This example shows how to retrieve topics posted on a Discourse discussion platform and the posts in each topic, along with different metadata for each item type.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Get your discourse Api Key like instructed [here](https://docs.discourse.org/). 
2. Create a Generic REST API source
3. In the authentication section, paste your API Key (provided in step 1)
4. Configure your Generic REST API source according to the example in SourceJSONConfig.json
5. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
6. Create the appropiate fields and mappings.