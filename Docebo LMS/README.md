# Indexing Docebo LMS using the Generic REST API Connector

1) Ask Docebo admin to create an API app for Coveo (OAuth). We need a Client ID and a Cient Secret. You can send these links: 
- https://www.docebo.com/knowledge-base/how-to-activate-and-manage-the-sso-and-api-app/
- https://www.docebo.com/knowledge-base/authentication-api-ssp-app-grant-types/
- Please Note: With the new 7.0 APIs (found at YOURLMS.docebosaas.com/api-browser/), the system also requires a specific user permission in order to work properly

2) Try generating an access token with Postman or any other REST client. Example with "password" grant type
<yourlms>.docebosaas.com/oauth2/token

3) Test your access token with the course endpoint YOURLMS.docebosaas.com/api/learn/v1/courses
 

4) Add a Generic REST source JSON Config


About the config:
This example config will retrieve:
* Courses 
* Learning Content (Courses content)
* Learning Plans