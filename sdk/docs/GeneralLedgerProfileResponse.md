# GeneralLedgerProfileResponse

A General Ledger Profile Definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**general_ledger_profile_code** | **str** | The unique code for the General Ledger Profile | 
**display_name** | **str** | The name of the General Ledger Profile | 
**description** | **str** | A description for the General Ledger Profile | [optional] 
**general_ledger_profile_mappings** | [**list[GeneralLedgerProfileMapping]**](GeneralLedgerProfileMapping.md) | Rules for mapping Account or property values to aggregation pattern definitions | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


