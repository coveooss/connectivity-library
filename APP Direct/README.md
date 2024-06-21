# Indexing AppDirect using the REST API connector
This guide explains how you can use the content of the provided JSON file in a [Coveo Platform](https://docs.coveo.com/en/3361/) [REST API](https://docs.coveo.com/en/1896/) source to index products from AppDirect. When you'll perform [update operations](https://docs.coveo.com/en/2039/), your Coveo REST API source will use this JSON configuration to perform HTTP requests against the AppDirect v1 API to extract content.

## Disclaimer
The Coveo GitHub Connectivity Library contains examples of repositories that have been indexed with Coveo's REST API or GraphQL API connector.

When using the search box on the [Add a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel, Coveo recommends using the REST API or GraphQL API source and the associated example configuration for a subset of the systems listed in the library. Coveo’s recommendations for the example configurations depend on the extent of testing in proofs of concept. Coveo recommends the REST API source AppDirect JSON configuration herein.

However, please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:

- Have a [Coveo organization](https://docs.coveo.com/en/185).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create and configure a REST API source](https://docs.coveo.com/en/1896/) using the example in [SourceJSONConfig.json](https://github.com/coveooss/connectivity-library/blob/master/APP%20Direct/SourceJSONConfig.json). This JSON configuration contains one Endpoint, which gets a list of all products, and one Subquery, which gets more details on the product. Adjust it to your own needs.
2. Make sure you've changed all placeholders in the configuration with your own values.
3. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
4. [Write an indexing pipeline extension](https://docs.coveo.com/en/1645/) based on the example in [`IPE.py`](https://github.com/coveooss/connectivity-library/blob/master/APP%20Direct/IPE.py).
5. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Limitation
Permissions can't be indexed.

## Reference
[AppDirect API documentation](https://help.appdirect.com/develop/useAppDirectAPI.html)
