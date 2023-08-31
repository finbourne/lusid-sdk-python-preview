# DiaryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**diary_entry_code** | **str** | The code of the diary entry. | [optional] 
**type** | **str** | The type of the diary entry. | 
**name** | **str** | The name of the diary entry. | [optional] 
**status** | **str** | The status of the diary entry. Defaults to &#39;Undefined&#39;. | 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**previous_entry_time** | **datetime** | The entry time of the previous diary entry. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Properties to add to the diary entry. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


