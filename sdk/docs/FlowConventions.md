# FlowConventions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the flow convention. | 
**payment_frequency** | [**Tenor**](Tenor.md) |  | 
**day_count_basis** | **str** | When calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year  and difference between them. | 
**roll_convention** | **str** | When generating a set of dates, what convention should be used for adjusting dates that coincide with a non-business day. | 
**holiday_calendars** | **str** | A comma separated string denoting holiday calendars that apply to generation and payment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


