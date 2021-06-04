# IndexConvention

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixing_reference** | **str** | The reference rate name for fixings | 
**publication_day_lag** | **int** | Number of days between spot and publication of the rate. | 
**payment_tenor** | **str** | The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year. | 
**day_count_convention** | **str** | when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year              and difference between them. | 
**currency** | **str** | Currency of the index convention. | 
**scope** | **str** | The scope used when updating or inserting the convention. | [optional] 
**code** | **str** | The code of the convention. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


