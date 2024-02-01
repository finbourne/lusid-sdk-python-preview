# Account

An account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Account. | 
**description** | **str** | A description for the Account. | [optional] 
**type** | **str** | The Account type. Can have the values: Asset/Liabilities/Income/Expense/Capital/Revenue. | 
**status** | **str** | The Account status. Can be Active, Inactive or Deleted. Defaults to Active. The available values are: Active, Inactive, Deleted | 
**control** | **str** | This allows users to specify whether this a protected Account that prevents direct manual journal adjustment. Can have the values: System/ManualIt will default to “Manual”. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties for the Account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


