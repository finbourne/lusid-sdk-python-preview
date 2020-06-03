# DataMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_field_name_mappings** | [**dict(str, DataDefinition)**](DataDefinition.md) | A map from LUSID item keys to data definitions that define the names, types and degree of uniqueness of data provided to LUSID in structured data stores. | [optional] 
**version** | **str** | The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it. | [optional] 
**code** | **str** | A unique name to semantically identify the mapping set. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


