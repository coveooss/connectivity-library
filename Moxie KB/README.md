# Indexing GoMoxie Using the REST API Connector

## Use Case
This example shows how to index GoMoxie Knowledge Base Articles.

## Prerequisites
In order to fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
You will need to make the four follwing API calls. If you need to test them, you may use Postman, but GoMoxie also usually offers a visual widget to try calls. Its URL should be: `restapi-<<YOUR_DOMAIN>>.kb.net/Widgets/Admin`. If using Chrome, you must open Chrome Dev Tools to see the results of some of those calls.
* Get Article List (`NewlyPublished`/"Get Newly Published Article" button) – one call per rebuild
* Get Article List (`RecentlyUpdated`/"Get Recently Updated Published Article" button) - one call per rebuild
* Get Article – one call per document
* Get Article Metadata – one call per document

**Important:** There are two endpoints that carries same parameters, if you modify/reuse it don't forget to update both endpoints parameters the same way. The two parameters are NewlyPublished (for new articles), and RecentlyUpdated (for new versions of existing articles). When an article is updated with a new version, its record will cease to be part of the NewlyPublished list.
    
1. Ensure you have a client ID, an API key, and a profile ID.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter these credentials.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/commit/fd92a6cd8e2afd6885d6360276cb1d5bc65abe6b) as a base to build your source JSON configuration. This example retrieves the list of articles using the main endpoint, then the body using a subquery, and then metadata using another subquery. Adjust the configuration example to your own needs. 
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. [Write an indexing pipeline extension](https://docs.coveo.com/en/1645/) based on the example in [`IPE.py`](https://github.com/coveooss/connectivity-library/blob/master/Moxie%20KB/IPE.py).
5. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.
