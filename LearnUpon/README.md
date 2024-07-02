# Indexing LearnUpon using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API source](https://docs.coveo.com/en/1896/) to index courses. Your Coveo source will use this JSON configuration to customize HTTP requests for the LearnUpon v1 API and identify the specific content to extract from the responses.

## Advisory

When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites

To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

1. [Get a LearnUpon account](https://docs.learnupon.com/api/#get-started).
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide the credentials obtained in step 1.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/LearnUpon/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs. For example, you may want to extend the configuration to index [course modules](https://docs.learnupon.com/api/#modules).
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

[LearnUpon API documentation](https://docs.learnupon.com/api/#learnupon-technical-documentation)
