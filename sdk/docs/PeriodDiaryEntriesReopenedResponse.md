# PeriodDiaryEntriesReopenedResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**effective_from** | **datetime** | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the deletion was committed to LUSID. | 
**period_diary_entries_removed** | **int** | Number of Diary Entries removed as a result of reopening periods | 
**period_diary_entries_from** | **datetime** | The start point where periods were removed from | 
**period_diary_entries_to** | **datetime** | The end point where periods were removed to | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


