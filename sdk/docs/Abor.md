# Abor

An Abor entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Abor. | [optional] 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**list[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties for the Abor. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**base_currency** | **str** | The base currency of the abor based on contained portfolio base currencies. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


