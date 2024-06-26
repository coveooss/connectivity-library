# Pendo API response examples

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