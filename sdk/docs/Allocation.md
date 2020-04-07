# Allocation

An Allocation of a certain quantity of a specific instrument against an originating  Order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **int** | The quantity of given instrument allocated. | 
**instrument_identifiers** | **dict(str, str)** | The instrument allocated. | 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this allocation. | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument allocated. | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


