# Indexing Sitecore Content Hub using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API](https://docs.coveo.com/en/1896/) source to index Sitecore Content Hub items. Your Coveo source will use this JSON configuration to customize HTTP requests for the Sitecore Content Hub API and identify the specific content to extract from the responses.

## Disclaimer
When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

> [!NOTE]
> See [Understanding the SourceJSONConfig.json file](resources/understanding-the-sourcejsonconfig-json-file.md) for explanations on the key aspects of the REST API source configuration.

1. [Create a token](https://doc.sitecore.com/ch/en/developers/42/cloud-dev/rest-api--get-token.html) to access the Content Hub REST API.
2. [Log in to your Coveo organization](https://platform.cloud.coveo.com).
3. [Create and configure a REST API source](https://docs.coveo.com/en/1896/).
   1. In the **Authentication** section, enter your previously created token in the API key field.
   2. Under **Content to Include**, enter your source JSON configuration. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Sitecore%20Content%20Hub/SourceJSONConfig.json) as a base.
   3. Make sure you replace the `{Your Content Hub Domain}` placeholder with your site's URL.
   4. Add or update the `Endpoints` section according to your data structure in Sitecore Content Hub.
4. [Create the appropriate fields and mappings](https://docs.coveo.com/en/1896/#completion).
5. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

[Sitecore Content Hub REST API documentation](https://doc.sitecore.com/ch/en/developers/cloud-dev/rest-api.html)

[REST API source concepts](https://docs.coveo.com/en/3131/)

[REST API source reference](https://docs.coveo.com/en/1525/)
