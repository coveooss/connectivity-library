# Indexing Azure Blob Storage using the Coveo REST API connector

This guide explains how you can use the content of the [`GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json`](GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json) or [`GenericRestToCrawlPublicAzureBlobs.json`](GenericRestToCrawlPublicAzureBlobs.json) files in a [REST API source](https://docs.coveo.com/en/1896/) to index Azure Blob Storage content. Your Coveo source will use this JSON configuration to customize HTTP requests for the Microsoph Graph v1.0 API and identify the specific content to extract from the responses. Please refer to the [REST API source reference](https://docs.coveo.com/en/1525/index-content/rest-api-source-reference) for more details on the JSON configuration.

In order to successfully create the source JSON configuration, you will need knowledge of Azure's [Azure Blob Storage REST API](https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api), which is the API used in the recipes to retrieve Azure Blob Storage content.

# Public content
To crawl public content or simply test the connector with Azure Blob Storage, [`GenericRestToCrawlPublicAzureBlobs.json`](GenericRestToCrawlPublicAzureBlobs.json) works out of the box. In order to connect to a different Storage account, the field "Url" in the "Services" node must be modified. To select which Blob container to retreive within the account, the field "Path" within the "Endpoints" node must be modified.

# Private and secured content
To crawl private and/or secured content, start from the [`GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json`](GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json) recipe. The difference in this recipe is the inclusion of the "Authentication" node in the JSON configuration. To authenticate, we use the client_credentials OAuth flow. In order to successfully complete this authentication flow, an application was registered within Microsoft Entra.


