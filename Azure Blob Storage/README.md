# Indexing Azure Blob Storage using the Coveo REST API connector

This guide explains how you can use the content of the [`GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json`](GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json) or [`GenericRestToCrawlPublicAzureBlobs.json`](GenericRestToCrawlPublicAzureBlobs.json) files in a [REST API source](https://docs.coveo.com/en/1896/) to index Azure Blob Storage content. Your Coveo source will use this JSON configuration to customize HTTP requests for the Microsoph Graph v1.0 API and identify the specific content to extract from the responses. Please refer to the [REST API source reference](https://docs.coveo.com/en/1525/index-content/rest-api-source-reference) for more details on the JSON configuration.

In order to successfully create the source JSON configuration, you will need knowledge of Azure's [Azure Blob Storage REST API](https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api), which is the API used in the recipes to retrieve Azure Blob Storage content.

# Public content
To crawl public content or simply test the connector with Azure Blob Storage, [`GenericRestToCrawlPublicAzureBlobs.json`](GenericRestToCrawlPublicAzureBlobs.json) works out of the box. In order to connect to a different Storage account, the field "Url" in the "Services" node must be modified. To select which Blob container to retreive within the account, the field "Path" within the "Endpoints" node must be modified.

# Private and secured content
To crawl private and/or secured content, start from the [`GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json`](GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json) recipe. The difference in this recipe is the inclusion of the "Authentication" node in the JSON configuration. To authenticate, we use the client_credentials OAuth flow. In order to successfully complete this authentication flow, an application was registered within Microsoft Entra. The following scope provides sufficient right to crawl the content of Azure Blob Storage:
![AzureBlobStorageAppPermissions](https://github.com/user-attachments/assets/ca6bbfc2-fc77-4c62-bb76-b6f8ab3e9cbb)

Once the application is properly created, 2 more information are required in the source configuration for authentication to work: the Client Id and Client Secret values

![AzureBlobStorageSource](https://github.com/user-attachments/assets/21f574f5-9031-437c-a518-61e8911d59d5)

The client Id of your Azure Blob Storage app can be found in its main overview in Microsoft Entra

![AzureBlobStorageClientId](https://github.com/user-attachments/assets/509f0cdd-f4fe-4aed-958c-add65f19214b)

Finally, the client secret must be created and its sensitive value will be available and added to the source in the proper parameter (Do not put it in clear text in the JSON configuration, the @clientId and @clientSecret are there for replacement purposes!)

![AzureBlobStorageClientSecret](https://github.com/user-attachments/assets/080cd460-f19d-4031-b76e-2b979465c62e)
