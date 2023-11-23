# GroupOfMarketDataKeyRules

Represents a collection of MarketDataKeyRules that should be resolved together when resolving market data.  That is, market data resolution will always attempt to resolve with all rules in the group  before deciding what market data to return.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_key_rule_group_operation** | **str** | The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used. | 
**market_rules** | [**list[MarketDataKeyRule]**](MarketDataKeyRule.md) | The rules that should be grouped together in market data resolution. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


