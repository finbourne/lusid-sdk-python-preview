# GetQuotesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**values** | [**dict(str, Quote)**](Quote.md) | The collection of requested quote series with their latest values | [optional] 
**not_found** | **dict(str, list[str])** | If any quotes could not be retrieved, they will be listed in &#39;NotFound&#39;, along  with a reason why. | [optional] 
**failed** | **dict(str, list[str])** | If any quotes could not be requested, due to errors in the structure of the   QuoteSeriesId, they will be listed in &#39;Failed&#39;, along with the reason(s) why. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


