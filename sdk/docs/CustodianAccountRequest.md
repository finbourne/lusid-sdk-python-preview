# CustodianAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used | [optional] 
**code** | **str** | Unique Code representing the Custodian Account | 
**status** | **str** | The account status. Can be Active, Inactive or Deleted. Defaults to Active. | [optional] 
**account_number** | **str** | The Custodian Account Number | 
**account_name** | **str** | The identifiable name given to the Custodian Account | 
**accounting_method** | **str** | The Accounting method to be used | 
**currency** | **str** | The Currency for the Account | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain. | [optional] 
**custodian_identifier** | [**TypedResourceId**](TypedResourceId.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


