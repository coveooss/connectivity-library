# Indexing Contentstack Using the Generic REST API Connector

## Use Case
This example shows how to index Contentstack. It is based on the sample from Contentstack with Blogs and Authors.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo organization.
2. Learn about [Coveo connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Log in to Contentstack](https://app.contentstack.com/).
2. Find the stack you want to index.
3. Under **Settings** > **Tokens**, [create a management token](https://www.contentstack.com/docs/developers/create-tokens/generate-a-management-token/). Take note of the API key and the management token.
4. Test the authentication on Postman. Use the **Run in Postman** button on the [Content Management API](https://www.contentstack.com/docs/developers/apis/content-management-api/) page.
5. [Log in to your Coveo organization](https://platform.cloud.coveo.com).
6. Under **Sources**, [create a Generic REST API source](https://docs.coveo.com/en/1896/):
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
