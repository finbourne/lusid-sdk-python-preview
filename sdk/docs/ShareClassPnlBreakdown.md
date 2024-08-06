# ShareClassPnlBreakdown

The breakdown of PnL for a Share Class on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apportioned_non_class_specific_pnl** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class. | 
**class_pnl** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Bucket of detail for PnL specific to the share class within the queried period. | 
**total_pnl** | [**dict(str, ShareClassAmount)**](ShareClassAmount.md) | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


