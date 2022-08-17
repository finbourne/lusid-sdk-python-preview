# TradeTicket

A Trade Ticket comprising of an instrument, a transaction and a counterparty.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction. | 
**type** | **str** | The type of the transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction. | 
**source** | **str** | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. | [optional] 
**transaction_date** | **str** | The date of the transaction. | 
**settlement_date** | **str** | The settlement date of the transaction. | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**units** | **float** | The number of units of the transacted instrument. | 
**instrument_identifiers** | **dict(str, str)** | The set of identifiers that can be used to identify the instrument. | 
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**instrument_name** | **str** | The name of the instrument. | [optional] 
**instrument_definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**counterparty_agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


