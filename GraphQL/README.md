Indexing is done using the Generic REST API connector

The Generic REST API was created to connect to REST APIs, but it can also be used to connect to GraphQL by sending the Query and Variables JSON content as a POST request body using the PayloadJsonContent <https://docs.coveo.com/en/1525/cloud-v2-administrators/generic-rest-api-source-reference#payloadjsoncontent-string> parameter. When setting this parameter, the Content-Type header is automatically set to application/json.

The example included in the SourceJSONConfig.json file is using the Anilist GraphQL. <https://anilist.gitbook.io/anilist-apiv2-docs/overview/graphql>

Note: As indicated in the documentation, since the JSON content is provided as a string value in a JSON configuration, it must be escaped accordingly (\").
