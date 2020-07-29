# lusid.CalendarsApi

All URIs are relative to *http://localhost:47060*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_date_to_calendar**](CalendarsApi.md#add_date_to_calendar) | **PUT** /api/calendar/generic/{scope}/{code}/dates | [EXPERIMENTAL] Add a date to a calendar
[**create_calendar**](CalendarsApi.md#create_calendar) | **POST** /api/calendar/generic | [EXPERIMENTAL] Create a calendar in its generic form
[**delete_calendar**](CalendarsApi.md#delete_calendar) | **DELETE** /api/calendar/generic/{scope}/{code} | [EXPERIMENTAL] Delete a calendar
[**delete_date_from_calendar**](CalendarsApi.md#delete_date_from_calendar) | **DELETE** /api/calendar/generic/{scope}/{code}/dates/{dateId} | [EXPERIMENTAL] Remove a date from a calendar
[**get_calendar**](CalendarsApi.md#get_calendar) | **GET** /api/calendar/generic/{scope}/{code} | [EXPERIMENTAL] Get a calendar in its generic form
[**get_dates**](CalendarsApi.md#get_dates) | **GET** /api/calendar/generic/{scope}/{code}/dates | [EXPERIMENTAL] Get dates for a specific calendar
[**update_calendar**](CalendarsApi.md#update_calendar) | **PUT** /api/calendar/generic/{scope}/{code}/mask | [EXPERIMENTAL] Update a calendar


# **add_date_to_calendar**
> CalendarDate add_date_to_calendar(scope, code, create_date_request)

[EXPERIMENTAL] Add a date to a calendar

Add an event to the calendar. These Events can be a maximum of 24 hours and must be specified in UTC.  A local date will be calculated by the system and applied to the calendar before processing.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
create_date_request = {"dateId":"TestDate","fromUtc":"2020-02-12T12:00:00+00:00","toUtc":"2020-02-13T12:00:00+00:00","timeZone":"CET","description":"Chinese New year","type":"Holiday","sourceData":{}} # CreateDateRequest | Add date to calendar request

try:
    # [EXPERIMENTAL] Add a date to a calendar
    api_response = api_instance.add_date_to_calendar(scope, code, create_date_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->add_date_to_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **create_date_request** | [**CreateDateRequest**](CreateDateRequest.md)| Add date to calendar request | 

### Return type

[**CalendarDate**](CalendarDate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created date |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_calendar**
> Calendar create_calendar(create_calendar_request)

[EXPERIMENTAL] Create a calendar in its generic form

Create a calendar in a generic form which can be used to store date events.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
create_calendar_request = {"calendarId":{"scope":"TestScope","code":"TestCode"},"calendarType":"Holiday","weekendMask":{"days":["Saturday","Sunday"],"timeZone":"UTC"},"sourceProvider":"Finbourne Calendar Service","properties":[{"key":"Calendar/default/Center","value":{"labelValue":"CBTR"}}]} # CreateCalendarRequest | A request to create the calendar

try:
    # [EXPERIMENTAL] Create a calendar in its generic form
    api_response = api_instance.create_calendar(create_calendar_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->create_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_calendar_request** | [**CreateCalendarRequest**](CreateCalendarRequest.md)| A request to create the calendar | 

### Return type

[**Calendar**](Calendar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_calendar**
> Calendar delete_calendar(scope, code)

[EXPERIMENTAL] Delete a calendar

Delete a calendar and all of its respective dates

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar

try:
    # [EXPERIMENTAL] Delete a calendar
    api_response = api_instance.delete_calendar(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->delete_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 

### Return type

[**Calendar**](Calendar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_date_from_calendar**
> CalendarDate delete_date_from_calendar(scope, code, date_id)

[EXPERIMENTAL] Remove a date from a calendar

Remove a date from a calendar.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
date_id = 'date_id_example' # str | Identifier of the date to be removed

try:
    # [EXPERIMENTAL] Remove a date from a calendar
    api_response = api_instance.delete_date_from_calendar(scope, code, date_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->delete_date_from_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **date_id** | **str**| Identifier of the date to be removed | 

### Return type

[**CalendarDate**](CalendarDate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted date |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar**
> Calendar get_calendar(scope, code, as_at=as_at)

[EXPERIMENTAL] Get a calendar in its generic form

Retrieve a generic calendar by a specific ID at a point in AsAt time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar identifier
code = 'code_example' # str | Code of the calendar identifier
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendar (optional)

try:
    # [EXPERIMENTAL] Get a calendar in its generic form
    api_response = api_instance.get_calendar(scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->get_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar identifier | 
 **code** | **str**| Code of the calendar identifier | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the calendar | [optional] 

### Return type

[**Calendar**](Calendar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dates**
> ResourceListOfCalendarDate get_dates(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, id_filter=id_filter)

[EXPERIMENTAL] Get dates for a specific calendar

Get dates from a specific calendar within a specific window of effective time, at a point in AsAt time.  Providing an id filter can further refine the results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
from_effective_at = 'from_effective_at_example' # str | Where the effective window of dates should begin from (optional)
to_effective_at = 'to_effective_at_example' # str | Where the effective window of dates should end (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt the dates should be retrieved at (optional)
id_filter = ['id_filter_example'] # list[str] | An additional filter that will filter dates based on their identifer (optional)

try:
    # [EXPERIMENTAL] Get dates for a specific calendar
    api_response = api_instance.get_dates(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, id_filter=id_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->get_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **from_effective_at** | **str**| Where the effective window of dates should begin from | [optional] 
 **to_effective_at** | **str**| Where the effective window of dates should end | [optional] 
 **as_at** | **datetime**| AsAt the dates should be retrieved at | [optional] 
 **id_filter** | [**list[str]**](str.md)| An additional filter that will filter dates based on their identifer | [optional] 

### Return type

[**ResourceListOfCalendarDate**](ResourceListOfCalendarDate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested date |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_calendar**
> Calendar update_calendar(scope, code, update_calendar_request)

[EXPERIMENTAL] Update a calendar

Update the calendars WeekendMask, SourceProvider or Properties

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:47060
configuration.host = "http://localhost:47060"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the request
code = 'code_example' # str | Code of the request
update_calendar_request = {"weekendMask":{"days":["Saturday","Sunday"],"timeZone":"UTC"},"sourceProvider":"Finbourne Calendar Service","properties":[{"key":"Calendar/default/Center","value":{"labelValue":"CBTR"}}]} # UpdateCalendarRequest | The new state of the calendar

try:
    # [EXPERIMENTAL] Update a calendar
    api_response = api_instance.update_calendar(scope, code, update_calendar_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->update_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the request | 
 **code** | **str**| Code of the request | 
 **update_calendar_request** | [**UpdateCalendarRequest**](UpdateCalendarRequest.md)| The new state of the calendar | 

### Return type

[**Calendar**](Calendar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

