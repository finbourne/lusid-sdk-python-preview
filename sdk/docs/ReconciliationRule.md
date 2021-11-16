# ReconciliationRule

A rule describing how a comparison between two items in the reconciliation should be performed and what constitutes equality.  This does not influence WHAT constitutes a match, but only whether once a line has been matched whether an item within it matches another item.  If a rule is not given for an item, it will default to equality comparison.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


