# CancelPlacementsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, CancelledPlacementResult)**](CancelledPlacementResult.md) | The placements which have been successfully cancelled. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The placements that could not be cancelled, along with a reason for their failure. | [optional] 
**metadata** | **dict(str, list[ResponseMetaData])** | Meta data associated with the cancellation event. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


