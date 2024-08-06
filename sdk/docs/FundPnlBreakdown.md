# FundPnlBreakdown

The breakdown of PnL for a Fund on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_class_specific_pnl** | [**dict(str, FundAmount)**](FundAmount.md) | Bucket of detail for PnL within the queried period that is not specific to any share class. | 
**aggregated_class_pnl** | [**dict(str, FundAmount)**](FundAmount.md) | Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period. | 
**total_pnl** | [**dict(str, FundAmount)**](FundAmount.md) | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


