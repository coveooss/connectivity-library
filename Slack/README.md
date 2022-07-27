# Indexing Slack Using the Generic REST API Connector

## Use Case
This examples shows you how to index Slack.

## Prerequisites
To use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Important Disclaimer
While it theoretically makes sense to make all the information shared through Slack searchable, there are many downsides that should be considered. Indexing Slack content means that:
    * In your search interface, the excerpt of a Slack item will be the message itself, leading to a lot of noise.
    * Relevance will most likely be poor since most search terms will return Slack messages, thus introducing a lot of noise.
    * Machine Learning won't have a lot of click data to learn from since:
       * End users will probably never click on Slack results, they'll just read the excerpt.
       * Your index will contain a multitude of small items, and therefore very few clicks will be generated per document, especially if you index private channels and direct messages.
    * Your Slack source will eventually get very large, and the number of items in your index will keep growing rapidly.

A more practical use case for indexing Slack messages would be to index only the pinned messages of a specific corporate channel where you know that the information is well structured, public, and relevant for all.

## Instructions
1. [Create a Slack bot application](https://api.slack.com/authentication/basics#calling).
2. Assign permissions to the application and generate a token:
   1. Under **OAuth & Permissions**, assign the `channels:read` and `channels:history` scopes and get the bot token. You'll need it to install the application on your Slack instance.
3. Find your Slack ID: open Slack in a browser window and, in the URL, take the ID right after `/client/`. You'll need it to generate clickable links.
4. Invite your application in the channels that you want to index.
5. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter the token you obtained at step 2.
6. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Slack/SourceJSONConfig.json) as a base to build your source JSON configuration. This example has one endpoint to get the Slack channels, which includes a subquery to get the messages in each channel, and another endpoint to get the members. Adjust the configuration example to your own needs.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
9. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

### Alternative Options
* Index pinned messages: when querying for the channel messages, index only the messages that have the `pinned_to` key in the JSON.
* Index and group threads: thread replies are of "subtype" `thread_broadcast` and have the parent message ID under `root.client_msg_id`.

## Reference
* [Legacy token](https://get.slack.help/hc/en-us/articles/215770388-Create-and-regenerate-API-tokens#-internal-app-tokens)
* [OAuth](https://api.slack.com/docs/oauth)
* [API](https://api.slack.com/methods/conversations.history)
