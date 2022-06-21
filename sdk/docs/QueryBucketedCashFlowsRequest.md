# QueryBucketedCashFlowsRequest

Query for bucketed cashflows from one or more portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for bucketed cashflows. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**list[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**effective_at** | **datetime** | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**rounding_method** | **str** | When bucketing, there is not a unique way to allocate the bucket points. RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp]. | 
**bucketing_dates** | **list[datetime]** | A list of dates to perform cashflow bucketing upon. If this is provided, the list of tenors for bucketing should be empty. | [optional] 
**bucketing_tenors** | **list[str]** | A list of tenors to perform cashflow bucketing upon. If this is provided, the list of dates for bucketing should be empty. | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. | 
**group_by** | **list[str]** | The set of address keys to use to group the bucketed cash flows. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


