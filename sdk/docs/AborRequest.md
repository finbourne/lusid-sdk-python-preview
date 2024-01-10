# AborRequest

The request used to create an Abor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Abor. | 
**display_name** | **str** | The name of the Abor. | 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**list[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties for the Abor. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


