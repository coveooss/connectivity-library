# Connectivity Library
The Coveo GitHub Connectivity Library is an open source repository containing JSON configuration examples. These examples allow you to index popular systems that Coveo doesn't provide a [native connector](https://docs.coveo.com/en/1702/#native-connectors) for, but which expose a REST or GraphQL API. Copy the content of the relevant JSON configuration file from this library and paste it directly into your [Coveo Platform](https://docs.coveo.com/en/3361/) [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source **JSON configuration** box.

## Disclaimer
When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

> [!NOTE]
> If you want to index a repository that doesn’t appear in the library, it's quite possible you'll be able to do so using one of Coveo's [generic connectors](https://docs.coveo.com/en/1702/#generic-connectors).

## Requirements
To use the configuration examples in this library you must have:
* A [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
* Basic knowledge of the Coveo [REST API](https://docs.coveo.com/en/1896/) and [GraphQL API](https://docs.coveo.com/en/n6gh2329/) sources.
