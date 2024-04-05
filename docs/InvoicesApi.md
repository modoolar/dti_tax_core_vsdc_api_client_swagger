# dti_tax_core_vsdc_api_client_swagger.InvoicesApi

All URIs are relative to *https://vsdc.sandbox.suf.purs.gov.rs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_create_invoice**](InvoicesApi.md#invoices_create_invoice) | **POST** /api/v3/invoices | Post invoice request to sign invoice.
[**invoices_get_signed_invoice**](InvoicesApi.md#invoices_get_signed_invoice) | **GET** /api/v3/invoices/{requestId} | 


# **invoices_create_invoice**
> InvoiceResult invoices_create_invoice(invoice_request)

Post invoice request to sign invoice.

### Example
```python
from __future__ import print_function
import time
import dti_tax_core_vsdc_api_client_swagger
from dti_tax_core_vsdc_api_client_swagger.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dti_tax_core_vsdc_api_client_swagger.InvoicesApi()
invoice_request = dti_tax_core_vsdc_api_client_swagger.InvoiceRequest() # InvoiceRequest | Invoice request.

try:
    # Post invoice request to sign invoice.
    api_response = api_instance.invoices_create_invoice(invoice_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_request** | [**InvoiceRequest**](InvoiceRequest.md)| Invoice request. | 

### Return type

[**InvoiceResult**](InvoiceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_signed_invoice**
> InvoiceResult invoices_get_signed_invoice(request_id)



### Example
```python
from __future__ import print_function
import time
import dti_tax_core_vsdc_api_client_swagger
from dti_tax_core_vsdc_api_client_swagger.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dti_tax_core_vsdc_api_client_swagger.InvoicesApi()
request_id = 'request_id_example' # str | 

try:
    api_response = api_instance.invoices_get_signed_invoice(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_signed_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 

### Return type

[**InvoiceResult**](InvoiceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

