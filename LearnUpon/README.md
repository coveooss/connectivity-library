# Indexing LearnUpon Using the Generic REST API Connector

## Use Case
This example shows how to retrieve courses from the LearnUpon platform. It is also possible to retrieve modules but this is not covered in this version.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Instructions
1. [Get a LearnUpon account](https://docs.learnupon.com/api/#get-started).
2. [Create a Generic REST API](https://docs.coveo.com/en/1896/) source and, in the **Authorization** section, provide the credentials obtained in step 1.
3. Use the example in [`SourceJSONConfig.json`](https://github.com/coveooss/connectivity-library/blob/master/LearnUpon/SourceJSONConfig.json) as a base to build your source JSON configuration. Adjust it to your own needs.
4. Make sure you've changed all placeholders in the configuration with your own values.
5. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).
6. Check whether your source indexes the desired content properly. You might find you need an additional [indexing pipeline extension](https://docs.coveo.com/en/1645/) to achieve the expected result.

## Reference
[LearnUpon API documentation](https://docs.learnupon.com/api/#learnupon-technical-documentation)
