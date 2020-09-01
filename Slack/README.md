# Indexing Slack using the Generic REST API Connector

## Use case
This examples shows you how to index Slack.

## Pre-requisites
To fully understand how to use this example, you must:
1. Have a Coveo platform organization
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/cloud-v2-administrators/add-or-edit-a-source-using-one-of-the-available-connectors)
3. Learn [how to configure a Generic REST API Connector](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source)

**Important disclaimers:**
* While it makes sense in theory to make all the info that is shared through Slack searchable, there are many downsides that should be considered.
* Indexing Slack means:
    * A lot of small documents in the index
    * The excerpt of the document will be the actual message itself, leading to a lot of noise
    * Relevancy will most likely be bad since it will introduce a lot of noise for most search terms will return results for what people talked about in Slack (just imagine what happens when you use the slack search)
    * ML will have a hard time to learn since
    * You'll probably never click on slack results, you'll just read the excerpt
    * A lot of small documents means that not much clicks will be generated per documents (especially if you index private channel and DMs) 
    * This will lead to large sources increasing the number of documents in the index which will keep growing over time.

One use case that could make sense is to index only the pinned messages of some specific corporate channel where you know that the information is well structured, public and relevant for all.

## Step-by-step guide
1. [Create a bot app](https://api.slack.com/authentication/basics#calling).
2. Assign permissions to the app and generate a token: Under OAuth & Permissions, assign the channels:read and channels:history scopes and get the bot token. You'll need be able to install the app in your Slack.
3. Find your Slack ID: Open your Slack in a browser and take the ID right after /client/ in the URL. You'll need it to generate clickable links.
4. Invite your app in channels that you want to index: If you take this approach of using an app (which is the recommended way according to Slack's documentation) you'll need to invite the app to the channels you wish to index.
5. Create a Generic REST API source.
4. On the authentication section paste your token on the API Key section (provided in step 2).
5. Configure your Generic REST API source according to the example in SourceJSONConfig.json. 
    * This example has one endpoint to get the Channels, which includes a Subquery to get the Messages of each channel, and another endpoint to get the Members.
6. Make sure you've changed all "placeholders" with your own values, and have adjusted the configuration to your own needs.
7. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/cloud-v2-administrators/add-or-edit-a-generic-rest-api-source#completion).

### Other possible features:
* **Index pinned messages:** When querying for the channel messages you could filter on pinned messages by only indexing message that have the "pinned_to" key in the JSON.
* **Index and group threads:** Thread replies will be of "subtype" thread_broadcast and have the parent message ID under root. client_msg_id

## References:
* [Legacy token](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens#-internal-app-tokens)
* [OAuth](https://api.slack.com/docs/oauth)
* [API](https://api.slack.com/methods/conversations.history)