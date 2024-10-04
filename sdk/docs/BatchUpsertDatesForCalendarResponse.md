# BatchUpsertDatesForCalendarResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**dict(str, CalendarDate)**](CalendarDate.md) | The dates which have been successfully upserted. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The dates that could not be upserted along with a reason for their failure. | [optional] 
**metadata** | **dict(str, list[ResponseMetaData])** | Contains warnings related to the upserted dates | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


