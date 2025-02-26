# Indexing MindTickle using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API source](https://docs.coveo.com/en/1896/) to index course material. Your Coveo source will use this JSON configuration to customize HTTP requests for the Mindtickle reporting API and identify the specific content to extract from the responses.

## Advisory

When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require adjustments to fit your specific use case.

## Prerequisites

To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

In MindTickle, course material is organized into three object types: SeriesCollection, SeriesModules, and Module. However in order to index a Module, you must start with the SeriesCollection and obtain the series ID, then get the SeriesModules and obtain the module ID, then get the Module using the series and module ID. Therefore, if you want to index Module items only, you can use the indexing pipeline extension (IPE) in this folder to discard non-Module items.

1. [Create and configure a REST API source](https://docs.coveo.com/en/1896/) using the example in [`SourceJSONConfig.json`](SourceJSONConfig.json). This JSON configuration indexes SeriesCollections through the main endpoint, and then SeriesModules as SeriesCollection subitems, and then Modules as subitems of the SeriesModules. Adjust the configuration example to your own needs.
2. Make sure you've changed all placeholders in the configuration with your own values.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
4. To reject non-Module items, [write an indexing pipeline extension](https://docs.coveo.com/en/1645/) based on the example in [`IPE.py`](Extensions/IPE.py).
5. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.
