# Indexing Slack using the Coveo REST API connector
This guide explains how you can use the content of the [`SourceJSONConfig.json`](SourceJSONConfig.json) in a [REST API](https://docs.coveo.com/en/1896/) source to index channels, messages, and users. Your Coveo source will use this JSON configuration to customize HTTP requests for the Slack API and identify the specific content to extract from the responses.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When [adding a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source), Coveo may recommend, or not recommend, using one of these source types along with the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

However, please note that all configurations in this library, including those recommended in the Coveo Administration Console, aren't actively maintained or officially supported. Consider them as starting points that will require customization to fit your specific use case.

## Prerequisites
To fully understand how to use the example JSON configuration, you must:
- Have a [Coveo organization](https://docs.coveo.com/en/185). Don't have a Coveo organization yet? [Sign up for a free trial](https://www.coveo.com/en/free-trial?utm_marketing_tactic=connectivity_library).
- Learn about [Coveo connectivity](https://docs.coveo.com/en/1702).
- Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Important
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
5. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter the token you obtained at step 2.
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
