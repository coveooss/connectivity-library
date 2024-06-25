# Indexing GitHub using the Coveo REST API connector
This guide explains how you can use the content of the provided JSON files in a [REST API](https://docs.coveo.com/en/1896/) source on the [Coveo Platform](https://docs.coveo.com/en/3361/) to index repositories, branches, and other content types. When you'll perform [update operations](https://docs.coveo.com/en/2039/) on your Coveo REST API source, it will use this JSON configuration to perform HTTP requests against the GitHub REST API to extract content.

This guide covers two use cases:
- Indexing without taking account of permissions.
- Indexing and taking account of permissions.

## Disclaimer
The JSON configuration examples in this library have been used to index the related system with a Coveo [REST API](https://docs.coveo.com/en/1896/) or [GraphQL API](https://docs.coveo.com/en/n6gh2329/) source. When searching for a system in the [Add a source of content](https://docs.coveo.com/en/3390/index-content/add-or-edit-a-source#add-a-source) panel of the Coveo Platform, Coveo may recommend, or not, using one of these source types and the associated example JSON configuration from this library. Coveo’s recommendation depends on the extent of testing of the system example configuration in proofs of concept.

Coveo recommends the REST API GitHub example JSON configuration herein.

However, please be aware that all library configurations, including those recommended on the Coveo Platform, are not actively maintained or officially supported. Consider them as starting points that you’ll need to customize to your specific use case. 

## Prerequisites

To fully understand how to use this example, you must:

1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions - GitHub without security

1. Follow the [Web Application Flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) steps to get an OAuth 2.0 token.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your token.
3. Use the example in [`SourceJSONConfig.json`](./SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Indexing GitHub with security and members in SSO

**Use case**

You want to index the collaborators of each Repository and use them for security trimming.
During indexing we assign the `RepoMembersGroup` using the `name` of the repository as an `Allowed permission`.

During the Security Cache expansion we follow the following steps to resolve the groups to a valid email address:

- We first request for each `RepoMembersGroup` the `/collaborators`. This will give us all the usernames from GitHub. We put them into `GithubUserGroupMember` using the `login` information from the `/collaborators` call.
- Next step is to map the `GithubUserGroupMember` to an actual email address. We are using a `GraphQL` query against GitHub for that. This will translate a `login` like `wim` into `wim@coveo.com`.

**Example of the flow**

1. Index Repository: `coveo-labs/searchkit-proxy`
2. For each item in this repository, assign `PermissionsSets>AllowedMembers`

   - Type: `Group`
   - PermissionType: `RepoMembersGroup`
   - AdditionalInfo (this is being used in the Security Cache): `groupid: searchkit-proxy`

3. During Security Cache refresh/update, all needed `AdditionalInfo->groupid` are expanded. For each `groupid`, ask GitHub for collaborators using: `coveo-labs/[groupid]/collaborators` (in our example, `coveo-labs/searchkit-proxy/collaborators`).

   Two example results:

   - Type: `User`
   - PermissionType: `GithubUserGroupMember`
   - AdditionalInfo: `login: wim`

   - Type: `User`
   - PermissionType: `GithubUserGroupMember`
   - AdditionalInfo: `login: jerome`

4. The next step in the Security Cache expansion is to retrieve mappings for each `login`. Using the `/graphql` GitHub call, we execute a request for each `login`.

   Example results:

   - For login: "wim"
     Result: "wim@coveo.com" (`%[node.samlIdentity.nameId]`)

   - For login: "jerome"
     Result: "jerome@coveo.com" (`%[node.samlIdentity.nameId]`)

9. Now the Security Cache knows exactly how a `Group`, expands to a `Collaborator user`, and how it maps to a `Email Security Provider`

**Instructions**

1. Follow the [Web Application Flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) steps to get an OAuth 2.0 token.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your token.
3. Set the Content Security to: `Determined by source permissions`.
4. Use the example in [`SecuredSourceJSON_Config.json`](./SecuredSourceJSON_Config.json) as a base to build your source JSON configuration. Adjust it to your own needs.
5. Under the `Content Security` tab, select **Same users and groups as in your current permission system** and use the example in [`SecuredSourceJSON_ContentSecurity.json`](./SecuredSourceJSON_ContentSecurity.json) as a base to build your source [**JSON permissions configuration**](https://docs.coveo.com/en/3303/). Adjust it to your own needs. Use a proper account for the SSO GraphQL call.
6. Make sure you've changed all placeholders in the configuration with your own values.
7. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
8. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

* [GitHub REST API documentation](https://docs.github.com/en/rest)
* [GitHub REST](https://docs.github.com/en/rest)
* [GitHub GraphQL](https://docs.github.com/en/graphql)
