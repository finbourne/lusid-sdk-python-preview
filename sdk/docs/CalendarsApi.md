# lusid.CalendarsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:60782*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_date_to_calendar**](CalendarsApi.md#add_date_to_calendar) | **PUT** /api/calendars/generic/{scope}/{code}/dates | [BETA] Add a date to a calendar
[**create_calendar**](CalendarsApi.md#create_calendar) | **POST** /api/calendars/generic | [BETA] Create a calendar in its generic form
[**delete_calendar**](CalendarsApi.md#delete_calendar) | **DELETE** /api/calendars/generic/{scope}/{code} | [BETA] Delete a calendar
[**delete_date_from_calendar**](CalendarsApi.md#delete_date_from_calendar) | **DELETE** /api/calendars/generic/{scope}/{code}/dates/{dateId} | [BETA] Remove a date from a calendar
[**get_calendar**](CalendarsApi.md#get_calendar) | **GET** /api/calendars/generic/{scope}/{code} | [BETA] Get a calendar in its generic form
[**get_dates**](CalendarsApi.md#get_dates) | **GET** /api/calendars/generic/{scope}/{code}/dates | [BETA] Get dates for a specific calendar
[**is_business_date_time**](CalendarsApi.md#is_business_date_time) | **GET** /api/calendars/businessday/{scope}/{code} | [BETA] Check whether a DateTime is a \&quot;Business DateTime\&quot;
[**list_calendars**](CalendarsApi.md#list_calendars) | **GET** /api/calendars/generic | [BETA] List Calenders
[**list_calendars_in_scope**](CalendarsApi.md#list_calendars_in_scope) | **GET** /api/calendars/generic/{scope} | [BETA] List all calenders in a specified scope
[**update_calendar**](CalendarsApi.md#update_calendar) | **POST** /api/calendars/generic/{scope}/{code} | [BETA] Update a calendar


# **add_date_to_calendar**
> CalendarDate add_date_to_calendar(scope, code, create_date_request)

[BETA] Add a date to a calendar

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
create_date_request = {"dateId":"TestDate","fromUtc":"2020-02-12T12:00:00.0000000+00:00","toUtc":"2020-02-13T12:00:00.0000000+00:00","timeZone":"CET","description":"Chinese New year","type":"Holiday","sourceData":{}} # CreateDateRequest | Add date to calendar request

try:
    # [BETA] Add a date to a calendar
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

[BETA] Create a calendar in its generic form

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
create_calendar_request = {"calendarId":{"scope":"TestScope","code":"TestCode"},"calendarType":"Holiday","weekendMask":{"days":["Saturday","Sunday"],"timeZone":"UTC"},"sourceProvider":"Finbourne Calendar Service","properties":[{"key":"Calendar/default/Center","value":{"labelValue":"CBTR"}}]} # CreateCalendarRequest | A request to create the calendar

try:
    # [BETA] Create a calendar in its generic form
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

[BETA] Delete a calendar

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar

try:
    # [BETA] Delete a calendar
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

[BETA] Remove a date from a calendar

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
date_id = 'date_id_example' # str | Identifier of the date to be removed

try:
    # [BETA] Remove a date from a calendar
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

[BETA] Get a calendar in its generic form

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar identifier
code = 'code_example' # str | Code of the calendar identifier
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendar (optional)

try:
    # [BETA] Get a calendar in its generic form
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

[BETA] Get dates for a specific calendar

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
from_effective_at = 'from_effective_at_example' # str | Where the effective window of dates should begin from (optional)
to_effective_at = 'to_effective_at_example' # str | Where the effective window of dates should end (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt the dates should be retrieved at (optional)
id_filter = ['id_filter_example'] # list[str] | An additional filter that will filter dates based on their identifer (optional)

try:
    # [BETA] Get dates for a specific calendar
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

# **is_business_date_time**
> IsBusinessDayResponse is_business_date_time(date_time, scope, code, as_at=as_at)

[BETA] Check whether a DateTime is a \"Business DateTime\"

A Business DateTime is defined as a point in time that:      * Does not represent a day that overlaps with the calendars WeekendMask      * If the calendar is a \"Holiday Calendar\" Does not overlap with any dates in the calendar      * If the calendar is a \"TradingHours Calendar\" Does overlap with a date in the calendar                All dates specified must be UTC and the upper bound of a calendar is not inclusive   e.g. From: 2020-12-25-00-00-00        To: 2020-12-26-00-00-00  IsBusinessDay(2020-12-26-00-00-00) == false

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
date_time = '2013-10-20T19:20:30+01:00' # datetime | DateTime to check - This DateTime must be UTC
scope = 'scope_example' # str | Scope of the calendar
code = 'code_example' # str | Code of the calendar
as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt for the request (optional)

try:
    # [BETA] Check whether a DateTime is a \"Business DateTime\"
    api_response = api_instance.is_business_date_time(date_time, scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->is_business_date_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_time** | **datetime**| DateTime to check - This DateTime must be UTC | 
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **as_at** | **datetime**| AsAt for the request | [optional] 

### Return type

[**IsBusinessDayResponse**](IsBusinessDayResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether or not the requested DateTime is a BusinessDay or not |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calendars**
> PagedResourceListOfCalendar list_calendars(as_at=as_at, page=page, limit=limit, filter=filter)

[BETA] List Calenders

List calendars at a point in AsAt time.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendars (optional)
page = 'page_example' # str | The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [BETA] List Calenders
    api_response = api_instance.list_calendars(as_at=as_at, page=page, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->list_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the calendars | [optional] 
 **page** | **str**| The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfCalendar**](PagedResourceListOfCalendar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Calendars |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calendars_in_scope**
> PagedResourceListOfCalendar list_calendars_in_scope(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[BETA] List all calenders in a specified scope

List calendars at a point in AsAt time.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the calendars
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendars (optional)
page = 'page_example' # str | The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [BETA] List all calenders in a specified scope
    api_response = api_instance.list_calendars_in_scope(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalendarsApi->list_calendars_in_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendars | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the calendars | [optional] 
 **page** | **str**| The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfCalendar**](PagedResourceListOfCalendar.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calendars in the requested scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_calendar**
> Calendar update_calendar(scope, code, update_calendar_request)

[BETA] Update a calendar

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60782
configuration.host = "http://local-unit-test-server.lusid.com:60782"
# Create an instance of the API class
api_instance = lusid.CalendarsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the request
code = 'code_example' # str | Code of the request
update_calendar_request = {"weekendMask":{"days":["Saturday","Sunday"],"timeZone":"UTC"},"sourceProvider":"Finbourne Calendar Service","properties":[{"key":"Calendar/default/Center","value":{"labelValue":"CBTR"}}]} # UpdateCalendarRequest | The new state of the calendar

try:
    # [BETA] Update a calendar
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

