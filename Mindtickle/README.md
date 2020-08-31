# Indexing Mindtickle using the Generic REST API Connector

## Use case
This example shows how to index course materials from Mindtickle.

## Pre-requisites
In order to fully understand and use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide:
In Mindtickle, there are three inherent object types that the course materials are grouped: SeriesCollection, SeriesModules and Module. However in order to index just the Module, you must start with the SeriesCollection (obtain the seriesId), then get the SeriesModules (obtain the moduleId), then get the Module (using seriesId and moduleId).

This was achieved by using the Coveo Rest API connector against the Mindtickle reporting API and Basic Authentication credentials. In this example, we will only index the Module items, therefore there is also a pre-conversion IPE to reject the non-Module items when indexing.

1. Add new Generic Rest API connector (to your Coveo Cloud organization)
2. Configure API to generate three document types: SeriesCollection, SeriesModules, Module (using Basic Authentication credentials)
3. Make sure you've changed all "placeholders" with your own values, and to adjust the configuration to your own needs
4. Write IPE to reject non-Module items
5. 
