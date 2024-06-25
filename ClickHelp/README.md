# Indexing ClickHelp using the Coveo REST API connector
This guide explains how you can use the content of the provided JSON file in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index ClickHelp projects and articles. When you'll perform [update operations](https://docs.coveo.com/en/2039/) on your Coveo REST API source, it will use this JSON configuration to perform HTTP requests against the ClickHelp v1 API to extract content.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When searching for a system in the [Add a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel of the Coveo Platform, Coveo may recommend, or not, using one of these source types and the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Coveo recommends the REST API source ClickHelp example JSON configuration herein.

However, please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Generate an [API Key](https://clickhelp.com/software-documentation-tool/user-manual/api-authentication.html) from ClickHelp. To do so, simply navigate your profile and click on "RESET API KEY".
2. [Create a REST API](https://docs.coveo.com/en/1896/) source and, in the **Authorization** section, fill in you username and the API key obtained in step 1. as the password.
3. Use the example in [`SourceJSONConfig.json`](SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs. ClickHelp maintains a parent/child relationship between Project and Articles objects, this leads to a single endpoint to index projects along with SubItem queries to indexed the related Articles objects.
4. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
5. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[ClickHelp API documentation](https://clickhelp.com/software-documentation-tool/user-manual/clickhelp-api.html)
