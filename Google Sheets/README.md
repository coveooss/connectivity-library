# Indexing Google Sheets Using the REST API Connector

## Use Case
This examples shows you how to index the information on a Google Sheet.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create a new Google Cloud Platform project](https://console.developers.google.com/).
2. [Enable the Google Sheets API on your project](https://support.google.com/googleapi/answer/6158841?hl=en).
3. [Create authorization credentials](https://developers.google.com/sheets/api/guides/authorizing).
4. Obtain OAuth 2.0 access tokens:
    1. Open the following link in private browsing mode: https://accounts.google.com/o/oauth2/v2/auth?response_type=code&scope=https://www.googleapis.com/auth/spreadsheets.readonly&client_id=<YOUR_CLIENT_ID>&redirect_uri=https://localhost:8080&access_type=offline.
    2. Log in with the user account with which you created the project in step 1.
    3. Approve access to Google Sheets.
    4. In the URL of the returned page (which says it can’t be reached), copy the value for the code query parameter, e.g., `4/xyz`. This code can only be used once.
    5. [Exchange your authorization code for a refresh token](https://developers.google.com/identity/protocols/oauth2/web-server#httprest_3). Use Postman or a similar solution to call the required endpoint.
5. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your client ID, client secret, and refresh token.
6. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Google%20Sheets/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust the configuration example to your own needs.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[Google Sheets API documentation](https://developers.google.com/sheets/api)
