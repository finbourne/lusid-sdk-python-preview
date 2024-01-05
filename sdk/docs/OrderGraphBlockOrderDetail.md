# OrderGraphBlockOrderDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**compliance_state** | **str** | The compliance state of this order. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39; and &#39;Passed&#39;. | 
**approval_state** | **str** | The approval state of this order. Possible values are &#39;Pending&#39;, &#39;Rejected&#39; and &#39;Approved&#39;. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_name** | **str** | The name of the order&#39;s referenced Portfolio. | [optional] 
**order_approval_task_id** | **str** | The task id associated with the approval state of the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


