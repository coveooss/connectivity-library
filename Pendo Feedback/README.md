# Indexing Pendo Feeback (Formerly Receptive.io) Using the Generic REST API Connector

## Use Case
This example shows how to retrieve Features(cases) submit to the [Pendo Feedback](https://app.pendo.io/) platform and the comments on each Feature.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Get a Pendo Feeback API key](https://support.pendo.io/hc/en-us/articles/360042025452-Salesforce-Integration-Setup-for-Feedback#h_6cb2d977-ee2b-4b8f-aa24-66455c2d4b9d).
2. [Create a Generic REST API](https://docs.coveo.com/en/1896/) source and, in the **Authorization** section, provide the API key obtained in step 1.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Pendo%20Feedback/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Pendo Feedback API Specifics
* [API Documentation](http://apidoc.receptive.io/)
* Retrieving Feature views and vote counts from the API requires retrieving the individual features in a sub query. This is not optimal, so if you don't need the view count in the search results, you can omit the sub queries.
You can use the sub query if you need additional data from Features, just add the metadata fields that are missing.
* In the example JSON configuration private Feedback and private comments are ignored. You can remove the  `IndexingAction` if you want to include `private` items.

### Response Examples

`{{baseUrl}}/features?`
```
[
    {
        "id": 55555,
        "title": "",
        "description": "",
        "resolution": null,
        "status": "",
        "vendor_id": 55555,
        "created_by_user_id": 555555,
        "updated_by_user_id": null,
        "resolved_by_user_id": null,
        "app_url": "",
        "form_entry": "",
        "created_at": "",
        "updated_at": "",
        "declined_at": null,
        "developing_at": null,
        "planned_at": null,
        "released_at": null,
        "waiting_at": null,
        "status_changed_at": "",
        "seen_case": false,
        "is_private": false,
        "effort": null,
        "products": [
            ""
        ],
        "groups": [],
        "uploads": []
    }
]
```

`{{PENDO_FEEDBACK_URL}}/features/:id`
```
{
    "id": ""
    "title": "",
    "description": "",
    "resolution": null,
    "status": "",
    "vendor_id": 55555,
    "created_by_user_id": 5555555,
    "updated_by_user_id": null,
    "resolved_by_user_id": null,
    "merged_to_case_id": null,
    "form_entry": "",
    "app_url": "",
    "created_at": "",
    "updated_at": "",
    "declined_at": null,
    "developing_at": null,
    "planned_at": null,
    "released_at": null,
    "waiting_at": null,
    "status_changed_at": "",
    "requested_by": {
        "name": null,
        "id": null
    },
    "status_request=": "",
    "merged_to_feature_id": null,
    "vendor_name": "",
    "is_private": false,
    "view_count": 0,
    "effort": null,
    "tags": [],
    "products": [
        ""
    ],
    "groups": [],
    "creator": {
        "name": "",
        "email": "",
        "account": {
            "name": ""
        }
    },
    "uploads": []
}
```

## Reference
[Pendo Feedback API documentation](https://developers.pendo.io/docs/?bash#)
