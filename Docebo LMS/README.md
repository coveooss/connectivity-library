# Indexing Docebo LMS using the Generic REST API Connector

## Use case
This example shows how to index Courses, Learning Content (Courses content) and Learning Plans from Docebo LMS

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
1. Ask Docebo admin to create an API app for Coveo (OAuth). You'll need a Client ID and a Cient Secret. You can find more information [here](https://www.docebo.com/knowledge-base/how-to-activate-and-manage-the-sso-and-api-app/) and [here](https://www.docebo.com/knowledge-base/authentication-api-ssp-app-grant-types/). **Important note:** With the new 7.0 APIs (found at <<YOUR_LMS>>.docebosaas.com/api-browser/), the system also requires a specific user permission in order to work properly
2. Try generating an access token with Postman or any other REST client. Example with "password" grant type (<yourlms>.docebosaas.com/oauth2/token)
3. Test your access token with the course endpoint YOURLMS.docebosaas.com/api/learn/v1/courses
4. Create a Generic REST API source
5. On the authentication section, paste your Client ID, Client Secret, Username and Password (provided in step 1)
6. Configure your Generic REST API source according to the example in SourceJSONConfig.json. This configuration uses two Endpoints. One to get the Courses, using a Subquery to get the Course Content, and a second endpoint to get the Learning Plans.
7. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
8. Create the appropiate fields and mappings