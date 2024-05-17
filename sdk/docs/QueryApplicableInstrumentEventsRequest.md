# QueryApplicableInstrumentEventsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**effective_at** | **datetime** | The Effective date that splits query window into two parts: factual period and forecast period | 
**portfolio_entity_ids** | [**list[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**forecasting_recipe_id** | [**ResourceId**](ResourceId.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


