# Indexing Google Sheets using the Generic REST API Connector

## Use case
This examples shows you how to index the information on a Google Sheet.
## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

## Step-by-step guide
To connect you must:

1. Create a new project in https://console.developers.google.com/
2. Enable the Google Sheets API on your project <https://support.google.com/googleapi/answer/6158841?hl=en>
3. Create Authorization Credentials <https://developers.google.com/sheets/api/guides/authorizing>
4. Obtain Oauth 2.0 access tokens
    a. Run the following url from an incognito browser page: <https://accounts.google.com/o/oauth2/v2/auth?response_type=code&scope=https://www.googleapis.com/auth/spreadsheets.readonly&client_id=[YOUR_CLIENT_ID]&redirect_uri=https://localhost:8080&access_type=offline>
    b. Log in with the user with which you created the project.
    c. Approve access to Google Sheets.
    d. In the returned page (that says it can’t be reached), look at the URL, and copy the value for the code query parameter. Ex.: 4/tQGh5NYllICGM5Bq_NE1jiYEAryac_k9t2mTJkde0LnXWHdbl2hP9s4ktAbk2YEPAeRsgjDMkrHORYM6gDpK1SE IMPORTANT: Such a code can be used only once. You must repeat steps 1 to 4 to get another one. 
    e. Using Postman, or a similar solution, exchange authorization code for refresh and access token. This should return a JSON File with the access token and refresh token. 
       {
        "access_token": "YOUR_ACCESS_TOKEN",
        "expires_in": 3600,
        "refresh_token": "YOUR_REFRESH_TOKEN",
        "scope": "https://www.googleapis.com/auth/spreadsheets.readonly",
        "token_type": "Bearer"
        }

The obtained refresh_token will then be used to complete the Generic REST API source configuration. The refresh token enables your application to obtain a new access token if the one that you have expires. As such, if your application loses the refresh token, the user will need to repeat the OAuth 2.0 consent flow so that your application can obtain a new refreshtoken.
