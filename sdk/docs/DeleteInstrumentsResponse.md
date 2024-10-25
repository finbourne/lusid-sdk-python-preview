# DeleteInstrumentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**as_at** | **datetime** | The as-at datetime at which the instrument was deleted. | 
**staged** | [**dict(str, StagedModificationsInfo)**](StagedModificationsInfo.md) | Information about the pending staged modifications for the current entity. | [optional] [readonly] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


