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
3. Activate the Feature Flag: `Generic rest permissions config`.
4. To index your Workplace by Facebook content, you will need to [create three Generic REST API sources](https://docs.coveo.com/en/1896/): one for the content that supports incremental indexing, two for the content that does not support incremental indexing. For each source you create, follow steps 4 to 7.

5. In the **Authentication** section, enter your Workplace by Facebook access token under **API key authentication**.

6. In the **Content to include** section, paste one of the following configurations:

    - For your first non incremental indexing source, enter the [NormalConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/NormalConfig.json) configuration.

    - For your second incremental indexing source, enter the [MembersInfoConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/MembersInfoConfig.json) configuration.

    - For the incremental indexing source, enter the [IncrementalConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/IncrementalConfig.json) configuration.

6. (Optional) After saving the source, and you forgot to change the security setting: Now change the `createSecurityProvider.py` script.
   - Change the `organizationId`, `sourceId` and the `authToken`.
   - Execute the script. This will create a security provider for your source.

7. Add the [SecurityConfig.json](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/index/SecurityConfig.json) security configuration to the JSON configuration you provided at step 5. 

8. Ensure you've replaced all placeholders (e.g., `solutions788` in the URIs) in the configuration with your own values.

9. Once you've create all three sources, [schedule a refresh operation](https://docs.coveo.com/en/1933/) every 10 minutes for your incremental indexing source.

10. [Add](https://docs.coveo.com/en/1645/) the [FixFacebookURL.py](https://github.com/coveooss/connectivity-library/blob/master/WorkplaceByFacebook/FixFacebookURL.py) indexing pipeline extension to your organization.

11. [Apply this extension](https://docs.coveo.com/en/1936/) to your incremental indexing source.

12. [Create the appropriate fields and mappings](https://docs.coveo.com/en/1896/#completion).


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
* [Meta for Developers: Custom Integrations](https://developers.facebook.com/docs/workplace/custom-integrations-new/)
* [Meta for Developers: Reference](https://developers.facebook.com/docs/workplace/reference)
* [Meta for Developers: Graph API Overview](https://developers.facebook.com/docs/graph-api/using-graph-api)
* [Meta for Developers: Graph API Community](https://developers.facebook.com/docs/workplace/reference/graph-api/community)
* [GitHub: Workplace From Facebook Platform API samples for Postman](https://github.com/fbsamples/workplace-platform-samples/tree/master/SampleAPIEndpoints/Postman)

## Version
1.0 Feb 2021, Wim Nijmeijer
