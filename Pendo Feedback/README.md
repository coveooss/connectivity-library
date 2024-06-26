# Indexing Pendo Feedback (formerly Receptive.io) using the Coveo REST API connector
This guide explains how you can use the content of the provided JSON file in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index features and feature comments. When you'll perform [update operations](https://docs.coveo.com/en/2039/) on your Coveo REST API source, it will use this JSON configuration to perform HTTP requests against the Pendo Feedback API to extract content.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When searching for a system in the [**Add a source of content**](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel of the Coveo Platform, Coveo may recommend, or not, using one of these source types and the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Coveo recommends the REST API source Pendo Feedback example JSON configuration herein.

However, please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Get a Pendo Feeback API key](https://support.pendo.io/hc/en-us/articles/14541867340571-Pendo-Feedback-API-Key).
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide the API key obtained in step 1.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Pendo%20Feedback/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Pendo Feedback API specifics
* [API Documentation](https://feedbackapi.pendo.io/)
* Retrieving feature views and vote counts from the API requires retrieving the individual features in a sub query. This is not optimal. Therefore, if you don't need the view count in the search results, you can omit the sub queries.
You can use the sub query if you need additional data from features. Just add the metadata fields that are missing.
* In the example JSON configuration, private Feedback and private comments are ignored. You can remove the  `IndexingAction` if you want to include `private` items.
* You can view example Pendo API JSON responses for feature and comment calls in [`PendoApiResponseExamples.md`](./PendoApiResponseExamples.md).

## Reference
[Pendo Feedback API documentation](https://engageapi.pendo.io/?bash)
