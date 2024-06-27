# Indexing the Star Wars API Explorer using the Coveo GraphQL API connector

This guide demonstrates how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source to index Star Wars films. Your Coveo source will use this JSON configuration to customize HTTP requests for the Star Wars GraphQL API and identify the specific content to extract from the responses.

## Disclaimer
When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a GraphQL API source](https://docs.coveo.com/en/n6gh2329/).

## Instructions

1. [Create a GraphQL API source](https://docs.coveo.com/en/n6gh2329/).
2. Copy the config in [`SourceJSONConfig.json`](SourceJSONConfig.json) to your source JSON configuration. Adjust it to your own needs.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/n6gh2329#completion).
4. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

[Star Wars API Explorer](https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer)
