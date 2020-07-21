# CreateDataTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**type_value_range** | **str** | The available values are: Open, Closed | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**value_type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, BenchmarkType, Code, Id, Uri, ArrayOfIds, ArrayOfTransactionAliases, ArrayofTransactionMovements, ArrayofUnits, StringArray, CurrencyAndAmount, TradePrice, UnitCreation, Currency, UserId, MetricValue, QuoteId, QuoteSeriesId, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, Transition, StructuredData, StructuredDataId, ConfigurationRecipe, ConfigurationRecipeSnippet, StructuredResultDataId, StructuredResultData, DataMapping, LusidInstrument, WeightedInstrument, Tenor, CdsProtectionDetailSpecification, FlowConventions, CdsFlowConventions, LegDefinition, IndexConvention, OrderId, Order, Quote, WeekendMask, DateAttributes | 
**acceptable_values** | **list[str]** |  | [optional] 
**unit_schema** | **str** | The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**list[CreateUnitDefinition]**](CreateUnitDefinition.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


