# FxRateScheduleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**fx_conversion_types** | **list[str]** | List of flags to indicate if coupon payments, principal payments or both are converted | [optional] 
**rate** | **float** | FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate | [optional] 
**to_currency** | **str** | Currency that payments are converted to | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, Invalid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


