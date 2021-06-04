# CreateRecipeRequest

Specification class to request for the creation/supplementing of a configuration recipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_creation_market_data_scopes** | **list[str]** | The scopes in which the recipe creation would look for quotes/data. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**inline_recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**as_at** | **datetime** | The asAt date to use | [optional] 
**effective_at** | **str** | The market data time, i.e. the recipe generated will look for rules with this effectiveAt. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


