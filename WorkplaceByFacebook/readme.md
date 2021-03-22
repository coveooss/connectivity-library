# Indexing Workplace by Facebook Using the Generic REST API Connector

## Use Case
This shows how to index Workplace by Facebook.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Create a Custom Integration into Workplace by Facebook](https://developers.facebook.com/docs/workplace/custom-integrations-new/).
2. Make sure the Integration has the following access: Read group content, Read user timeline, Read user email, Read group membership, Read all messages, Create link previews, Read work profile, Manage Knowledge Library content, and Manage work profiles.

3. Use the `Access Token` as `API Key` in your Generic Rest configuration.
4. [Create 3 Generic REST API Sources](https://docs.coveo.com/en/1896/). One for the content which supports incremental indexing, two for the content which does not support incremental indexing. 
5. Use in the three sources the security setup in [SecurityConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/SecurityConfig.json). 
6. Add the [MembersInfoConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/MembersInfoConfig.json) in one of the non incremental indexing source.
7. Add the  [IncrementalConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/IncrementalConfig.json). To the 'Incremental indexing' source. Make sure to setup an incremental indexing schedule for every 10 minutes.
8. Add the  [NormalConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/NormalConfig.json). To the other non incremental source.
9. Add the Extension script [FixFacebookURL.py](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/FixFacebookURL.py) to your organization.
10. Assocatie the Extension script to the `Incremental Source`.
11. Make sure you've changed all placeholders (such as `solutions788` in configs' Uris) in the configuration with your own values.
12. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Content indexed
* Groups (documenttype `GroupFB`)
* Groups > Posts (documenttype `PostFB`)
* Groups > Posts > Attachments (documenttype `AttachmentFB`)
* Groups > Posts > Comments (documenttype `CommentFB`)
* Groups > Docs (documenttype `DocFB`)
* Groups > Events (documenttype `EventFB`)
* Groups > Albums (documenttype `AlbumFB`)
* KnowledgeArticles (documenttype `KnowledgeFB`)
* Events (documenttype `WorkplaceEvents`). Events can be for specific groups or for the entire workplace.
* Members Infos (documenttype `WorplaceMember`, Manager(s), Reporter(s), Group(s), position...)


Attachments are completely downloaded and full text indexed.

Comments can contain nested comments, they are indexed as a single comment item (comment + nested comments).

** Only Posts supports incremental indexing, be-aware of the duplicate entries in `RefreshEndpoints` **

### Folding
For Posts with Comments & Attachments folding is enabled.
For both the field `foldingcollection` is defined. For the parent (Posts), the field `foldingparent` is defined. For the childs (comments, attachments) the field `foldingchild` is defined.

### Custom fields
The following custom fields must be created:
| Field        | Type           | Features  |
| ------------- |-------------|-----|
| id       | string |  |
| groupid  | Integer 64 | |
| postid   | String | |
| mediaurl | String      |     |
| iconurl  | String     | |
| mymessage | String  | Free Text, Ranking, Stemming |
| mystory   | String  | Free Text, Ranking, Stemming |


## Security indexed
Workplace by Facebook is using security based upon Community Members and Group Members. The configuration indexes both.

## Limitation
Nested community groups are not supported

## Special attention
Posts can contain a message and/or a story. The field `mymessage` and/or `mystory` is added to the content. `message` is a better fit, so if that is there, use that one.

## Reference
https://developers.facebook.com/docs/workplace/custom-integrations-new/

https://developers.facebook.com/docs/workplace/reference

https://developers.facebook.com/docs/graph-api/using-graph-api

https://github.com/fbsamples/workplace-platform-samples/tree/master/SampleAPIEndpoints/Postman

https://developers.facebook.com/docs/workplace/reference/graph-api/community


## Version
1.0 Feb 2021, Wim Nijmeijer
