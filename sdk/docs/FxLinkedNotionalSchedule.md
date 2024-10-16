# FxLinkedNotionalSchedule

Schedule for notional changes based on the change in FX rate.  Used in the representation of a resettable cross currency interest rate swap.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fx_conventions** | [**FxConventions**](FxConventions.md) |  | 
**varying_notional_currency** | **str** | The currency of the varying notional amount. | 
**varying_notional_fixing_dates** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | 
**varying_notional_interim_exchange_payment_dates** | [**RelativeDateOffset**](RelativeDateOffset.md) |  | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


