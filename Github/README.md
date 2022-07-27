# Indexing Github Using the Generic REST API Connector

## Use Case

This example shows how to index GitHub repositories and other content types.

## Prerequisites

To fully understand how to use this example, you must:

1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions, Github without Security

1. Follow the [Web Application Flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) steps to get an OAuth 2.0 token.
2. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your token.
3. Use the example in [`SourceJSONConfig.json`](./SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Instructions, Github with Security and members in SSO

Use case: you want to index the collaborators of each Repository and use them for security trimming.
During indexing we assign the `RepoMembersGroup` using the `name` of the repository as a `Allowed permission`.

During the Security Cache expansion we follow the following steps to resolve the groups to a valid email address:

- We first request for each `RepoMembersGroup` the `/collaborators`. This will give us all the usernames from Github. We put them into `GithubUserGroupMember` using the `login` information from the `/collaborators` call.
- Next step is to map the `GithubUserGroupMember` to an actual email address. We are using a `GraphQL` query against Github for that. This will translate a `login` like `wim` into `wim@coveo.com`.

Example of the flow:

1. Index Repository: `coveo-labs/searchkit-proxy`
2. For each item in this repository: assign `PermissionSet>AllowedMembers`

- PermissionType: `RepoMembersGroup`
- Type: `Group`
- AdditionalInfo (this is being used in the Security Cache): `groupid: searchkit-proxy`

3. During Security Cache refresh/update
4. All the needed `AdditionalInfo->groupid` are being expanded.
5. For each `groupid`, ask Github for collaborators using: `coveo-labs/[groupid]/collaborators`. In our case: `coveo-labs/searchkit-proxy/collaborators`
6. Results in:

- Type: `User`
- PermissionType: `GithubUserGroupMember`
- AdditionalInfo: `login: wim`
- Type: `User`
- PermissionType: `GithubUserGroupMember`
- AdditionalInfo: `login: jerome`

7. Next step in the Security Cache expansion, retrieve mappings for each `login`
8. Using the `/graphql` Github call we execute for each `login` a request

- login: "wim"
- Results in: "wim@coveo.com" (`%[node.samlIdentity.nameId]`)
- login: "jerome"
- Results in: "jerome@coveo.com" (`%[node.samlIdentity.nameId]`)

9. Now the Security Cache knows exactly how a `Group`, expands to a `Collaborator user`, and how it maps to a `Email Security Provider`

To configure:

1. Follow the [Web Application Flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) steps to get an OAuth 2.0 token.
2. [Create a Generic REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, provide your token.
3. Set the Content Security to: `Determined by source permissions`.
4. Use the example in [`SourceJSONWithSecurityConfig.json`](./SourceJSONWithSecurityConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
5. Use the example in [`SourceJSONSecurityConfig.json`](./SourceJSONSecurityConfig.json) as a base to build your source JSON Security configuration. Adjust it to your own needs. Use an proper account for the SSO GraphQL call. Put the JSON into the `Content Security` tab.
6. Make sure you've changed all placeholders in the configuration with your own values.
7. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
8. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference

[GitHub REST API documentation](https://docs.github.com/en/rest)
[GitHub REST](https://docs.github.com/en/rest)
[GitHub GraphQL](https://docs.github.com/en/graphql)
