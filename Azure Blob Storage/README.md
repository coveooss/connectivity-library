# Indexing Azure Blob Storage Using the REST API Connector

## Use Case

This example shows how to index Azure Blob Storage files from a specific container.

- List Blobs in the container: `&restype=container&comp=list`
- `maxresults`: maximum number of results to fetch
- return: `NextMarker` for next call
- then use `marker` parameter in URI
- Get the actual blob is using the container name + the name of the document

## Enable logging in your JSON of the source

Add to the `parameters`:

```json
 "Log4netLoggers": {
        "value": "{ \"Coveo.Connectors.GenericRest\": \"TRACE\", \"Coveo.CES.CustomCrawlers.GenericRest\": \"TRACE\", \"Coveo.Platform\": \"TRACE\" }"
      },
      "Log4netAppenderName": {
        "value": "AsyncBufferingForwardingAppender"
      },
```

## Prerequisites

To fully understand how to use this example, you must:

1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions

1. [Create an Access Policy](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/accesspolicy/storageAccountId/). Make sure to enable `Read` and `List`.
2. [Create an Shared Access Token](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/sas/storageAccountId). Use Stored Access Policy from Step 1.
3. Generate SAS token and URL. Use the Blob SAS URL for the Generic Rest Configuration.
4. Create a REST API source.
5. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Azure%20Blob%20Storage/Config.json) as a base to build your source JSON configuration. Replace the [YOURSTORAGE] and [CONTAINER] to your own. Also replace all the SAS token parameters in all requests.
6. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Limitation

Content [refresh](https://docs.coveo.com/en/2039/#refresh) isn't possible, not supported by the `List Blobs` API call.

## Reference

[Azure Storage API documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs?tabs=azure-ad)
