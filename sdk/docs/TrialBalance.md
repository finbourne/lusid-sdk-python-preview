# TrialBalance

A TrialBalance entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_account_code** | **str** | The Account code that the trial balance results have been grouped against | 
**description** | **str** | The description of the record | [optional] 
**levels** | **list[str]** | The levels that have been derived from the specified General Ledger Profile | 
**account_type** | **str** | The account type attributed to the record | 
**local_currency** | **str** | The account type attributed to the record | 
**opening** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**closing** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**debit** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**credit** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Properties found on the mapped &#39;Account&#39;, as specified in request | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


