# Indexing Azure Blob Storage using the Coveo REST API connector

This guide explains how you can use the content of the [`GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json`](GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json) or [`GenericRestToCrawlPublicAzureBlobs.json`](GenericRestToCrawlPublicAzureBlobs.json) files in a [REST API source](https://docs.coveo.com/en/1896/) to index Azure Blob Storage content. Your Coveo source will use this JSON configuration to customize HTTP requests for the Microsoph Graph v1.0 API and identify the specific content to extract from the responses. See the [REST API source reference](https://docs.coveo.com/en/1525/index-content/rest-api-source-reference) for more details on the JSON configuration. 

If you are familiar with our REST API connector, you know it expects JSON in the API responses, but Azure Blob Storage returns XML. Thanks to a feature that was added at the end of 2024, the connector will auto-detect an XML response, convert it to JSON automatically, and then proceed normally. You can read more on this feature [in our documentation](https://docs.coveo.com/en/3131/index-content/rest-api-source-concepts#json-path).

To write your source JSON configuration, you will need knowledge of Azure's [Azure Blob Storage REST API](https://learn.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api), which is the API used in the recipes to retrieve Azure Blob Storage content.

# Public content
To crawl public content or simply test the connector with Azure Blob Storage, [`GenericRestToCrawlPublicAzureBlobs.json`](GenericRestToCrawlPublicAzureBlobs.json) works out of the box. To connect to a different Storage account, edit the "Url" in the "Services" node. To select which Blob container to retrieve within the account, edit the "Path" in the "Endpoints" node.

# Private and secured content
To crawl private and/or secured content, start from the [`GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json`](GenericRestToCrawlPrivateAzureBlobsWithClientCredentials.json) recipe. The difference in this recipe is the inclusion of the "Authentication" node in the JSON configuration. To authenticate, we use the `client_credentials` OAuth flow. In order to successfully complete this authentication flow, an application was registered within Microsoft Entra. The following scope provides sufficient rights to crawl the content of Azure Blob Storage:
![AzureBlobStorageAppPermissions](https://github.com/user-attachments/assets/ca6bbfc2-fc77-4c62-bb76-b6f8ab3e9cbb)

Once the application is properly created, the following are required in the source configuration for authentication to work: the authentication URL, the client ID, and the client secret.
![AzureBlobStorageSource](https://github.com/user-attachments/assets/21f574f5-9031-437c-a518-61e8911d59d5)

The authentication URL is formed using your tenant ID, which you can find on the Microsoft Entra ID page on Azure. Replace the placeholder in the "RefreshUrl" node to allow the connector to hit the correct authentication endpoint.
![AzureBlobStorageTenantId](https://github.com/user-attachments/assets/146b0e46-abff-4808-a06a-0084d82c2548)

You can find the client ID of your Azure Blob Storage app in its main overview in Microsoft Entra. Enter your client ID in Coveo's source creation panel, under **Client ID**, and then use `@clientId` as a placeholder in your source JSON configuration. Do not enter your client ID in clear text in the source JSON configuration!
![AzureBlobStorageClientId](https://github.com/user-attachments/assets/509f0cdd-f4fe-4aed-958c-add65f19214b)

Finally, you must create the client secret, and then enter its sensitive value in Coveo's source creation panel, under **Client secret**. Use `@clientSecret` as a placeholder in your source JSON configuration. Do not enter your client secret in clear text in the source JSON configuration!
![AzureBlobStorageClientSecret](https://github.com/user-attachments/assets/080cd460-f19d-4031-b76e-2b979465c62e)

You may notice that both JSON configuration examples include the "x-ms-version" header. This header is mandatory for all requests to Azure Blob Storage and is documented [here](https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-for-the-azure-storage-services). The chosen value may affect what is available to you.

To target your crawling to a specific blob container, replace the placeholder in a few spots in the JSON configuration. The available blob containers can easily be found using the Microsoft Azure Storage Explorer.
![AzureBlobStorageExplorer](https://github.com/user-attachments/assets/67ddb211-40e2-4ce1-93ed-02969c354375)

