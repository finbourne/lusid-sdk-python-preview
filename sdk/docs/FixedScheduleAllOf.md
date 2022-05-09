# FixedScheduleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Date to start generate from | 
**maturity_date** | **datetime** | Date to generate to | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**coupon_rate** | **float** | Coupon rate given as a fraction. | [optional] 
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notional** | **float** | Scaling factor, the quantity outstanding on which the rate will be paid. | [optional] 
**payment_currency** | **str** | Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. | [optional] 
**schedule_type** | **str** | The available values are: Fixed, Float, Optionality, Step, Exercise, Invalid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


