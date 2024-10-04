# DataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_value_range** | **str** | The available values are: Open, Closed | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**value_type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **list[str]** |  | [optional] 
**unit_schema** | **str** | The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**list[IUnitDefinitionDto]**](IUnitDefinitionDto.md) |  | [optional] 
**reference_data** | [**ReferenceData**](ReferenceData.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


