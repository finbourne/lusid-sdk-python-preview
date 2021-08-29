# BucketedCashFlowResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**data** | **list[dict(str, object)]** | List of dictionary bucketed cash flow result set.  Each dictionary represent a bucketed cashflow result set keyed by AddressKeys.  e.g. dictionary[\&quot;Valuation/CashFlowAmount\&quot;] for the aggregated cash flow amount for the bucket.  e.g. suppose \&quot;RoundUp\&quot; method, then dictionary[\&quot;Valuation/CashFlowDate/RoundUp\&quot;] returns the bucketed cashflow date. | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant. | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


