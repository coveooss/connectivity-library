# Indexing GoMoxie using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index knowledge base articles. Your Coveo source will use this JSON configuration to customize HTTP requests for the Moxie API and identify the specific content to extract from the responses.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) on the Coveo Platform, Coveo may recommend, or not recommend, using one of these source types along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please note that all configurations in this library, including those recommended on the Coveo Platform, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
You will need to make the four follwing API calls. If you need to test them, you may use Postman, but GoMoxie also usually offers a visual widget to try calls. Its URL should be: `restapi-<<YOUR_DOMAIN>>.kb.net/Widgets/Admin`. If using Chrome, you must open Chrome Dev Tools to see the results of some of those calls.
* Get Article List (`NewlyPublished`/"Get Newly Published Article" button) – one call per rebuild
* Get Article List (`RecentlyUpdated`/"Get Recently Updated Published Article" button) - one call per rebuild
* Get Article – one call per document
* Get Article Metadata – one call per document

**Important:** There are two endpoints that carry the same parameters. If you modify/reuse endpoints, don't forget to update both endpoint parameters the same way. The two parameters are `NewlyPublished` (for new articles), and `RecentlyUpdated` (for new versions of existing articles). When an article is updated with a new version, its record will cease to be part of the NewlyPublished list.

1. Ensure you have a client ID, an API key, and a profile ID.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter these credentials.
3. Use the example in [`SourceJSONConfig.json`](SourceJSONConfig.json) as a base to build your source JSON configuration. This example retrieves the list of articles using the main endpoint, then the body using a subquery, and then metadata using another subquery. Adjust the configuration example to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. [Write an indexing pipeline extension](https://docs.coveo.com/en/1645/) based on the example in [`IPE.py`](Extensions/IPE.py).
5. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.
