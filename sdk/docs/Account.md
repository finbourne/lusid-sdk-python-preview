# Account

An account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the account. | 
**description** | **str** | The description for the account. | [optional] 
**type** | **str** | The account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue. | 
**status** | **str** | The account status. Can be Active, Inactive or Deleted. Defaults to Active. The available values are: Active, Inactive, Deleted | 
**control** | **str** | This allows users to specify whether this a protected account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”. | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Account properties to add to the account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


