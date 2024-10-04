# UpdateOrdersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, Order)**](Order.md) | The orders which have been successfully updated. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The orders that could not be updated, along with a reason for their failure. | [optional] 
**metadata** | **dict(str, list[ResponseMetaData])** | Meta data associated with the update event. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


