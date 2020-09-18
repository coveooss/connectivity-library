# Indexing MindTickle Using the Generic REST API Connector

## Use Case
This example shows how to index course materials from MindTickle using its reporting API and basic authentication.

## Prerequisites
In order to fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
In MindTickle, course material is organized into three object types: SeriesCollection, SeriesModules, and Module. However in order to index a Module, you must start with the SeriesCollection and obtain the series ID, then get the SeriesModules and obtain the module ID, then get the Module using the series and module ID. Therefore, if you want to index Module items only, you can use the indexing pipeline extension (IPE) in this folder to discard non-Module items.

1. [Create and configure a Generic REST API source](https://docs.coveo.com/en/1896/) using the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Mindtickle/SourceJSONConfig.json). This JSON configuration indexes SeriesCollections through the main endpoint, and then SeriesModules as SeriesCollection subitems, and then Modules as subitems of the SeriesModules. Adjust the configuration example to your own needs.
2. Make sure you've changed all placeholders in the configuration with your own values.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
4. To reject non-Module items, [write an indexing pipeline extension]({{ site.baseurl }}/1645/) based on the example in [`IPE.py`](https://github.com/coveooss/connectivity-library/blob/master/Mindtickle/IPE.py).
