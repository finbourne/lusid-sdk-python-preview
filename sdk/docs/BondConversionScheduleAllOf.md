# BondConversionScheduleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **dict(str, str)** | The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied. | [optional] 
**bond_conversion_entries** | [**list[BondConversionEntry]**](BondConversionEntry.md) | The dates at which the bond may be converted and associated information required about the conversion. | [optional] 
**conversion_trigger** | **str** | Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall]. | 
**delivery_type** | **str** | Is a conversion made into cash or into shares?    Supported string (enumeration) values are: [Cash, Physical]. | [optional] 
**exercise_type** | **str** | The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**includes_accrued** | **bool** | Set this to true if a accrued interest is included in the conversion. Defaults to true. | [optional] 
**mandatory_conversion** | **bool** | Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false. | [optional] 
**notification_period_end** | **datetime** | The last day in the notification period for the conversion of the bond | [optional] 
**notification_period_start** | **datetime** | The first day in the notification period for the conversion of the bond | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


