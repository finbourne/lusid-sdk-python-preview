# Abor

An Abor entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The given name for the Abor. | [optional] 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**list[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. For now the only supported value is SinglePortfolio. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Properties to add to the Abor. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


