# LusidTradeTicket

A LUSID Trade Ticket comprising an instrument, a transaction, and a counterparty.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**transaction_type** | **str** |  | 
**source** | **str** |  | [optional] 
**transaction_date** | **str** |  | 
**settlement_date** | **str** |  | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**units** | **float** |  | 
**instrument_identifiers** | **dict(str, str)** |  | 
**instrument_scope** | **str** |  | [optional] 
**instrument_name** | **str** |  | [optional] 
**instrument_definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**counterparty_agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_properties** | [**list[ModelProperty]**](ModelProperty.md) |  | [optional] 
**transaction_properties** | [**list[ModelProperty]**](ModelProperty.md) |  | [optional] 
**trade_ticket_type** | **str** | The available values are: LusidTradeTicket, ExternalTradeTicket | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


