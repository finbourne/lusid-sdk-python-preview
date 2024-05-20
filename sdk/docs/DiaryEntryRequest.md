# DiaryEntryRequest

The request to add a diary entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the diary entry. | [optional] 
**status** | **str** | The status of the diary entry. Defaults to &#39;Undefined&#39; and the allowed options are: &#39;Undefined&#39; and &#39;Estimate&#39;. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


