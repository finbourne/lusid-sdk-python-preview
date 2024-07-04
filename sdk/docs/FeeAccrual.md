# FeeAccrual


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective date for which the fee accrual has been calculated. | 
**code** | **str** | The code of the fee for which the accrual has been calculated. | 
**name** | **str** | The name of the fee for which the accrual has been calculated. | 
**calculation_base** | **float** | The result of the evaluating the fee&#39;s calculation base expression. | [optional] 
**amount** | **float** | The result of applying the fee to the calculation base, and scaled down to a day. | [optional] 
**previous_accrual** | **float** | The previous valuation point&#39;s total accrual. | [optional] 
**total_accrual** | **float** | The sum of the PreviousAccrual and Amount. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


