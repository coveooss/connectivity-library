# How to index App Direct content into Coveo platform using the Generic REST API Connector

Indexing is done using the Generic REST API. Permissions can't be indexed. There are two possible calls : 

Main call : Returns the list of available apps : https://apps.<customer>.com/api/marketplace/v1/listing
Products call : Returns more details on each app : https://apps.
Most setups will not require authentication. You can use Postman to visualize the output of each call.

On the Service Object we will define the URL as https://<subdomain>.appdirect.com/api/marketplace/v1 --- Q: THIS is on the config but the comments is a different URL structure. 
For the main call, we will point to /listing, therefore the Path on the Endpoint Object will be /listing to get all elements
For the products call we will point /listing/products/<id>, therefore we will use the SubQuery Object, definint /listing/products/<id> in Path to get the metadata on all products.