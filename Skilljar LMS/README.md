# Indexing Skilljar LMS using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API source](https://docs.coveo.com/en/1896/) to index published courses and course series. Your Coveo source will use this JSON configuration to customize HTTP requests for the Skilljar LMS v1 API and identify the specific content to extract from the responses.

## Advisory

When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require adjustments to fit your specific use case.

## Prerequisites

To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

1. [Get a Skilljar API key](https://support.skilljar.com/hc/en-us/articles/203811260-Getting-started-with-the-Skilljar-API) to use in basic authentication.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your API key.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Skilljar%20LMS/SourceJSONConfig.json) as a base to build your source JSON configuration. This example retrieves the list of published courses with the first endpoint, the course description using a subquery in the first endpoint, and the course series with the second endpoint. Adjust the configuration example to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

* [Getting started with the Skilljar API](http://support.skilljar.com/hc/en-us/articles/203811260-Getting-started-with-the-Skilljar-API)
* [Skilljar API Endpoint Reference](https://api.skilljar.com/docs/#!/domains)
