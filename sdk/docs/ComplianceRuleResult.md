# ComplianceRuleResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The unique identifierof a compliance rule | 
**rule_name** | **str** | The User-given name of the rule | 
**rule_description** | **str** | The User-given description of the rule | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**passed** | **bool** | The result of an individual compliance run, true if passed | 
**result_value** | **float** | The calculation result that was used to confirm a pass/fail | 
**rule_information_match** | **str** | The value matched by the rule | 
**rule_information_key** | **str** | The property key matched by the rule | 
**rule_lower_limit** | **int** | The lower limit of the rule | 
**rule_upper_limit** | **int** | The upper limit of the rule | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


