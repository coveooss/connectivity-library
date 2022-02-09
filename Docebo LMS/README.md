# Indexing Docebo LMS Using the Generic REST API Connector

## Use Case
This example shows how to index courses, learning content (courses content) and learning plans from Docebo LMS.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. Ask Docebo administrator to create an API app for Coveo (OAuth 2.0 protocol). You'll need a client ID and a client secret. For more information, see [Activating and Managing the SSO and API App](https://www.docebo.com/knowledge-base/how-to-activate-and-manage-the-sso-and-api-app/) and [APIs Authentication](https://www.docebo.com/knowledge-base/authentication-api-ssp-app-grant-types/). **Important:** With the new 7.0 APIs (found at `<<YOUR_LMS>>.docebosaas.com/api-browser/`), the system also requires a specific user permission.
2. Try generating an access token with Postman or any other REST client. Example with "password" grant type (`<<YOUR_LMS>>.docebosaas.com/oauth2/token`).
3. Test your access token with the course endpoint `<<YOUR_LMS>>.docebosaas.com/api/learn/v1/courses`.
4. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your client ID, client secret, and credentials.
5. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Docebo%20LMS/SourceJSONConfig.json) as a base to build your source JSON configuration. This example uses two endpoints to retrieve courses and learning plans. The course endpoint uses a subquery to get course content. Adjust the configuration example to your own needs.
6. Make sure you've changed all placeholders in the configuration with your own values.
7. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Reference
[Docebo LMS API documentation](https://help.docebo.com/hc/en-us)
