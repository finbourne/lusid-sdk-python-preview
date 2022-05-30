# InstrumentPaymentDiaryRow

An individual row containing details of a single cashflow in the diary.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it. | [optional] 
**currency** | **str** | The payment currency of the cash flow. | [optional] 
**payment_date** | **datetime** | The date at which the given cash flow is due to be paid. | [optional] 
**pay_or_receive** | **str** | Does the cash flow belong to the Pay or Receive leg. | [optional] 
**accrual_start** | **datetime** | The date on which accruals start for this cashflow. | [optional] 
**accrual_end** | **datetime** | The date on which accruals end for this cashflow. | [optional] 
**cash_flow_type** | **str** | The type of cashflow. | [optional] 
**is_cash_flow_determined** | **bool** | Is the cashflow determined as of the effective date time. | [optional] 
**is_cash_flow_historic** | **bool** | Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt. | [optional] 
**discount_factor** | **float** | Weighting factor to discount cashflow to the present value. | [optional] 
**discounted_expected_cash_flow_amount** | **float** | The expected cashflow amount taking into account the discount factor. | [optional] 
**day_count_fraction** | **float** | The day count fraction, if appropriate. | [optional] 
**forward_rate** | **float** | Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg) | [optional] 
**reset_rate** | **float** | The value of the reset, if any. | [optional] 
**spread** | **float** | The spread that exists on the payoff. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


