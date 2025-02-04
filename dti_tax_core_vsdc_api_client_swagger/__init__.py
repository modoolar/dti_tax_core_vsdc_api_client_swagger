# coding: utf-8

# flake8: noqa

"""
    Dti.TaxCore.VSDC.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from dti_tax_core_vsdc_api_client_swagger.api.invoices_api import InvoicesApi
from dti_tax_core_vsdc_api_client_swagger.api.status_api import StatusApi

# import ApiClient
from dti_tax_core_vsdc_api_client_swagger.api_client import ApiClient
from dti_tax_core_vsdc_api_client_swagger.configuration import Configuration
# import models into sdk package
from dti_tax_core_vsdc_api_client_swagger.models.get_status_response import GetStatusResponse
from dti_tax_core_vsdc_api_client_swagger.models.invoice_request import InvoiceRequest
from dti_tax_core_vsdc_api_client_swagger.models.invoice_result import InvoiceResult
from dti_tax_core_vsdc_api_client_swagger.models.item import Item
from dti_tax_core_vsdc_api_client_swagger.models.payment import Payment
from dti_tax_core_vsdc_api_client_swagger.models.tax_category import TaxCategory
from dti_tax_core_vsdc_api_client_swagger.models.tax_core_public_configuration import TaxCorePublicConfiguration
from dti_tax_core_vsdc_api_client_swagger.models.tax_item import TaxItem
from dti_tax_core_vsdc_api_client_swagger.models.tax_rate import TaxRate
from dti_tax_core_vsdc_api_client_swagger.models.tax_rate_group import TaxRateGroup
