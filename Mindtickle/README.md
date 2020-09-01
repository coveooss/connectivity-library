# Indexing Mindtickle using the Generic REST API Connector

## Use case
This example shows how to index course materials from Mindtickle using its reporting API and Basic Authentication.

## Pre-requisites
In order to fully understand and use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide:
In Mindtickle, there are three inherent object types that the course materials are grouped: SeriesCollection, SeriesModules and Module. However in order to index just the Module, you must start with the SeriesCollection (obtain the seriesId), then get the SeriesModules (obtain the moduleId), then get the Module (using seriesId and moduleId).

In this example, we will only index the Module items, therefore there is also a pre-conversion IPE to reject the non-Module items when indexing.

1. Create a Generic REST API Source.
2. Configure your Generic REST API source according to the example in SourceJSONConfig.json 
    * In this example (using Basic Authentication credentials) we are indexing the SeriesCollection in our main endpoint, and adding SeriesModules as a Subquey, and Module as a Subquery of the Subquery.
3. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source#completion).
5. Write and IPE, according to the example in IPE.py, to reject non-Module items.
