# DataDefinition

When importing data from an external data source, in order for it to be reliable queryable, LUSID needs to know something about it.  A data definition tells LUSID, what a given external data item is, what type it is and whether it in some way identifies items of data.  Consider presenting LUSID with a list of dictionaries where each dictionary contains the same set of keys (names). Each data item pointed to by  a key would be expected to be of the same type (integer, string, decimal etc.). To identify a particular dictionary from the list, a tuple of  one or more of the items in the dictionary would make it unique. If only a single item is required then the

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The internal address (LUSID native) of the unit in the provided data itself and corresponds to the external name of the data item | [optional] 
**name** | **str** | The name of the data item. This is the name that will appear | [optional] 
**data_type** | **str** | A member of the set of possible data types, that all data passed under that key is expected to be of.  Currently limited to one of [string, integer, decimal]. | [optional] 
**key_type** | **str** | Is the item either a unique key for the dictionary, i.e. does it identify a unique index or conceptual &#39;row&#39; within the list of dictionaries,  or a partial key or is it simply a data item within that dictionary. Must be one of [Unique,PartOfUnique,Leaf] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


