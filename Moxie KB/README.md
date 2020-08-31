# Indexing Moxie KB using the Generic REST API Connector

## Use case
This example shows how to index Moxie Knowledge Base Articles.

## Pre-requisites
In order to fully understand and use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. You will need to make 4 API calls:
    * Get Article List (NewlyPublished) – one call per rebuild
    * Get Article List (RecentlyUpdated) - one call per rebuild
    * Get Article (one call per document)
    * Get Article Metadata (one call per document)
2. You should have a Client ID, API Key and a Profile ID.
3. Create a Generic REST API Source.
4. On the authentication section add your credentials (ClientID, API Key).
5. Configure your Generic REST API source according to the example in SourceJSONConfig.json 
    * This example retrieves the list of articles using the main endpoint, the body using subquery and metadata using another subquery).
    * If you need to test API calls, you may use Postman, but Moxie also usually makes a visual widget available to try calls. The url should be something like restapi-customername.kb.net/Widgets/Admin.
        * The widgets you need to replicate what the REST config below does are
            * Get Article List (button "Get Newly Published Article")
            * Get Article List (button "Get Recently Updated Published Article")
            * Get Article 
            * Get Article Metadata
        * If using Chrome, you must open Chrome Dev Tools to see some of those calls results:
    * **Important note:** There are two endpoints that carries same parameters, if you modify/reuse it don't forget to update both enpoints parameters the same way. The two parameters are NewlyPublished (for new articles), and RecentlyUpdated (for new versions of existing articles). When an article is updated with a new version, its record will cease to be part of the NewlyPublished list.
6. Make sure you've changed all "placeholders" with your own values, and to adjust the configuration to your own needs.
7. Use an Indexing Pipeline Extension (example: IPE.py) to transform the date of the article version (because of a trailing Z character).
8. Create the appropiate fields and mappings.