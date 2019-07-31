# UpsertQuotesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**values** | [**dict(str, Quote)**](Quote.md) | The collection of upserted quotes with their latest values | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | If any quotes failed to be upserted, they will be listed in &#39;Failed&#39;, along  with a reason why. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


