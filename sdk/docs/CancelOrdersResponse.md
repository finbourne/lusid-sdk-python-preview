# CancelOrdersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, CancelledOrderResult)**](CancelledOrderResult.md) | The orders which have been successfully cancelled. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The orders that could not be cancelled, along with a reason for their failure. | [optional] 
**metadata** | **dict(str, list[ResponseMetaData])** | Meta data associated with the cancellation event. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


