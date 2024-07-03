# Indexing Contentful using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file in a [REST API source](https://docs.coveo.com/en/1896/) to index assets. Your Coveo source will use this JSON configuration to customize HTTP requests for the Contentful Content Delivery API and identify the specific content to extract from the responses.

## Advisory

When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the [Coveo Administration Console](https://docs.coveo.com/en/1841/), Coveo may recommend, or not recommend, using a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites

To fully understand and effectively use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

1. Get a Content Delivery API key from Contentful for the [Authentication](https://www.contentful.com/developers/docs/references/authentication/). Make sure the API key has access to the space you want to index.

2. Get the [space id](https://www.contentful.com/help/find-space-id/) from Contentful.

3. [Create a REST API source](https://docs.coveo.com/en/1896/).

4. In the **Authentication** section, enter your API key under **API key authentication**.

5. In the **Content to include** section, paste the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) file.

6. After saving your config, click on your source and hit `edit JSON`.
Add in the parameter section (normally the parameter is already there):
   ```json
   "parameters": {
         "RetryWaitTimeCushion": {
           "sensitive": false,
           "value": "50"
         },
   ```
   The above will add a `50 seconds` wait time when an `HTTP 429` code is received.

7. [Create the appropriate Coveo Platform fields](https://docs.coveo.com/en/1896/#completion).

   The following custom fields must be created:
   | Field        | Type           |
   | ------------- |-------------|
   | id       | string |
   | description   | String |
   | filename | String      |

   The custom fields must have these exact names for the automatic mapping of retrieved metadata to work.

8. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Content indexed

* Assets

Attachments are completely downloaded and full text indexed.

## Security indexed

All content is public.

## Reference

- [Contentful API documentation](https://www.contentful.com/developers/docs/)
- [Contentful assets collection](
https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/assets/assets-collection)
- [Contentful authentication](https://www.contentful.com/developers/docs/references/content-management-api/#/introduction/authentication)

## Version

1.0 Dec 2021, Wim Nijmeijer
