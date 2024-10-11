# GroupReconciliationSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_details** | [**GroupReconciliationRunDetails**](GroupReconciliationRunDetails.md) |  | [optional] 
**group_reconciliation_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**instance_id** | [**GroupReconciliationInstanceId**](GroupReconciliationInstanceId.md) |  | 
**dates_reconciled** | [**GroupReconciliationDates**](GroupReconciliationDates.md) |  | 
**reconciliation_run_as_at** | **str** | The date and time the reconciliation was run | 
**count_comparison_results** | **int** | The total number of comparison results with this InstanceId and ReconciliationType | 
**link_comparison_results** | [**Link**](Link.md) |  | [optional] 
**result_types** | [**GroupReconciliationResultTypes**](GroupReconciliationResultTypes.md) |  | [optional] 
**result_statuses** | [**GroupReconciliationResultStatuses**](GroupReconciliationResultStatuses.md) |  | [optional] 
**review_statuses** | [**GroupReconciliationReviewStatuses**](GroupReconciliationReviewStatuses.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


