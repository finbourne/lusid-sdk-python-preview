# GetReferencePortfolioConstituentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** | The first date from which the weights will apply | 
**weight_type** | **str** | Indicates the weight reset methods. Static, floating or periodical | 
**period_type** | **str** | Indicates the period type (daily, weekly) that weights will reset | [optional] 
**period_count** | **int** | How many multiples of the period between resets | [optional] 
**constituents** | [**list[ReferencePortfolioConstituent]**](ReferencePortfolioConstituent.md) | Set of constituents (instrument/weight pairings) | 
**href** | **str** | The Uri that returns the same result as the original request,  but may include resolved as at time(s). | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


