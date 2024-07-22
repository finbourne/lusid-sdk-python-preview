# ShareClassBreakdown

The Valuation Point Data for a Share Class on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_out** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. | 
**dealing** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Bucket of detail for any &#39;Dealing&#39; that has occured inside the queried period. | 
**pn_l** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Bucket of detail for &#39;PnL&#39; that has occured inside the queried period. | 
**gav** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**fees** | [**dict(str, FeeAccrual)**](FeeAccrual.md) | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. | 
**nav** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 
**miscellaneous** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). | [optional] 
**share_class_to_fund_fx_rate** | **float** | The fx rate from the Share Class currency to the fund currency at this valuation point. | 
**capital_ratio** | **float** | The proportion of the fund&#39;s adjusted beginning equity (ie: the sum of the previous NAV and the net dealing) that is invested in the share class. | 
**previous_share_class_breakdown** | [**PreviousShareClassBreakdown**](PreviousShareClassBreakdown.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


