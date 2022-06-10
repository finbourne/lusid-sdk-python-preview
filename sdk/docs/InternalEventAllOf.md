# InternalEventAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | What category of event does this represent; instrument opening, closing, transition or other. | [optional] [readonly] 
**event_category** | **str** | What category of event does this represent; instrument opening, closing, transition or other. | [optional] 
**event_source** | **str** | What is the event source, what causes it to happen. | [optional] 
**anchor_date** | **datetime** | In the case of a point event, the single date on which the event occurs. In the case of an event which is  spread over a window, e.g. a barrier or American option, the start of that window. | [optional] 
**event_window_end** | **datetime** | In the case of a point event this is identical to the anchor date. In the case of an event that is spread over a window,  this is the end of that window. | [optional] [readonly] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InternalEvent, CouponEvent, OpenEvent, CloseEvent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


