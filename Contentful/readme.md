# Indexing Contentful Using the Generic REST API Connector

## Use Case
This shows how to index Contentful.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Get an (Content Delivery) API Key from Contentful for the [Authentication](https://www.contentful.com/developers/docs/references/authentication/). Make sure the API Key has access to the space you want to index.

2. Get the [space id](https://www.contentful.com/help/find-space-id/) from Contentful.
 
3. To index your Workplace by Facebook content, you will need to [create one Generic REST API sources](https://docs.coveo.com/en/1896/).

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
The above will add a `50 seconds` wait time when a `HTTP 429` code is received.

7. [Create the appropriate fields and mappings](https://docs.coveo.com/en/1896/#completion).


## Content indexed
* Assets


Attachments are completely downloaded and full text indexed.


### Custom fields
The following custom fields must be created:
| Field        | Type           | Features  |
| ------------- |-------------|-----|
| id       | string |  |
| description   | String | |
| filename | String      |     |


## Security indexed
All content is public



## Reference
https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/assets/assets-collection

https://www.contentful.com/developers/docs/references/content-management-api/#/introduction/authentication



## Version
1.0 Dec 2021, Wim Nijmeijer
