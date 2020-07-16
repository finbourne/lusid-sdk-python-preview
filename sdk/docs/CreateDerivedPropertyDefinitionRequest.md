# CreateDerivedPropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**derivation** | **str** | The string that contains the rule for the derived property. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


