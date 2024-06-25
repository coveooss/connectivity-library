# Indexing the Star Wars API Explorer using the Coveo GraphQL API connector

This guide demonstrates how you can use the content of the provided JSON file in a [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index Star Wars films. When you'll perform [update operations](https://docs.coveo.com/en/2039/) on your GraphQL source, it will use this JSON configuration to perform HTTP requests against the Star Wars GraphQL API to extract content.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When searching for a system in the [Add a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel of the Coveo Platform, Coveo may recommend, or not, using one of these source types and the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a GraphQL API source](https://docs.coveo.com/en/n6gh2329/).

## Instructions

1. [Create a GraphQL API source](https://docs.coveo.com/en/n6gh2329/).
2. Copy the config in [`SourceJSONConfig.json`](./SourceJSONConfig.json) to your source JSON configuration. Adjust it to your own needs.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/n6gh2329#completion).
4. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

[Star Wars API Explorer](https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer)
