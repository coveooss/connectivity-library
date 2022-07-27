# Indexing Contentstack Using the Generic REST API Connector

## Use Case
This example shows how to index Contentstack. It is based on the sample from Contentstack with Blogs and Authors.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Login to Contentstack](https://app.contentstack.com/).
2. Find the _Stack_ you want to index.
3. In _Settings_/_Tokens_, create a Management Token. Take note of the Api Key and the Management Token. [Detailed instructions](https://www.contentstack.com/docs/developers/create-tokens/generate-a-management-token/)
4. Test the authentication on Postman:
    * Contentstack has a Postman collection. Find the "`Run in Postman`" button in https://www.contentstack.com/docs/developers/apis/content-management-api/
5. [Login to your Coveo organization](https://platform.cloud.coveo.com).
    1. Under _Sources_, create a Generic REST API source. 
    2. In the **Authorization** section of the configuration UI, set your _Api Key_.
    3. In the **Content to Include**, paste the JSON of the config
    4. Make sure you've changed all placeholders in the configuration with your own values.
        1. Set your _Management Token_ in all `headers` sections
        2. Update the URLs to your site in the JSON 
    5. Add/Update _Endpoints_ according to your data structure in Contentstack
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Contentstack's Content Management API](https://www.contentstack.com/docs/developers/apis/content-management-api/)
