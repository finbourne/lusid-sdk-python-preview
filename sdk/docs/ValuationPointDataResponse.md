# ValuationPointDataResponse

The Valuation Point Data Response for the Fund and specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**type** | **str** | The Type of the associated Diary Entry (&#39;PeriodBoundary&#39;,&#39;ValuationPoint&#39;,&#39;Other&#39; or &#39;Adhoc&#39; when a diary entry wasn&#39;t used). | 
**status** | **str** | The status of a Diary Entry of Type &#39;ValuationPoint&#39;. Defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. The status of a Diary Entry becomes &#39;Unofficial&#39; when a diary entry wasn&#39;t used. | 
**backout** | **dict(str, float)** | DEPRECATED. Bucket of detail for the Valuation Point, where data points have been &#39;backed out&#39;. | 
**dealing** | **dict(str, float)** | DEPRECATED. Bucket of detail for any &#39;Dealing&#39; that has occured inside the queried period. | 
**pn_l** | **dict(str, float)** | DEPRECATED. Bucket of detail for &#39;PnL&#39; that has occured inside the queried period. | 
**gav** | **float** | DEPRECATED. The Gross Asset Value of the Fund at the Period end. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;. | 
**fees** | [**dict(str, FeeAccrual)**](FeeAccrual.md) | DEPRECATED. Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. | 
**nav** | **float** | DEPRECATED. The Net Asset Value of the Fund at the Period end. This represents the GAV with any fees applied in the period. | 
**previous_nav** | **float** | DEPRECATED. The Net Asset Value of the Fund at the End of the last Period. | 
**fund_details** | [**FundDetails**](FundDetails.md) |  | 
**fund_valuation_point_data** | [**FundValuationPointData**](FundValuationPointData.md) |  | 
**share_class_data** | [**dict(str, ShareClassData)**](ShareClassData.md) | The data for all share classes in fund. Share classes are identified by their short codes. | 
**valuation_point_code** | **str** | The code of the valuation point. | [optional] 
**previous_valuation_point_code** | **str** | The code of the previous valuation point. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


