# Indexing Contentstack using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source to index blogs and authors. Your Coveo source will use this JSON configuration to customize HTTP requests for the Contentstack v3 API and identify the specific content to extract from the responses.

## Disclaimer
When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Log in to Contentstack](https://app.contentstack.com/).
2. Find the stack you want to index.
3. Under **Settings** > **Tokens**, [create a management token](https://www.contentstack.com/docs/developers/create-tokens/generate-a-management-token/). Take note of the API key and the management token.
4. Test the authentication on Postman. Use the **Run in Postman** button on the [Content Management API](https://www.contentstack.com/docs/developers/apis/content-management-api/) page.
5. [Log in to your Coveo organization](https://platform.cloud.coveo.com).
6. Under **Sources**, [create a REST API source](https://docs.coveo.com/en/1896/):
   1. In the **Authorization** section, enter your API key.
   2. Under **Content to Include**, enter your source JSON configuration. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Contentstack/SourceJSONConfig.json) as a base.
   3. Make sure you've changed all placeholders in the configuration with your own values:
      1. Enter your management token in all `headers` sections.
      2. Replace the URL placeholders with your site's URL.
   4. Add or update the `Endpoints` section according to your data structure in Contentstack.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Contentstack's Content Management API documentation](https://www.contentstack.com/docs/developers/apis/content-management-api/)
