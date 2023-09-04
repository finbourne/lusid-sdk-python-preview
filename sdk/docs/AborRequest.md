# AborRequest

The request used to create an Abor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Abor. | 
**display_name** | **str** | The given name for the Abor. | 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**list[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. For now the only supported value is SinglePortfolio. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Properties to add to the Abor. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


