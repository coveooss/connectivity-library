# Indexing Contentful using the Coveo REST API connector
This guide explains how you can use the content of the provided JSON file in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index assets. When you'll perform [update operations](https://docs.coveo.com/en/2039/) on your Coveo REST API source, it will use this JSON configuration to perform HTTP requests against the Contentful Content Delivery API to extract content.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When searching for a system in the [Add a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel of the Coveo Platform, Coveo may recommend, or not, using one of these source types and the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Coveo recommends the REST API Contentful example JSON configuration herein.

However, please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Get an (Content Delivery) API Key from Contentful for the [Authentication](https://www.contentful.com/developers/docs/references/authentication/). Make sure the API Key has access to the space you want to index.

2. Get the [space id](https://www.contentful.com/help/find-space-id/) from Contentful.
 
3. To index your Workplace by Facebook content, you will need to [create a REST API source](https://docs.coveo.com/en/1896/).

4. In the **Authentication** section, enter your API key under **API key authentication**.

5. In the **Content to include** section, paste the following configurations:

    - Enter the [NormalConfig.json](https://github.com/coveooss/connectivity-library/blob/master/Contentful/index/NormalConfig.json) configuration.

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
