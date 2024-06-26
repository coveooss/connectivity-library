# Indexing Google Sheets using the Coveo REST API connector

This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source to index a [specified range in a given sheet](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get). Your Coveo source will use this JSON configuration to customize HTTP requests for the Google Sheets v4 API and identify the specific content to extract from the responses.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) in the Coveo Administration Console, Coveo may recommend, or not recommend, using one of these source types along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

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
