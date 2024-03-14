# LusidTradeTicket

A LUSID Trade Ticket comprising an instrument, a transaction, and a counterparty.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID. Must be unique. | 
**transaction_type** | **str** | Type of transaction for processing. Referenced by Transaction Configuration. | 
**source** | **str** | Transaction Source. Referenced by Transaction Configuration. | [optional] 
**transaction_date** | **str** | Transaction Date. Date at which transaction is known. | 
**settlement_date** | **str** | Transaction settlement. Date at which transaction is finalised and realised into the system. | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**units** | **float** | Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised. | 
**instrument_identifiers** | **dict(str, str)** | Identifiers for the instrument. | 
**instrument_scope** | **str** | Scope of instrument | [optional] 
**instrument_name** | **str** | Name of instrument | [optional] 
**instrument_definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**counterparty_agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**counterparty** | **str** | Counterparty | [optional] 
**instrument_properties** | [**list[ModelProperty]**](ModelProperty.md) | Set of instrument properties (as defined by client/user). | [optional] 
**transaction_properties** | [**list[ModelProperty]**](ModelProperty.md) | Set of transaction properties (as defined by client/user). | [optional] 
**trade_ticket_type** | **str** | The available values are: LusidTradeTicket, ExternalTradeTicket | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


