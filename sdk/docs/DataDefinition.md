# DataDefinition

When importing data from an external data source, in order for it to be reliable queryable, LUSID needs to know something about it.  A data definition tells LUSID, what a given external data item is, what type it is and whether it in some way identifies items of data.  Consider presenting LUSID with a list of dictionaries where each dictionary contains the same set of keys (names). Each data item pointed to by  a key would be expected to be of the same type (integer, string, decimal etc.). To identify a particular dictionary from the list, a tuple of  one or more of the items in the dictionary would make it unique. If only a single item is required then the
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


