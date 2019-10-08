# CreateDerivedTransactionPortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Portfolio display name | 
**description** | **str** | A long form text description of  the portfolio | [optional] 
**code** | **str** |  | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**created** | **datetime** | The original creation date, defaults to today if not specified when creating a portfolio | [optional] 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | Default taxlot selection method for the portfolio | [optional] 
**sub_holding_keys** | **list[str]** | Set of unique holding identifiers, e.g. trader, desk, strategy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


