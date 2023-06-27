# Indexing Skilljar LMS Using the REST API Connector

## Use Case
This example shows how to index Skilljar training content.

## Prerequisites
In order to fully understand and use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a REST API source](https://docs.coveo.com/en/1896/).

## Instructions
The two typical objects that get indexed are:
* Published courses: `https://api.skilljar.com/v1/domains/training.<<YOUR_DOMAIN>>.com/published-courses`
* Course series: `https://api.skilljar.com/v1/domains/training.<<YOUR_DOMAIN>>.com/course-series`

1. Get Skilljar API key using basic authentication.
2. [Create a REST API source](https://docs.coveo.com/en/1896/) and, in the **Authorization** section, enter your API key.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/Skilljar%20LMS/SourceJSONConfig.json) as a base to build your source JSON configuration. This example retrieves the list of published courses with the first endpoint, the course description using a subquery in the first endpoint, and the course series with the second endpoint. Adjust the configuration example to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
* [Getting started with the Skilljar API](http://support.skilljar.com/hc/en-us/articles/203811260-Getting-started-with-the-Skilljar-API)
* [Skilljar API Endpoint Reference](https://api.skilljar.com/docs/#!/domains)
