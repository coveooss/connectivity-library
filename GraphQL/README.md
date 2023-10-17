# Indexing a GraphQL API Using the GraphQL API Connector

## Use Case

This example shows how to index a GraphQL API, using the free Star Wars API.

## Prerequisites

To fully understand how to use this example, you must:

1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions, GraphQL without Security

1. [Create a GraphQL API source](https://docs.coveo.com/en/n6gh2329/index-content/add-or-edit-a-graphql-api-source).
2. Copy the config in [`SourceJSONConfig.json`](./SourceJSONConfig.json) to your source JSON configuration. Adjust it to your own needs.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/n6gh2329/index-content/add-or-edit-a-graphql-api-source#completion).
4. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

* [Star Wars API Explorer](https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer)
