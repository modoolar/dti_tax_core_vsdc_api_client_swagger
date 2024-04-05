# dti_tax_core_vsdc_api_client_swagger.StatusApi

All URIs are relative to *https://vsdc.sandbox.suf.purs.gov.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_attention**](StatusApi.md#status_attention) | **GET** /api/v3/attention | 
[**status_get_status**](StatusApi.md#status_get_status) | **GET** /api/v3/status | This method returns general infromation about Tax Authority and current tax rate group used to  calculate taxes by this instance of V-SDC
[**status_get_tax_authority_params**](StatusApi.md#status_get_tax_authority_params) | **GET** /api/v3/environment-parameters | This method returns general infromation about Tax Authority


# **status_attention**
> object status_attention()



### Example
```python
from __future__ import print_function
import time
import dti_tax_core_vsdc_api_client_swagger
from dti_tax_core_vsdc_api_client_swagger.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dti_tax_core_vsdc_api_client_swagger.StatusApi()

try:
    api_response = api_instance.status_attention()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_attention: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get_status**
> GetStatusResponse status_get_status()

This method returns general infromation about Tax Authority and current tax rate group used to  calculate taxes by this instance of V-SDC

### Example
```python
from __future__ import print_function
import time
import dti_tax_core_vsdc_api_client_swagger
from dti_tax_core_vsdc_api_client_swagger.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dti_tax_core_vsdc_api_client_swagger.StatusApi()

try:
    # This method returns general infromation about Tax Authority and current tax rate group used to  calculate taxes by this instance of V-SDC
    api_response = api_instance.status_get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStatusResponse**](GetStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get_tax_authority_params**
> TaxCorePublicConfiguration status_get_tax_authority_params()

This method returns general infromation about Tax Authority

### Example
```python
from __future__ import print_function
import time
import dti_tax_core_vsdc_api_client_swagger
from dti_tax_core_vsdc_api_client_swagger.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dti_tax_core_vsdc_api_client_swagger.StatusApi()

try:
    # This method returns general infromation about Tax Authority
    api_response = api_instance.status_get_tax_authority_params()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get_tax_authority_params: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxCorePublicConfiguration**](TaxCorePublicConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

