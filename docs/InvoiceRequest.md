# InvoiceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_and_time_of_issue** | **datetime** |  | [optional] 
**cashier** | **str** |  | [optional] 
**buyer_id** | **str** |  | [optional] 
**buyer_cost_center_id** | **str** |  | [optional] 
**invoice_type** | **int** |  | 
**transaction_type** | **int** |  | 
**payment** | [**list[Payment]**](Payment.md) |  | 
**invoice_number** | **str** |  | [optional] 
**referent_document_number** | **str** |  | [optional] 
**referent_document_dt** | **datetime** |  | [optional] 
**options** | **dict(str, str)** |  | [optional] 
**items** | [**list[Item]**](Item.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


