# DataDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The internal address (LUSID native) of the unit in the provided data itself and corresponds to the external name of the data item | [optional] 
**name** | **str** | The name of the data item. This is the name that will appear | [optional] 
**data_type** | **str** | A member of the set of possible data types, that all data passed under that key is expected to be of.  Currently limited to one of [string, integer, decimal]. | [optional] 
**key_type** | **str** | Is the item either a unique key for the dictionary, i.e. does it identify a unique index or conceptual &#39;row&#39; within the list of dictionaries,  or a partial key or is it simply a data item within that dictionary. Must be one of [Unique,PartOfUnique,Leaf] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


