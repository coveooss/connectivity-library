# Indexing Sitecore Content Hub Using the Generic REST API Connector

## Use Case
This example shows how to index Sitecore Content Hub.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo organization.
2. Learn about [Coveo connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create a token](https://doc.sitecore.com/ch/en/developers/42/cloud-dev/rest-api--get-token.html) to access the Content Hub REST API.
2. [Log in to your Coveo organization](https://platform.cloud.coveo.com).
3. Under **Sources**, [create a Generic REST API source](https://docs.coveo.com/en/1896/):
    1. In the **Authentication** section, enter your previously created token in the API key field.
    2. Under **Content to Include**, enter your source JSON configuration. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Sitecore%20Content%20Hub/SourceJSONConfig.json) as a base.
    3. Make sure you've changed all placeholders in the configuration with your own values:
        1. Replace the URL placeholders with your site's URL.
    4. Add or update the `Endpoints` section according to your data structure in Contentstack.
4. [Create the appropriate fields and mappings](https://docs.coveo.com/en/1896/#completion).
5. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Sitecore Content Hub's REST API documentation](https://doc.sitecore.com/ch/en/developers/42/cloud-dev/rest-api--about.html)