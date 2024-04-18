# Indexing Sitecore Content Hub Using the REST API Connector

## Use Case
This example shows how to index Sitecore Content Hub.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo organization.
2. Learn about [Coveo connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create a token](https://doc.sitecore.com/ch/en/developers/42/cloud-dev/rest-api--get-token.html) to access the Content Hub REST API.
2. [Log in to your Coveo organization](https://platform.cloud.coveo.com).
3. Under **Sources**, [create a REST API source](https://docs.coveo.com/en/1896/):
    1. In the **Authentication** section, enter your previously created token in the API key field.
    2. Under **Content to Include**, enter your source JSON configuration. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Sitecore%20Content%20Hub/SourceJSONConfig.json) as a base.
    3. Make sure you replace the `{Your Content Hub Domain}` placeholder with your site's URL.
    4. Add or update the `Endpoints` section according to your data structure in Sitecore Content Hub.
    5. See the [Understanding the `SourceJSONConfig.json` file](#understanding-the-sourcejsonconfig-json-file) section for explanations on the key aspects of the configuration.
4. [Create the appropriate fields and mappings](https://docs.coveo.com/en/1896/#completion).
5. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Understanding the `SourceJSONConfig.json` file

The following are a few pointers to help you understand the example JSON configuration:

### Authenticating calls to the Content Hub API

All calls to the Sitecore Content Hub performed in the configuration [inherit](https://docs.coveo.com/en/3131/#inheritable-properties) the `X-Auth-Token` header property.
The `@ApiKey` syntax is used to retrieve the `API key` field value from the REST source user interface [Authentication section](https://docs.coveo.com/en/1896/#authentication-section).

<img src="images\GenericRestApiKeyConfig.png" width="600" alt="Configuring authentication for calls to Content Hub API | Coveo">

### Setting the main HTTP call method and URL

A main GET call is performed against the Content Hub [query](https://doc.sitecore.com/ch/en/developers/42/cloud-dev/rest-api--query.html) endpoint. The full call URL is obtained by concatenating the JSON configuration `service` [`url`](https://docs.coveo.com/en/1525/#url-string-required), the `endpoint` [`path`](https://docs.coveo.com/en/1525/#path-string-required), and the [Content Hub parent relationship](https://doc.sitecore.com/ch/en/developers/40/cloud-dev/rest-api--relations.html) query string [`queryParameter`](https://docs.coveo.com/en/1525/#queryparameters-object).

<img src="images\GenericRestEndpointUrlConfig.png" width="600" alt="Content Hub API query resource URL configuration | Coveo">

### Telling Coveo how to parse the Content Hub API response object

The configuration [`itemPath`](https://docs.coveo.com/en/1525/#itempath-string) value tells Coveo where the document objects are located in the Content Hub API response object.

<img src="images\GenericRestItemPathConfig.png" width="600" alt="Setting the itemPath parameter | Coveo">

### Populating metadata for Coveo default fields

Under the `endpoints` property, metadata that's automatically [mapped](https://docs.coveo.com/en/217/) to Coveo [default fields](https://docs.coveo.com/en/2036/#default) is populated with either static values (e.g., `itemType`) or [dynamic values](https://docs.coveo.com/en/3131/#dynamic-values) retrieved from the Content Hub API JSON response (e.g., `uri`, `clickableUri`).

<img src="images\GenericRestOOTBMetadataConfig.png" width="600" alt="Populating metadata for Coveo default fields | Coveo">

### Creating and populating custom metadata

Under the `metadata` property, custom metadata names are defined.
This metadata is populated with dynamic values retrieved from the Content Hub API JSON response.

<img src="images\GenericRestCustomMetadataConfig.png" width="600" alt="Creating and populating custom metadata | Coveo">

---
**TIP**

Use your custom metadata to [populate fields](https://docs.coveo.com/en/1896/#completion).
These fields can then be used in search interface [facets](https://docs.coveo.com/en/198/) and [result templates](https://docs.coveo.com/en/atomic/latest/reference/result-template-components/atomic-result-fields-list/) to enhance the search experience.

---

### Specifying whether to index the main GET call items

No item from the `endpoints` level is actually indexed with [`ActionOnItem`](https://docs.coveo.com/en/1525/#actiononitem-string-required) set to `Ignore` and no [`Condition`](https://docs.coveo.com/en/1525/#action-condition-string) specified.
Only [some sub-items are indexed](#indexing-sub-items-on-a-conditional-basis) in the REST API source.

<img src="images\GenericRestActionOnItem.png" width="600" alt="ActionOnItem value | Coveo">

### Referencing parent metadata and main GET call response data

Sub-items are created by performing GET calls.
For each sub-item, the `path` property value determines the sub-item GET call URL and this value is retrieved from the main GET call response items, as indicated by the combined use of the [`coveo_parent`](https://docs.coveo.com/en/3131/#coveo_parent) and [`raw`](https://docs.coveo.com/en/3131/#raw) dynamic values.
When used without `raw`, `coveo_parent` references a property from the `endpoint` (i.e., the parent) `metadata` properties.
Of all the sub-item metadata, only the `assettopubliclinkchildren` property value actually comes from the sub-item GET call response.

<img src="images\GenericRestSubItems.png" width="600" alt="Creating sub-items | Coveo">

### Indexing sub-items on a conditional basis

A sub-item is indexed only if its parent's `donotshow` metadata value is `'False'`.

<img src="images\GenericRestSubItemsActionOnItem.png" width="600" alt="Sub-items ActionOnItem value | Coveo">

## Reference

[Sitecore Content Hub REST API documentation](https://doc.sitecore.com/ch/en/developers/cloud-dev/rest-api.html)

[REST API source concepts](https://docs.coveo.com/en/3131/)

[REST API source reference](https://docs.coveo.com/en/1525/)
