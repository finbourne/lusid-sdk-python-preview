# OutputTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | [optional] 
**instrument_identifiers** | **dict(str, str)** |  | [optional] 
**instrument_uid** | **str** |  | 
**transaction_date** | **datetime** |  | 
**settlement_date** | **datetime** |  | 
**units** | **float** |  | 
**transaction_amount** | **float** |  | [optional] 
**transaction_price** | [**TransactionPrice**](TransactionPrice.md) |  | [optional] 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**transaction_to_portfolio_rate** | **float** |  | [optional] 
**transaction_currency** | **str** |  | [optional] 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) |  | [optional] 
**counterparty_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**transaction_status** | **str** |  | [optional] 
**entry_date_time** | **datetime** |  | [optional] 
**cancel_date_time** | **datetime** |  | [optional] 
**realised_gain_loss** | [**list[RealisedGainLoss]**](RealisedGainLoss.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


