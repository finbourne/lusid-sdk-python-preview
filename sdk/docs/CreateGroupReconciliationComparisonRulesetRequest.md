# CreateGroupReconciliationComparisonRulesetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the ruleset | 
**reconciliation_type** | **str** | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; | 
**core_attribute_rules** | [**list[GroupReconciliationCoreAttributeRule]**](GroupReconciliationCoreAttributeRule.md) | The core comparison rules | 
**aggregate_attribute_rules** | [**list[GroupReconciliationAggregateAttributeRule]**](GroupReconciliationAggregateAttributeRule.md) | The aggregate comparison rules | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


