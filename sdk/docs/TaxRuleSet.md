# TaxRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly name | 
**description** | **str** | A description of what this rule set is for | 
**output_property_key** | **str** | The property key that this rule set will write to | 
**rules** | [**list[TaxRule]**](TaxRule.md) | The rules of this rule set, which stipulate what rate to apply (i.e. write to the OutputPropertyKey) under certain conditions | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


