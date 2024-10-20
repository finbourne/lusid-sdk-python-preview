# BatchUpdateUserReviewForComparisonResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**dict(str, GroupReconciliationComparisonResult)**](GroupReconciliationComparisonResult.md) | The collection of comparison results that have been successfully updated. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The collection of comparison results that could not be updated with the provided user input along with a reason for their failure. | [optional] 
**metadata** | **dict(str, list[ResponseMetaData])** | Contains warnings related to the updated comparison result user input | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


