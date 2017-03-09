import MySQLdb
from btconfig import *

SO_MAP = { 
           'work_in_progress_state': 'WorkInProgressWIPState',
           'patient_id': 'PatientID',
           'ordering_doctor_city': 'OrderingDoctorCity',
           'ordering_doctor_state': 'OrderingDoctorState',
           'insurance_pri_payor': 'InsurancePriPayor',
           'marketing_rep_fullname': 'MarketingRepFullName',
           'referral_name': 'ReferralName',
           'referral_city': 'ReferralCity',
           'referral_state': 'ReferralState',

           'so_number': 'SalesOrderNumber',
           'so_date_created': 'SalesOrderDateCreated',
           'so_created_by': 'SalesOrderCreatedby',
           'so_branch_office': 'SalesOrderBranchOffice',
           'so_status': 'SalesOrderStatus',
           'so_manual_hold': 'SalesOrderManualHold',
           'so_location': 'SalesOrderLocation',
           'so_po_number': 'SalesOrderPONumber',
           'so_purchase_order_number': 'SalesOrderPurchaseOrderNumber',
           'so_reference': 'SalesOrderReference',
           'so_user1': 'SalesOrderUser1',
           'so_user2': 'SalesOrderUser2',
           'so_user3': 'SalesOrderUser3',
           'so_user4': 'SalesOrderUser4',
           'so_confirm_date': 'SalesOrderConfirmDate',
           'so_confirmed_by': 'SalesOrderConfirmedBy',
           'so_last_printed': 'SalesOrderLastPrinted',
           'so_note': 'SalesOrderNote',
           'so_classification': 'SalesOrderClassification',
           'so_type': 'SalesOrderType',
           'so_manual_hold_reason': 'SalesOrderManualHoldReason',
           'so_custom_fields_field1': 'SalesOrderCustomFields_Field1',
           'so_custom_fields_field2': 'SalesOrderCustomFields_Field2',
           'so_custom_fields_field3': 'SalesOrderCustomFields_Field3',
           'so_custom_fields_field4': 'SalesOrderCustomFields_Field4',
           'so_custom_fields_field5': 'SalesOrderCustomFields_Field5',
           'so_custom_fields_field6': 'SalesOrderCustomFields_Field6',
           'so_custom_fields_field7': 'SalesOrderCustomFields_Field7',
           'so_custom_fields_field8': 'SalesOrderCustomFields_Field8',
           'so_custom_fields_field9': 'SalesOrderCustomFields_Field9',
           'so_custom_fields_field10': 'SalesOrderCustomFields_Field10',
           'so_custom_fields_field11': 'SalesOrderCustomFields_Field11',
           'so_custom_fields_field12': 'SalesOrderCustomFields_Field12',
           'so_custom_fields_field13': 'SalesOrderCustomFields_Field13',
           'so_custom_fields_field14': 'SalesOrderCustomFields_Field14',
           'so_custom_fields_field15': 'SalesOrderCustomFields_Field15',
           'so_custom_fields_field16': 'SalesOrderCustomFields_Field16',
           'so_custom_fields_field17': 'SalesOrderCustomFields_Field17',
           'so_custom_fields_field18': 'SalesOrderCustomFields_Field18',
           'so_custom_fields_field19': 'SalesOrderCustomFields_Field19',
           'so_hold_cmn_not_logged': 'SalesOrderHoldCMNNotLogged',
           'so_hold_cmn_expired': 'SalesOrderHoldCMNExpired',
           'so_hold_par_not_logged': 'SalesOrderHoldPARNotLogged',
           'so_hold_par_expired': 'SalesOrderHoldPARExpired',
           'so_hold_manual_hold': 'SalesOrderHoldManualHold',
           'so_stop_pending_pickup': 'SalesOrderStopPendingPickup',
           'so_stop_multiple_pricing_options': 'SalesOrderStopMultiplePricingOptions',
           'so_stop_policy_expired': 'SalesOrderStopPolicyExpired',
           'so_stop_no_pricing_found': 'SalesOrderStopNoPricingFound',
           'so_stop_policy_changed': 'SalesOrderStopPolicyChanged',
           'so_stop_manual_stop_date': 'SalesOrderStopManualStopDate',
           'so_stop_automatic_eligibility_check': 'SalesOrderStopAutomaticEligibilityCheck',
           'so_stop_ineligible_policy': 'SalesOrderStopIneligiblePolicy',
           'so_delivery_note': 'SalesOrderDeliveryNote',
           'work_in_progress_wip_state': 'WorkInProgressWIPState',
           'work_in_progress_assigned_to': 'WorkInProgressCompleted',
           'work_in_progress_completed': 'WorkInProgressCompleted',
           'work_in_progress_wip_days_in_state': 'WorkInProgressWIPDaysInState',
           'sleep_therapy_solution': 'SleepTherapySolution',
           'sleep_therapy_external_patient_id': 'SleepTherapyExternalPatientID',
           'marketing_rep_last_name': 'MarketingRepLastName',
           'marketing_rep_first_name': 'MarketingRepFirstName',
           'marketing_rep_full_name': 'MarketingRepFullName',
           'practitioner_last_name': 'PractitionerLastName',
           'practitioner_first_name': 'PractitionerFirstName',
           'practitioner_middle_name': 'PractitionerMiddleName',

           'delivery_scheduled_date': 'DeliveryScheduleddate',
           'delivery_actual_date': 'DeliveryActualdate',
           'delivery_address1': 'DeliveryAddress1',
           'delivery_address2': 'DeliveryAddress2',
           'delivery_city': 'DeliveryCity',
           'delivery_state': 'DeliveryState',
           'delivery_county': 'DeliveryCounty',
           'delivery_country': 'DeliveryCountry',
           'delivery_postal_code': 'DeliveryPostalCode',
           'delivery_phone': 'DeliveryPhone',
           'delivery_fax': 'DeliveryFax',
           'delivery_tax_zone': 'DeliveryTaxZone',
           'delivery_tax_rate': 'DeliveryTaxRate',
           'delivery_technician': 'DeliveryTechnician',
           'delivery_bright_ship_status': 'DeliveryBrightShipStatus',
           'delivery_bright_ship_carrier': 'DeliveryBrightShipCarrier',
           'delivery_bright_ship_method': 'DeliveryBrightShipMethod',
           'delivery_bright_ship_tracking_numbers': 'DeliveryBrightShipTrackingNumbers',
           'delivery_fulfillment_vendor': 'DeliveryFulfillmentVendor',
           'delivery_account_number': 'DeliveryAccountNumber',
           'delivery_ship_by': 'DeliveryShipBy',
           'delivery_status': 'DeliveryStatus',

           'patient_email_address': 'PatientEmailAddress',
           'patient_id': 'PatientID',
           'patient_date_created': 'PatientDateCreated',
           'patient_delivery_note': 'PatientDeliveryNote',
           'patient_branch': 'PatientBranch',
           'patient_bpc_auto_pay_status': 'PatientBPCAutoPAYStatus',
           'patient_bpc_edelivery_status': 'PatientBPCeDeliveryStatus',
           'patient_bpc_payment_plan': 'PatientBPCPaymentPlan',
           'patient_bpc_information': 'PatientBPCInformation',

           'ordering_doctor_last_name': 'OrderingDoctorLastName',
           'ordering_doctor_first_name': 'OrderingDoctorFirstName',
           'ordering_doctor_address1': 'OrderingDoctorAddress1',
           'ordering_doctor_address2': 'OrderingDoctorAddress2',
           'ordering_doctor_city': 'OrderingDoctorCity',
           'ordering_doctor_state': 'OrderingDoctorState',
           'ordering_doctor_postal_code': 'OrderingDoctorPostalCode',
           'ordering_doctor_phone': 'OrderingDoctorPhone',
           'ordering_doctor_fax': 'OrderingDoctorFax',
           'ordering_doctor_fax_to': 'OrderingDoctorFaxTo',
           'ordering_doctor_pecos_certify_status': 'OrderingDoctorPECOSCertifyStatus',
           'ordering_doctor_full_name': 'OrderingDoctorFullName',
           'ordering_doctor_group': 'OrderingDoctorGroup',
           'so_diagnosis_codes_dxicd-10_code_x0023_01': 'SalesOrderDiagnosisCodesDxICD-10Code_x0023_01',
           'so_diagnosis_codes_dxicd-10_description_x0023_01': 'SalesOrderDiagnosisCodesDxICD-10Description_x0023_01',
           'so_diagnosis_codes_dxicd-10_code_x0023_02': 'SalesOrderDiagnosisCodesDxICD-10Code_x0023_02',
           'so_diagnosis_codes_dxicd-10_description_x0023_02': 'SalesOrderDiagnosisCodesDxICD-10Description_x0023_02',
           'so_diagnosis_codes_dxicd-10_code_x0023_03': 'SalesOrderDiagnosisCodesDxICD-10Code_x0023_03',
           'so_diagnosis_codes_dxicd-10_description_x0023_03': 'SalesOrderDiagnosisCodesDxICD-10Description_x0023_03',
           'referral_type': 'ReferralType',
           'referral_name': 'ReferralName',
           'referral_address1': 'ReferralAddress1',
           'referral_city': 'ReferralCity',
           'referral_state': 'ReferralState',
           'referral_zip': 'ReferralZip',
           'referral_phone': 'ReferralPhone',
           'referral_fax': 'ReferralFax',
           'referral_doctor_group': 'ReferralDoctorGroup',
           'referral_facility_group': 'ReferralFacilityGroup',
           'insurance_pri_payor': 'InsurancePriPayor',
           'insurance_pri_policy_x0023': 'InsurancePriPolicy_x0023_',
           'insurance_pri_policy_x0023_': 'InsurancePriPolicy_x0023_',
           'insurance_pri_policy_verified': 'InsurancePriPolicyVerified',
           'insurance_pri_pay_pct': 'InsurancePriPayPct',
           'insurance_sec_payor': 'InsuranceSecPayor',
           'insurance_sec_policy_x0023_': 'InsuranceSecPolicy_x0023_',
           'insurance_sec_policy_verified': 'InsuranceSecPolicyVerified',
           'insurance_sec_payPct': 'InsuranceSecPayPct',
           'insurance_ter_payor': 'InsuranceTerPayor',
           'insurance_ter_policy_x0023_': 'InsuranceTerPolicy_x0023_',
           'insurance_insurance_verified': 'InsuranceInsuranceVerified',

           'sales_order_detail_item_id': 'SalesOrderDetailItemId',
           'sales_order_detail_item_name': 'SalesOrderDetailItemName',
           'sales_order_detail_item_description': 'SalesOrderDetailItemDescription',
           'sales_order_detail_stocking_uom': 'SalesOrderDetailStockingUOM',
           'sales_order_detail_original_dos': 'SalesOrderDetailOriginalDOS',
           'sales_order_detail_special_pricing': 'SalesOrderDetailSpecialPricing',
           'sales_order_detail_price_override': 'SalesOrderDetailPriceOverride',
           'sales_order_detail_qty': 'SalesOrderDetailQty',
           'sales_order_detail_bqty': 'SalesOrderDetailBqty',
           'sales_order_detail_proc_code': 'SalesOrderDetailProcCode',
           'sales_order_detail_price_option': 'SalesOrderDetailPriceOption',
           'sales_order_detail_modifier1': 'SalesOrderDetailModifier1',
           'sales_order_detail_modifier2': 'SalesOrderDetailModifier2',
           'sales_order_detail_modifier3': 'SalesOrderDetailModifier3',
           'sales_order_detail_modifier4': 'SalesOrderDetailModifier4',
           'sales_order_detail_charge': 'SalesOrderDetailCharge',
           'sales_order_detail_allow': 'SalesOrderDetailAllow',
           'sales_order_detail_taxable': 'SalesOrderDetailTaxable',
           'sales_order_detail_non_tax_reason': 'SalesOrderDetailNonTaxReason',
           'sales_order_detail_sale_type': 'SalesOrderDetailSaleType',
           'sales_order_detail_item_group': 'SalesOrderDetailItemGroup',
           'sales_order_detail_item_user1': 'SalesOrderDetailItemUser1',
           'sales_order_detail_manual_convert_to_purchase_mctp': 'SalesOrderDetailManualConvertToPurchaseMCTP',
           'sales_order_detail_mctp_charge': 'SalesOrderDetailMCTPCharge',
           'sales_order_detail_mctp_allow': 'SalesOrderDetailMCTPAllow',
           'sales_order_detail_mctp_modifier1': 'SalesOrderDetailMCTPModifier1',
           'sales_order_detail_mctp_modifier2': 'SalesOrderDetailMCTPModifier2',
           'sales_order_detail_mctp_modifier3': 'SalesOrderDetailMCTPModifier3',
           'sales_order_detail_mctp_modifier4': 'SalesOrderDetailMCTPModifier4',
           'sales_order_detail_mctp_period': 'SalesOrderDetailMCTPPeriod',
           'sales_order_detail_addtl_modifier1': 'SalesOrderDetailAddtlModifier1',
           'sales_order_detail_addtl_modifier2': 'SalesOrderDetailAddtlModifier2',
           'sales_order_detail_addtl_modifier3': 'SalesOrderDetailAddtlModifier3',
           'sales_order_detail_addtl_modifier4': 'SalesOrderDetailAddtlModifier4',
           'sales_order_detail_price_table': 'SalesOrderDetailPriceTable',
           'sales_order_detail_price_option_name': 'SalesOrderDetailPriceOptionName',
           'sales_order_detail_extended_charge_amount': 'SalesOrderDetailExtendedChargeAmount',
           'sales_order_detail_extended_allowance_amount': 'SalesOrderDetailExtendedAllowanceAmount',
           'sales_order_detail_cb_pricing': 'SalesOrderDetailCBPricing',
           'sales_order_detail_cb_price_table_override': 'SalesOrderDetailCBPriceTableOverride',
           'sales_order_detail_cb_override': 'SalesOrderDetailCBOverride',
           'sales_order_detail_messages': 'SalesOrderDetailMessages',
           'sales_order_detail_default_vendor': 'SalesOrderDetailDefaultVendor',
           'sales_order_detail_calories_per_day': 'SalesOrderDetailCaloriesPerDay',
           'sales_order_detail_location': 'SalesOrderDetailLocation',

           'invoice_number': 'InvoiceNumber',
           'invoice_status': 'InvoiceStatus',
           'invoice_sales_order_number': 'InvoiceSalesOrderNumber',
           'invoice_holdfromprinting_x002_f_submission': 'InvoiceHoldfromprinting_x002F_submission',
           'invoice_medicare_deductible_hold': 'InvoiceMedicareDeductibleHold',
           'invoice_user_manual_hold': 'InvoiceUserManualHold',
           'invoice_holdfrom_billing_statement': 'InvoiceHoldfromBillingStatement',
           'invoice_so_manual_hold_reason': 'InvoiceSOManualHoldReason',
           'invoice_biller_x002_f_collector': 'InvoiceBiller_x002F_Collector',
           'invoice_last_date_worked': 'InvoiceLastDateWorked',
           'invoice_follow_up_date': 'InvoiceFollowUpDate',
           'invoice_collection_type': 'InvoiceCollectionType',
           'invoice_collect_action_x002_f_status': 'InvoiceCollectAction_x002F_Status',
           'invoice_pro_med_status_code': 'InvoiceProMedStatusCode',
           'invoice_pro_med_status_code_date': 'InvoiceProMedStatusCodeDate',
           'invoice_appeals_due_date': 'InvoiceAppealsDueDate',
           'balances_charge_total': 'BalancesChargeTotal',
           'balances_allow_total': 'BalancesAllowTotal',
           'balances_tax_total': 'BalancesTaxTotal',
           'balances_adjustments': 'BalancesAdjustments',
           'balances_balance': 'BalancesBalance',
           'balances_payments': 'BalancesPayments',
           'work_in_progress_assigned_to': 'WorkInProgressAssignedTo',
           'sales_order_hold_cmn_not_logged': 'SalesOrderHoldCMNNotLogged',
           'sales_order_hold_cmn_expired': 'SalesOrderHoldCMNExpired',
           'sales_order_hold_par_not_logged': 'SalesOrderHoldPARNotLogged',
           'sales_order_hold_par_expired': 'SalesOrderHoldPARExpired',
           'sales_order_hold_manual_hold': 'SalesOrderHoldManualHold',
           'sales_order_stop_pending_pickup': 'SalesOrderStopPendingPickup',
           'sales_order_stop_multiple_pricing_options': 'SalesOrderStopMultiplePricingOptions',
           'sales_order_stop_policy_expired': 'SalesOrderStopPolicyExpired',
           'sales_order_stop_no_pricing_found': 'SalesOrderStopNoPricingFound',
           'sales_order_stop_policy_changed': 'SalesOrderStopPolicyChanged',
           'sales_order_stop_manual_stop_date': 'SalesOrderStopManualStopDate',
           'sales_order_stop_automatic_eligibility_check': 'SalesOrderStopAutomaticEligibilityCheck',
           'sales_order_stop_ineligible_policy': 'SalesOrderStopIneligiblePolicy',


           'par_number': 'PARNumber',
           'par_descr': 'PARDescr',
           'par_exclude_from_par_report': 'PARExcludeFromPARReport',
           'par_exclude_from_claim': 'PARExcludeFromClaim',
           'par_status': 'PARStatus',
           'par_create_date': 'PARCreateDate',
           'par_created_by': 'PARCreatedBy',
           'par_logged_by': 'PARLoggedBy',
           'par_insurance': 'PARInsurance',
           'par_branch': 'PARBranch',
           'par_printed_by': 'PARPrintedBy',
           'par_faxed_by': 'PARFaxedBy',
           'par_purchase_quantity_limits_proc_code': 'PARPurchaseQuantityLimitsProcCode',
           'par_purchase_quantity_limits_approved_qty': 'PARPurchaseQuantityLimitsApprovedQTY',
           'par_purchase_quantity_limits_returned_qty': 'PARPurchaseQuantityLimitsReturnedQTY',
           'par_purchase_quantity_limits_used_qty': 'PARPurchaseQuantityLimitsUsedQTY',
           'par_purchase_quantity_limits_adjusted_qty': 'PARPurchaseQuantityLimitsAdjustedQTY',
           'patient_key': 'PatientKey',
           'sales_order_number': 'SalesOrderNumber',
           'insurance_pri_payor_id': 'InsurancePriPayorID',
           'cmncmn_form': 'CMNCMNForm',
           'cmncmn_exp': 'CMNCMNExp',
           'cmncmn_init': 'CMNCMNInit',
           'cmncmn_status': 'CMNCMNStatus',
           'cmncmn_log_date': 'CMNCMNLogDate',
           'cmncmn_lengthof_need': 'CMNCMNLengthofNeed',
           'cmn_excludefrom_cmn_report': 'CMNExcludefromCMNReport',
           'cmncmn_faxed_by': 'CMNCMNFaxedBy',
           'cmncmn_placeholder': 'CMNCMNPlaceholder',

           'invoice_number': 'InvoiceNumber',
           'invoice_status': 'InvoiceStatus',
           'invoice_sales_order_number': 'InvoiceSalesOrderNumber',
           'invoice_date_created': 'InvoiceDateCreated',
           'invoice_dateof_service': 'InvoiceDateofService',
           'invoice_holdfromprinting_x002_f_submission': 'InvoiceHoldfromprinting_x002F_submission',
           'invoice_medicare_deductible_hold': 'InvoiceMedicareDeductibleHold',
           'invoice_reprint_x002_f_re_submit_claim': 'InvoiceReprint_x002F_ReSubmitClaim',
           'invoice_span_date_hold': 'InvoiceSpanDateHold',
           'invoice_branch': 'InvoiceBranch',
           'invoice_so_reference': 'InvoiceSOReference',
           'invoice_branch_group': 'InvoiceBranchGroup',
           'invoice_box19': 'InvoiceBox19',
           'invoice_so_place_of_service': 'InvoiceSOPlaceOfService',
           'invoice_so_classification': 'InvoiceSOClassification',
           'invoice_so_note': 'InvoiceSONote',
           'invoice_so_manual_hold_reason': 'InvoiceSOManualHoldReason',
           'invoice_so_created_by': 'InvoiceSOCreatedBy',
           'invoice_so_confirmed_by': 'InvoiceSOConfirmedBy',
           'invoice_submission_type': 'InvoiceSubmissionType',
           'invoice_key': 'InvoiceKey',
           'invoice_balances_charge_total': 'InvoiceBalancesChargeTotal',
           'invoice_balances_allow_total': 'InvoiceBalancesAllowTotal',
           'invoice_balances_tax_total': 'InvoiceBalancesTaxTotal',
           'invoice_balances_adjustments': 'InvoiceBalancesAdjustments',
           'invoice_balances_payments': 'InvoiceBalancesPayments',
           'invoice_balances_balance': 'InvoiceBalancesBalance',
           'policy_payor_name': 'PolicyPayorName',
           'policy_payor_id': 'PolicyPayorID',
           'policy_x0023': 'Policy_x0023_',
           'policy_group_x0023': 'PolicyGroup_x0023_',
           'policy_pay': 'PolicyPay',
           'policy_claim_form': 'PolicyClaimForm',
           'policy_payor_level': 'PolicyPayorLevel',
           'policy_plan_type': 'PolicyPlanType',
           'policy_do_not_print_secondary_claims': 'PolicyDoNotPrintSecondaryClaims',
           'invoice_detail_item_id': 'InvoiceDetailItemID',
           'invoice_detail_item_name': 'InvoiceDetailItemName',
           'invoice_detail_dos_from': 'InvoiceDetailDOSFrom',
           'invoice_detail_dos_to': 'InvoiceDetailDOSTo',
           'invoice_detail_billing_period': 'InvoiceDetailBillingPeriod',
           'invoice_detail_reprint_x002_f_resubmit_item': 'InvoiceDetailReprint_x002F_ResubmitItem',
           'invoice_detail_charge': 'InvoiceDetailCharge',
           'invoice_detail_allow': 'InvoiceDetailAllow',
           'invoice_detail_tax': 'InvoiceDetailTax',
           'invoice_detail_payments': 'InvoiceDetailPayments',
           'invoice_detail_balance': 'InvoiceDetailBalance',
           'invoice_detail_qty': 'InvoiceDetailQty',
           'invoice_detail_inventory_qty': 'InvoiceDetailInventoryQty',
           'invoice_detail_proc_code': 'InvoiceDetailProcCode',
           'invoice_detail_modifier1': 'InvoiceDetailModifier1',
           'invoice_detail_modifier2': 'InvoiceDetailModifier2',
           'invoice_detail_modifier3': 'InvoiceDetailModifier3',
           'invoice_detail_modifier4': 'InvoiceDetailModifier4',
           'invoice_detail_abn_proc_code': 'InvoiceDetailABNProcCode',
           'invoice_detail_price_type': 'InvoiceDetailPriceType',
           'invoice_detail_so_item_note': 'InvoiceDetailSOItemNote',
           'invoice_detail_par_number': 'InvoiceDetailParNumber',
           'ordering_doctor_key': 'OrderingDoctorKey',
           'ordering_doctor_npi': 'OrderingDoctorNPI',
           'serial_numbers_serial_number': 'SerialNumbersSerialNumber',
           'work_in_progress_assigned_to': 'WorkInProgressAssignedTo',
           'primary_invoice_primary_invoice_number': 'PrimaryInvoicePrimaryInvoiceNumber',
           'primary_invoice_primary_insurance_name': 'PrimaryInvoicePrimaryInsuranceName',
           'secondary_invoice_secondary_invoice_number': 'SecondaryInvoiceSecondaryInvoiceNumber',
           'secondary_invoice_secondary_insurance_name': 'SecondaryInvoiceSecondaryInsuranceName',
           'tertiary_invoice_tertiary_invoice_number': 'TertiaryInvoiceTertiaryInvoiceNumber',
           'tertiary_invoice_tertiary_insurance_name': 'TertiaryInvoiceTertiaryInsuranceName',
           'patient_invoice_patient_invoice_number': 'PatientInvoicePatientInvoiceNumber',
           'patient_invoice_patient_insurance_name': 'PatientInvoicePatientInsuranceName',
           'responsible_party_relationship': 'ResponsiblePartyRelationship',
           'responsible_party_phone': 'ResponsiblePartyPhone',
           'responsible_party_email_address': 'ResponsiblePartyEmailAddress',

           'par_number': 'PARNumber',
           'par_descr': 'PARDescr',
           'par_init': 'PARInit',
           'par_exclude_from_par_report': 'PARExcludeFromPARReport',
           'par_exclude_from_claim': 'PARExcludeFromClaim',
           'par_status': 'PARStatus',
           'par_create_date': 'PARCreateDate',
           'par_created_by': 'PARCreatedBy',
           'par_logged_date': 'PARLoggedDate',
           'par_logged_by': 'PARLoggedBy',
           'par_insurance': 'PARInsurance',
           'par_branch': 'PARBranch',
           'par_printed_by': 'PARPrintedBy',
           'par_faxed_by': 'PARFaxedBy',
           'par_purchase_quantity_limits_proc_code': 'PARPurchaseQuantityLimitsProcCode',
           'par_purchase_quantity_limits_approved_qty': 'PARPurchaseQuantityLimitsApprovedQTY',
           'par_purchase_quantity_limits_returned_qty': 'PARPurchaseQuantityLimitsReturnedQTY',
           'par_purchase_quantity_limits_used_qty': 'PARPurchaseQuantityLimitsUsedQTY',
           'par_purchase_quantity_limits_adjusted_qty': 'PARPurchaseQuantityLimitsAdjustedQTY',
           'patient_key': 'PatientKey',
           'insurance_pri_payor_id': 'InsurancePriPayorID',
           'cmncmn_form': 'CMNCMNForm',
           'cmncmn_exp': 'CMNCMNExp',
           'cmncmn_init': 'CMNCMNInit',
           'cmncmn_status': 'CMNCMNStatus',
           'cmncmn_log_date': 'CMNCMNLogDate',
           'cmncmn_lengthof_need': 'CMNCMNLengthofNeed',
           'cmn_excludefrom_cmn_report': 'CMNExcludefromCMNReport',
           'cmncmn_faxed_by': 'CMNCMNFaxedBy',
           'cmncmn_placeholder': 'CMNCMNPlaceholder',

           'sales_order_void_voided_sales_order_number': 'SalesOrderVoidVoidedSalesOrderNumber',
           'sales_order_void_void_reason': 'SalesOrderVoidVoidReason',
           'sales_order_void_voided_by': 'SalesOrderVoidVoidedBy',
           'sales_order_void_voided_date': 'SalesOrderVoidVoidedDate',

           'activity_task_id': 'ActivityTaskID',
           'activity_type': 'ActivityType',
           'activity': 'Activity',
           'priority': 'Priority',
           'assigned_to': 'AssignedTo',
           'amount': 'Amount',
           'task_status': 'TaskStatus',
           'create_date': 'CreateDate',
           'closed_date': 'ClosedDate',
           'patient_name': 'PatientName',
           'insurance_id': 'InsuranceID',
           'insurance_name': 'InsuranceName',
           'note': 'Note',
           'work_item_name': 'WorkItemName',
           'work_item_id': 'WorkItemID',
           'work_item_branch': 'WorkItemBranch',

           'payment_id': 'PaymentID',
           'payment_check_x002_f_reference': 'PaymentCheck_x002F_Reference',
           'payment_type': 'PaymentType',
           'payment_created_by': 'PaymentCreatedBy',
           'payment_create_date': 'PaymentCreateDate',
           'payment_date': 'PaymentDate',
           'payment_post_date': 'PaymentPostDate',
           'payment_posted_by': 'PaymentPostedBy',
           'payment_description': 'PaymentDescription',
           'payment_amount': 'PaymentAmount',
           'payment_gl_period': 'PaymentGLPeriod',
           'payment_gl_year': 'PaymentGLYear',
           'payment_gl_start_date': 'PaymentGLStartDate',
           'payment_gl_end_date': 'PaymentGLEndDate',
           'receipt_type': 'ReceiptType',
           'receipt_check_x002_f_reference': 'ReceiptCheck_x002F_Reference',
           'receipt_note': 'ReceiptNote',
           'deposit_created_by': 'DepositCreatedBy',
           'deposit_posted_by': 'DepositPostedBy',
           'deposit_reference': 'DepositReference',
           'deposit_description': 'DepositDescription',
           'invoice_number': 'InvoiceNumber',
           'invoice_status': 'InvoiceStatus',
           'invoice_sales_order_number': 'InvoiceSalesOrderNumber',
           'invoice_date_created': 'InvoiceDateCreated',
           'invoice_dateof_service': 'InvoiceDateofService',
           'invoice_holdfromprinting_x002_f_submission': 'InvoiceHoldfromprinting_x002F_submission',
           'invoice_reprint_x002_f_re_submit_claim': 'InvoiceReprint_x002F_ReSubmitClaim',
           'invoice_branch': 'InvoiceBranch',
           'invoice_note': 'InvoiceNote',
           'invoice_so_created_by': 'InvoiceSOCreatedBy',
           'invoice_so_confirmed_by': 'InvoiceSOConfirmedBy',
           'invoice_balances_charge_total': 'InvoiceBalancesChargeTotal',
           'invoice_balances_allow_total': 'InvoiceBalancesAllowTotal',
           'invoice_balances_tax_total': 'InvoiceBalancesTaxTotal',
           'invoice_balances_adjustments': 'InvoiceBalancesAdjustments',
           'invoice_balances_payments': 'InvoiceBalancesPayments',
           'invoice_balances_balance': 'InvoiceBalancesBalance',
           'invoice_biller_x002_f_collector': 'InvoiceBiller_x002F_Collector',
           'invoice_last_date_worked': 'InvoiceLastDateWorked',
           'invoice_follow_up_date': 'InvoiceFollowUpDate',
           'invoice_collection_type': 'InvoiceCollectionType',
           'invoice_collect_action_x002_f_status': 'InvoiceCollectAction_x002F_Status',
           'invoice_pro_med_status_code': 'InvoiceProMedStatusCode',
           'invoice_pro_med_status_code_date': 'InvoiceProMedStatusCodeDate',
           'invoice_appeals_due_date': 'InvoiceAppealsDueDate',
           'sales_order_so_number': 'SalesOrderSONumber',
           'policy_payor_name': 'PolicyPayorName',
           'policy_payor_id': 'PolicyPayorID',
           'policy_x0023': 'Policy_x0023_',
           'policy_pay': 'PolicyPay',
           'invoice_detail_id': 'InvoiceDetailID',
           'invoice_detail_item_id': 'InvoiceDetailItemID',
           'related_invoice_primary_invoice_nbr': 'RelatedInvoicePrimaryInvoiceNbr',
           'related_invoice_secondary_invoice_nbr': 'RelatedInvoiceSecondaryInvoiceNbr',
           'related_invoice_tertiary_invoice_nbr': 'RelatedInvoiceTertiaryInvoiceNbr',
           'related_invoice_patient_invoice_nbr': 'RelatedInvoicePatientInvoiceNbr'

         }


def get_col_val(rec, key):
    """"""
    if SO_MAP[key] in rec.keys() and type(rec[SO_MAP[key]]) in [type(''), type(u'')]:
       val = rec[SO_MAP[key]]
       if val.lower() == 'false': 
          val = 0
       elif val.lower() == 'true':
          val = 1
    else:
       val = ''

    if 'date' in key or 'dos' in key:
        val = val.replace('T', ' ')

    if type(val) in [type(''), type(u'')]:
        val = val.replace('"', '&quote;')

    return val


def insert_data_so(rec):
    """"""
    #print ("sales_order: inserting data for SO #." +  str(get_col_val(rec, 'so_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `sales_order` (`so_number`,
                                        `so_date_created`,
                                        `so_created_by`,
                                        `so_branch_office`,
                                        `so_location`,
                                        `so_classification`,
                                        `so_status`,
                                        `so_reference`,
                                        `so_confirm_date`,
                                        `work_in_progress_state`,
                                        `patient_id`,
                                        `ordering_doctor_city`,
                                        `ordering_doctor_state`,
                                        `insurance_pri_payor`,
                                        `marketing_rep_fullname`,
                                        `referral_name`,
                                        `referral_city`,
                                        `referral_state`)
                                VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                        "%s", "%s", "%s", "%s", "%s", "%s", "%s"  ) 
    """ % (

                       get_col_val(rec, 'so_number'),
                       get_col_val(rec, 'so_date_created'),
                       get_col_val(rec, 'so_created_by'),
                       get_col_val(rec, 'so_branch_office'),
                       get_col_val(rec, 'so_location'),
                       get_col_val(rec, 'so_classification'),
                       get_col_val(rec, 'so_status'),
                       get_col_val(rec, 'so_reference'),
                       get_col_val(rec, 'so_confirm_date'),
                       get_col_val(rec, 'work_in_progress_state'),
                       get_col_val(rec, 'patient_id'),
                       get_col_val(rec, 'ordering_doctor_city'),
                       get_col_val(rec, 'ordering_doctor_state'),
                       get_col_val(rec, 'insurance_pri_payor'),
                       get_col_val(rec, 'marketing_rep_fullname'),
                       get_col_val(rec, 'referral_name'),
                       get_col_val(rec, 'referral_city'),
                       get_col_val(rec, 'referral_state')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with SO #.' + str(get_col_val(rec, 'so_number')) )
        print (sql)
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_soc(rec):
    """"""
    #print ("sales_order_confirmed: inserting data for SO #." + str(get_col_val(rec, 'so_number')))

    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    #
    # sql statements .....
    sql_soc = """INSERT INTO `sales_order_confirmed` (
                                                 `so_number`, 
                                                 `so_date_created`, 
                                                 `so_created_by`, 
                                                 `so_branch_office`, 
                                                 `so_status`, 
                                                 `so_manual_hold`, 
                                                 `so_location`, 
                                                 `so_po_number`, 
                                                 `so_purchase_order_number`, 
                                                 `so_reference`, 
                                                 `so_user1`, 
                                                 `so_user2`, 
                                                 `so_user3`, 
                                                 `so_user4`, 
                                                 `so_confirm_date`, 
                                                 `so_confirmed_by`, 
                                                 `so_last_printed`, 
                                                 `so_note`, 
                                                 `so_classification`, 
                                                 `so_type`, 
                                                 `so_manual_hold_reason`, 
                                                 `so_custom_fields_field1`, 
                                                 `so_custom_fields_field2`, 
                                                 `so_custom_fields_field3`, 
                                                 `so_custom_fields_field4`, 
                                                 `so_custom_fields_field5`, 
                                                 `so_custom_fields_field6`, 
                                                 `so_custom_fields_field7`, 
                                                 `so_custom_fields_field8`, 
                                                 `so_custom_fields_field9`, 
                                                 `so_custom_fields_field10`, 
                                                 `so_custom_fields_field11`, 
                                                 `so_custom_fields_field12`, 
                                                 `so_custom_fields_field13`, 
                                                 `so_custom_fields_field14`, 
                                                 `so_custom_fields_field15`, 
                                                 `so_custom_fields_field16`, 
                                                 `so_custom_fields_field17`, 
                                                 `so_custom_fields_field18`, 
                                                 `so_custom_fields_field19`, 
                                                 `so_hold_cmn_not_logged`, 
                                                 `so_hold_cmn_expired`, 
                                                 `so_hold_par_not_logged`, 
                                                 `so_hold_par_expired`, 
                                                 `so_hold_manual_hold`, 
                                                 `so_stop_pending_pickup`, 
                                                 `so_stop_multiple_pricing_options`, 
                                                 `so_stop_policy_expired`, 
                                                 `so_stop_no_pricing_found`, 
                                                 `so_stop_policy_changed`, 
                                                 `so_stop_manual_stop_date`, 
                                                 `so_stop_automatic_eligibility_check`, 
                                                 `so_stop_ineligible_policy`, 
                                                 `so_delivery_note`, 
                                                 `work_in_progress_wip_state`, 
                                                 `work_in_progress_assigned_to`, 
                                                 `work_in_progress_completed`, 
                                                 `work_in_progress_wip_days_in_state`, 
                                                 `sleep_therapy_solution`, 
                                                 `sleep_therapy_external_patient_id`, 
                                                 `marketing_rep_last_name`, 
                                                 `marketing_rep_first_name`, 
                                                 `marketing_rep_full_name`, 
                                                 `practitioner_last_name`, 
                                                 `practitioner_first_name`, 
                                                 `practitioner_middle_name`) 
                                         VALUES (
                                                 "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                                 "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                                 "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                                 "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                                 "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                                 "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                                 "%s", "%s", "%s", "%s", "%s", "%s" 
    ) """ % (
                                get_col_val(rec, 'so_number'), 
                                get_col_val(rec, 'so_date_created'), 
                                get_col_val(rec, 'so_created_by'), 
                                get_col_val(rec, 'so_branch_office'), 
                                get_col_val(rec, 'so_status'), 
                                get_col_val(rec, 'so_manual_hold'), 
                                get_col_val(rec, 'so_location'), 
                                get_col_val(rec, 'so_po_number'), 
                                get_col_val(rec, 'so_purchase_order_number'), 
                                get_col_val(rec, 'so_reference'), 
                                get_col_val(rec, 'so_user1'), 
                                get_col_val(rec, 'so_user2'), 
                                get_col_val(rec, 'so_user3'), 
                                get_col_val(rec, 'so_user4'), 
                                get_col_val(rec, 'so_confirm_date'), 
                                get_col_val(rec, 'so_confirmed_by'), 
                                get_col_val(rec, 'so_last_printed'), 
                                get_col_val(rec, 'so_note'), 
                                get_col_val(rec, 'so_classification'), 
                                get_col_val(rec, 'so_type'), 
                                get_col_val(rec, 'so_manual_hold_reason'), 
                                get_col_val(rec, 'so_custom_fields_field1'), 
                                get_col_val(rec, 'so_custom_fields_field2'), 
                                get_col_val(rec, 'so_custom_fields_field3'), 
                                get_col_val(rec, 'so_custom_fields_field4'), 
                                get_col_val(rec, 'so_custom_fields_field5'), 
                                get_col_val(rec, 'so_custom_fields_field6'), 
                                get_col_val(rec, 'so_custom_fields_field7'), 
                                get_col_val(rec, 'so_custom_fields_field8'), 
                                get_col_val(rec, 'so_custom_fields_field9'), 
                                get_col_val(rec, 'so_custom_fields_field10'), 
                                get_col_val(rec, 'so_custom_fields_field11'), 
                                get_col_val(rec, 'so_custom_fields_field12'), 
                                get_col_val(rec, 'so_custom_fields_field13'), 
                                get_col_val(rec, 'so_custom_fields_field14'), 
                                get_col_val(rec, 'so_custom_fields_field15'), 
                                get_col_val(rec, 'so_custom_fields_field16'), 
                                get_col_val(rec, 'so_custom_fields_field17'), 
                                get_col_val(rec, 'so_custom_fields_field18'), 
                                get_col_val(rec, 'so_custom_fields_field19'), 
                                get_col_val(rec, 'so_hold_cmn_not_logged'), 
                                get_col_val(rec, 'so_hold_cmn_expired'), 
                                get_col_val(rec, 'so_hold_par_not_logged'), 
                                get_col_val(rec, 'so_hold_par_expired'), 
                                get_col_val(rec, 'so_hold_manual_hold'), 
                                get_col_val(rec, 'so_stop_pending_pickup'), 
                                get_col_val(rec, 'so_stop_multiple_pricing_options'), 
                                get_col_val(rec, 'so_stop_policy_expired'), 
                                get_col_val(rec, 'so_stop_no_pricing_found'), 
                                get_col_val(rec, 'so_stop_policy_changed'), 
                                get_col_val(rec, 'so_stop_manual_stop_date'), 
                                get_col_val(rec, 'so_stop_automatic_eligibility_check'), 
                                get_col_val(rec, 'so_stop_ineligible_policy'), 
                                get_col_val(rec, 'so_delivery_note'), 
                                get_col_val(rec, 'work_in_progress_wip_state'), 
                                get_col_val(rec, 'work_in_progress_assigned_to'), 
                                get_col_val(rec, 'work_in_progress_completed'), 
                                get_col_val(rec, 'work_in_progress_wip_days_in_state'), 
                                get_col_val(rec, 'sleep_therapy_solution'), 
                                get_col_val(rec, 'sleep_therapy_external_patient_id'), 
                                get_col_val(rec, 'marketing_rep_last_name'), 
                                get_col_val(rec, 'marketing_rep_first_name'), 
                                get_col_val(rec, 'marketing_rep_full_name'), 
                                get_col_val(rec, 'practitioner_last_name'), 
                                get_col_val(rec, 'practitioner_first_name'), 
                                get_col_val(rec, 'practitioner_middle_name') )

    sql_dlvry = """INSERT INTO `soc_delivery` (
                                               `so_number`,
                                               `delivery_scheduled_date`,
                                               `delivery_actual_date`,
                                               `delivery_address1`,
                                               `delivery_address2`,
                                               `delivery_city`,
                                               `delivery_state`,
                                               `delivery_county`,
                                               `delivery_country`,
                                               `delivery_postal_code`,
                                               `delivery_phone`,
                                               `delivery_fax`,
                                               `delivery_tax_zone`,
                                               `delivery_tax_rate`,
                                               `delivery_technician`,
                                               `delivery_bright_ship_status`,
                                               `delivery_bright_ship_carrier`,
                                               `delivery_bright_ship_method`,
                                               `delivery_bright_ship_tracking_numbers`,
                                               `delivery_fulfillment_vendor`,
                                               `delivery_account_number`,
                                               `delivery_ship_by`,
                                               `delivery_status` )
                                       VALUES (
                                               "%s", "%s", "%s",
                                               "%s", "%s", "%s",
                                               "%s", "%s", "%s",
                                               "%s", "%s", "%s",
                                               "%s", "%s", "%s",
                                               "%s", "%s", "%s",
                                               "%s", "%s", "%s",
                                               "%s", "%s"
                                              )
    """ % (
                              get_col_val(rec, 'so_number'),
                              get_col_val(rec, 'delivery_scheduled_date'),
                              get_col_val(rec, 'delivery_actual_date'),
                              get_col_val(rec, 'delivery_address1'),
                              get_col_val(rec, 'delivery_address2'),
                              get_col_val(rec, 'delivery_city'),
                              get_col_val(rec, 'delivery_state'),
                              get_col_val(rec, 'delivery_county'),
                              get_col_val(rec, 'delivery_country'),
                              get_col_val(rec, 'delivery_postal_code'),
                              get_col_val(rec, 'delivery_phone'),
                              get_col_val(rec, 'delivery_fax'),
                              get_col_val(rec, 'delivery_tax_zone'),
                              get_col_val(rec, 'delivery_tax_rate'),
                              get_col_val(rec, 'delivery_technician'),
                              get_col_val(rec, 'delivery_bright_ship_status'),
                              get_col_val(rec, 'delivery_bright_ship_carrier'),
                              get_col_val(rec, 'delivery_bright_ship_method'),
                              get_col_val(rec, 'delivery_bright_ship_tracking_numbers'),
                              get_col_val(rec, 'delivery_fulfillment_vendor'),
                              get_col_val(rec, 'delivery_account_number'),
                              get_col_val(rec, 'delivery_ship_by'),
                              get_col_val(rec, 'delivery_status')
    )

    sql_patient = """INSERT INTO `soc_patient` (
                                               `so_number`,
                                               `patient_email_address`,
                                               `patient_id`,
                                               `patient_date_created`,
                                               `patient_delivery_note`,
                                               `patient_branch`,
                                               `patient_bpc_auto_pay_status`,
                                               `patient_bpc_edelivery_status`,
                                               `patient_bpc_payment_plan`,
                                               `patient_bpc_information` )
                                        VALUES (
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s", "%s", "%s", "%s", "%s"
                                               )
    """ % (
                              get_col_val(rec, 'so_number'),
                              get_col_val(rec, 'patient_email_address'),
                              get_col_val(rec, 'patient_id'),
                              get_col_val(rec, 'patient_date_created'),
                              get_col_val(rec, 'patient_delivery_note'),
                              get_col_val(rec, 'patient_branch'),
                              get_col_val(rec, 'patient_bpc_auto_pay_status'),
                              get_col_val(rec, 'patient_bpc_edelivery_status'),
                              get_col_val(rec, 'patient_bpc_payment_plan'),
                              get_col_val(rec, 'patient_bpc_information')
    )
    
    sql_odoc = """INSERT INTO `soc_ordering_doctor` (
                                               `so_number`,
                                               `ordering_doctor_last_name`,
                                               `ordering_doctor_first_name`,
                                               `ordering_doctor_address1`,
                                               `ordering_doctor_address2`,
                                               `ordering_doctor_city`,
                                               `ordering_doctor_state`,
                                               `ordering_doctor_postal_code`,
                                               `ordering_doctor_phone`,
                                               `ordering_doctor_fax`,
                                               `ordering_doctor_fax_to`,
                                               `ordering_doctor_pecos_certify_status`,
                                               `ordering_doctor_full_name`,
                                               `ordering_doctor_group` )
                                        VALUES (
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s", "%s", "%s", "%s"
                                               )
    """ % (
                              get_col_val(rec, 'so_number'),
                              get_col_val(rec, 'ordering_doctor_last_name'),
                              get_col_val(rec, 'ordering_doctor_first_name'),
                              get_col_val(rec, 'ordering_doctor_address1'),
                              get_col_val(rec, 'ordering_doctor_address2'),
                              get_col_val(rec, 'ordering_doctor_city'),
                              get_col_val(rec, 'ordering_doctor_state'),
                              get_col_val(rec, 'ordering_doctor_postal_code'),
                              get_col_val(rec, 'ordering_doctor_phone'),
                              get_col_val(rec, 'ordering_doctor_fax'),
                              get_col_val(rec, 'ordering_doctor_fax_to'),
                              get_col_val(rec, 'ordering_doctor_pecos_certify_status'),
                              get_col_val(rec, 'ordering_doctor_full_name'),
                              get_col_val(rec, 'ordering_doctor_group')
    )

    sql_dgns = """INSERT INTO `soc_diagnosis` (
                                               `so_number`,
                                               `so_diagnosis_codes_dxicd-10_code_x0023_01`,
                                               `so_diagnosis_codes_dxicd-10_description_x0023_01`,
                                               `so_diagnosis_codes_dxicd-10_code_x0023_02`,
                                               `so_diagnosis_codes_dxicd-10_description_x0023_02`,
                                               `so_diagnosis_codes_dxicd-10_code_x0023_03`,
                                               `so_diagnosis_codes_dxicd-10_description_x0023_03` )
                                        VALUES (
                                                "%s", 
                                                "%s", "%s", "%s",
                                                "%s", "%s", "%s"
                                               )
    """ % (
                              get_col_val(rec, 'so_number'),
                              get_col_val(rec, 'so_diagnosis_codes_dxicd-10_code_x0023_01'),
                              get_col_val(rec, 'so_diagnosis_codes_dxicd-10_description_x0023_01'),
                              get_col_val(rec, 'so_diagnosis_codes_dxicd-10_code_x0023_02'),
                              get_col_val(rec, 'so_diagnosis_codes_dxicd-10_description_x0023_02'),
                              get_col_val(rec, 'so_diagnosis_codes_dxicd-10_code_x0023_03'),
                              get_col_val(rec, 'so_diagnosis_codes_dxicd-10_description_x0023_03')
    )

    sql_rfrl = """INSERT INTO `soc_referral` (
                                               `so_number`,
                                               `referral_type`,
                                               `referral_name`,
                                               `referral_address1`,
                                               `referral_city`,
                                               `referral_state`,
                                               `referral_zip`,
                                               `referral_phone`,
                                               `referral_fax`,
                                               `referral_doctor_group`,
                                               `referral_facility_group` )
                                        VALUES (
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s"
                                               ) 
    """ % (
                              get_col_val(rec, 'so_number'),
                              get_col_val(rec, 'referral_type'),
                              get_col_val(rec, 'referral_name'),
                              get_col_val(rec, 'referral_address1'),
                              get_col_val(rec, 'referral_city'),
                              get_col_val(rec, 'referral_state'),
                              get_col_val(rec, 'referral_zip'),
                              get_col_val(rec, 'referral_phone'),
                              get_col_val(rec, 'referral_fax'),
                              get_col_val(rec, 'referral_doctor_group'),
                              get_col_val(rec, 'referral_facility_group')
    )

    sql_insrnc = """INSERT INTO `soc_insurance` (
                                               `so_number`,
                                               `insurance_pri_payor`,
                                               `insurance_pri_policy_x0023_`,
                                               `insurance_pri_policy_verified`,
                                               `insurance_pri_pay_pct`,
                                               `insurance_sec_payor`,
                                               `insurance_sec_policy_x0023_`,
                                               `insurance_sec_policy_verified`,
                                               `insurance_sec_payPct`,
                                               `insurance_ter_payor`,
                                               `insurance_ter_policy_x0023_`,
                                               `insurance_insurance_verified` )
                                        VALUES (
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s", "%s", "%s", "%s", "%s",
                                                "%s", "%s"
                                               )
    """ % (
                              get_col_val(rec, 'so_number'),
                              get_col_val(rec, 'insurance_pri_payor'),
                              get_col_val(rec, 'insurance_pri_policy_x0023_'),
                              get_col_val(rec, 'insurance_pri_policy_verified'),
                              get_col_val(rec, 'insurance_pri_pay_pct'),
                              get_col_val(rec, 'insurance_sec_payor'),
                              get_col_val(rec, 'insurance_sec_policy_x0023_'),
                              get_col_val(rec, 'insurance_sec_policy_verified'),
                              get_col_val(rec, 'insurance_sec_payPct'),
                              get_col_val(rec, 'insurance_ter_payor'),
                              get_col_val(rec, 'insurance_ter_policy_x0023_'),
                              get_col_val(rec, 'insurance_insurance_verified')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql_soc)
        r = cursor.execute(sql_dlvry)
        r = cursor.execute(sql_patient)
        r = cursor.execute(sql_odoc)
        r = cursor.execute(sql_dgns)
        r = cursor.execute(sql_rfrl)
        r = cursor.execute(sql_insrnc)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with SO #.' + str(get_col_val(rec, 'so_number')) )
        print (e)

        # Rollback in case there is any error
        db.rollback()


def insert_data_socitems(rec):
    """"""
    #print ("soc_items: inserting data for SO #." +  str(get_col_val(rec, 'sales_order_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `soc_items` (
                                               `sales_order_number`,
                                               `sales_order_detail_item_id`,
                                               `sales_order_detail_item_name`,
                                               `sales_order_detail_item_description`,
                                               `sales_order_detail_stocking_uom`,
                                               `sales_order_detail_original_dos`,
                                               `sales_order_detail_special_pricing`,
                                               `sales_order_detail_price_override`,
                                               `sales_order_detail_qty`,
                                               `sales_order_detail_bqty`,
                                               `sales_order_detail_proc_code`,
                                               `sales_order_detail_price_option`,
                                               `sales_order_detail_modifier1`,
                                               `sales_order_detail_modifier2`,
                                               `sales_order_detail_modifier3`,
                                               `sales_order_detail_modifier4`,
                                               `sales_order_detail_charge`,
                                               `sales_order_detail_allow`,
                                               `sales_order_detail_taxable`,
                                               `sales_order_detail_non_tax_reason`,
                                               `sales_order_detail_sale_type`,
                                               `sales_order_detail_item_group`,
                                               `sales_order_detail_item_user1`,
                                               `sales_order_detail_manual_convert_to_purchase_mctp`,
                                               `sales_order_detail_mctp_charge`,
                                               `sales_order_detail_mctp_allow`,
                                               `sales_order_detail_mctp_modifier1`,
                                               `sales_order_detail_mctp_modifier2`,
                                               `sales_order_detail_mctp_modifier3`,
                                               `sales_order_detail_mctp_modifier4`,
                                               `sales_order_detail_mctp_period`,
                                               `sales_order_detail_addtl_modifier1`,
                                               `sales_order_detail_addtl_modifier2`,
                                               `sales_order_detail_addtl_modifier3`,
                                               `sales_order_detail_addtl_modifier4`,
                                               `sales_order_detail_price_table`,
                                               `sales_order_detail_price_option_name`,
                                               `sales_order_detail_extended_charge_amount`,
                                               `sales_order_detail_extended_allowance_amount`,
                                               `sales_order_detail_cb_pricing`,
                                               `sales_order_detail_cb_price_table_override`,
                                               `sales_order_detail_cb_override`,
                                               `sales_order_detail_messages`,
                                               `sales_order_detail_default_vendor`,
                                               `sales_order_detail_calories_per_day`,
                                               `sales_order_detail_location`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s" 
                                       )
    """ % (
                              get_col_val(rec, 'sales_order_number'),
                              get_col_val(rec, 'sales_order_detail_item_id'),
                              get_col_val(rec, 'sales_order_detail_item_name'),
                              get_col_val(rec, 'sales_order_detail_item_description'),
                              get_col_val(rec, 'sales_order_detail_stocking_uom'),
                              get_col_val(rec, 'sales_order_detail_original_dos'),
                              get_col_val(rec, 'sales_order_detail_special_pricing'),
                              get_col_val(rec, 'sales_order_detail_price_override'),
                              get_col_val(rec, 'sales_order_detail_qty'),
                              get_col_val(rec, 'sales_order_detail_bqty'),
                              get_col_val(rec, 'sales_order_detail_proc_code'),
                              get_col_val(rec, 'sales_order_detail_price_option'),
                              get_col_val(rec, 'sales_order_detail_modifier1'),
                              get_col_val(rec, 'sales_order_detail_modifier2'),
                              get_col_val(rec, 'sales_order_detail_modifier3'),
                              get_col_val(rec, 'sales_order_detail_modifier4'),
                              get_col_val(rec, 'sales_order_detail_charge'),
                              get_col_val(rec, 'sales_order_detail_allow'),
                              get_col_val(rec, 'sales_order_detail_taxable'),
                              get_col_val(rec, 'sales_order_detail_non_tax_reason'),
                              get_col_val(rec, 'sales_order_detail_sale_type'),
                              get_col_val(rec, 'sales_order_detail_item_group'),
                              get_col_val(rec, 'sales_order_detail_item_user1'),
                              get_col_val(rec, 'sales_order_detail_manual_convert_to_purchase_mctp'),
                              get_col_val(rec, 'sales_order_detail_mctp_charge'),
                              get_col_val(rec, 'sales_order_detail_mctp_allow'),
                              get_col_val(rec, 'sales_order_detail_mctp_modifier1'),
                              get_col_val(rec, 'sales_order_detail_mctp_modifier2'),
                              get_col_val(rec, 'sales_order_detail_mctp_modifier3'),
                              get_col_val(rec, 'sales_order_detail_mctp_modifier4'),
                              get_col_val(rec, 'sales_order_detail_mctp_period'),
                              get_col_val(rec, 'sales_order_detail_addtl_modifier1'),
                              get_col_val(rec, 'sales_order_detail_addtl_modifier2'),
                              get_col_val(rec, 'sales_order_detail_addtl_modifier3'),
                              get_col_val(rec, 'sales_order_detail_addtl_modifier4'),
                              get_col_val(rec, 'sales_order_detail_price_table'),
                              get_col_val(rec, 'sales_order_detail_price_option_name'),
                              get_col_val(rec, 'sales_order_detail_extended_charge_amount'),
                              get_col_val(rec, 'sales_order_detail_extended_allowance_amount'),
                              get_col_val(rec, 'sales_order_detail_cb_pricing'),
                              get_col_val(rec, 'sales_order_detail_cb_price_table_override'),
                              get_col_val(rec, 'sales_order_detail_cb_override'),
                              get_col_val(rec, 'sales_order_detail_messages'),
                              get_col_val(rec, 'sales_order_detail_default_vendor'),
                              get_col_val(rec, 'sales_order_detail_calories_per_day'),
                              get_col_val(rec, 'sales_order_detail_location')
    )


    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with SO #.' + str(get_col_val(rec, 'sales_order_number')) )
        print (sql)
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_sovoid(rec):
    """"""
    #print ("so_void: inserting data for SO #." +  str(get_col_val(rec, 'sales_order_void_voided_sales_order_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `so_void` (
                                               `sales_order_void_voided_sales_order_number`,
                                               `sales_order_void_void_reason`,
                                               `sales_order_void_voided_by`,
                                               `sales_order_void_voided_date`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s"
                              )
    """ % (
                              get_col_val(rec, 'sales_order_void_voided_sales_order_number'),
                              get_col_val(rec, 'sales_order_void_void_reason'),
                              get_col_val(rec, 'sales_order_void_voided_by'),
                              get_col_val(rec, 'sales_order_void_voided_date')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with SO #.' + str(get_col_val(rec, 'sales_order_void_voided_sales_order_number')) )
        print (sql)
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_rcmclosed(rec):
    """"""
    #print ("rcm_closed: inserting data for activity task " +  str(get_col_val(rec, 'activity_task_id')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `rcm_closed` (
                                               `activity_task_id`,
                                               `activity_type`,
                                               `activity`,
                                               `priority`,
                                               `assigned_to`,
                                               `amount`,
                                               `task_status`,
                                               `create_date`,
                                               `closed_date`,
                                               `patient_name`,
                                               `patient_id`,
                                               `patient_branch`,
                                               `insurance_id`,
                                               `insurance_name`,
                                               `note`,
                                               `work_item_name`,
                                               `work_item_id`,
                                               `work_item_branch`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"
                                       )
    """ % (
                              get_col_val(rec, 'activity_task_id'),
                              get_col_val(rec, 'activity_type'),
                              get_col_val(rec, 'activity'),
                              get_col_val(rec, 'priority'),
                              get_col_val(rec, 'assigned_to'),
                              get_col_val(rec, 'amount'),
                              get_col_val(rec, 'task_status'),
                              get_col_val(rec, 'create_date'),
                              get_col_val(rec, 'closed_date'),
                              get_col_val(rec, 'patient_name'),
                              get_col_val(rec, 'patient_id'),
                              get_col_val(rec, 'patient_branch'),
                              get_col_val(rec, 'insurance_id'),
                              get_col_val(rec, 'insurance_name'),
                              get_col_val(rec, 'note'),
                              get_col_val(rec, 'work_item_name'),
                              get_col_val(rec, 'work_item_id'),
                              get_col_val(rec, 'work_item_branch')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with activity task ' + str(get_col_val(rec, 'activity_task_id')) )
        print (sql)
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_parscreated(rec):
    """"""
    #print ("pars_created: inserting data for PAR #." +  str(get_col_val(rec, 'par_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `pars_created` (
                                               `par_number`,
                                               `par_descr`,
                                               `par_exclude_from_par_report`,
                                               `par_exclude_from_claim`,
                                               `par_status`,
                                               `par_create_date`,
                                               `par_created_by`,
                                               `par_logged_by`,
                                               `par_insurance`,
                                               `par_branch`,
                                               `par_printed_by`,
                                               `par_faxed_by`,
                                               `par_purchase_quantity_limits_proc_code`,
                                               `par_purchase_quantity_limits_approved_qty`,
                                               `par_purchase_quantity_limits_returned_qty`,
                                               `par_purchase_quantity_limits_used_qty`,
                                               `par_purchase_quantity_limits_adjusted_qty`,
                                               `sales_order_number`,
                                               `patient_id`,
                                               `patient_key`,
                                               `insurance_pri_payor`,
                                               `insurance_pri_payor_id`,
                                               `insurance_pri_policy_x0023`,
                                               `cmncmn_form`,
                                               `cmncmn_exp`,
                                               `cmncmn_init`,
                                               `cmncmn_status`,
                                               `cmncmn_log_date`,
                                               `cmncmn_lengthof_need`,
                                               `cmn_excludefrom_cmn_report`,
                                               `cmncmn_faxed_by`,
                                               `cmncmn_placeholder`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s"
                                        )
    """ % (
                              get_col_val(rec, 'par_number'),
                              get_col_val(rec, 'par_descr'),
                              get_col_val(rec, 'par_exclude_from_par_report'),
                              get_col_val(rec, 'par_exclude_from_claim'),
                              get_col_val(rec, 'par_status'),
                              get_col_val(rec, 'par_create_date'),
                              get_col_val(rec, 'par_created_by'),
                              get_col_val(rec, 'par_logged_by'),
                              get_col_val(rec, 'par_insurance'),
                              get_col_val(rec, 'par_branch'),
                              get_col_val(rec, 'par_printed_by'),
                              get_col_val(rec, 'par_faxed_by'),
                              get_col_val(rec, 'par_purchase_quantity_limits_proc_code'),
                              get_col_val(rec, 'par_purchase_quantity_limits_approved_qty'),
                              get_col_val(rec, 'par_purchase_quantity_limits_returned_qty'),
                              get_col_val(rec, 'par_purchase_quantity_limits_used_qty'),
                              get_col_val(rec, 'par_purchase_quantity_limits_adjusted_qty'),
                              get_col_val(rec, 'sales_order_number'),
                              get_col_val(rec, 'patient_id'),
                              get_col_val(rec, 'patient_key'),
                              get_col_val(rec, 'insurance_pri_payor'),
                              get_col_val(rec, 'insurance_pri_payor_id'),
                              get_col_val(rec, 'insurance_pri_policy_x0023'),
                              get_col_val(rec, 'cmncmn_form'),
                              get_col_val(rec, 'cmncmn_exp'),
                              get_col_val(rec, 'cmncmn_init'),
                              get_col_val(rec, 'cmncmn_status'),
                              get_col_val(rec, 'cmncmn_log_date'),
                              get_col_val(rec, 'cmncmn_lengthof_need'),
                              get_col_val(rec, 'cmn_excludefrom_cmn_report'),
                              get_col_val(rec, 'cmncmn_faxed_by'),
                              get_col_val(rec, 'cmncmn_placeholder')
    )


    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with PAR #.' + str(get_col_val(rec, 'par_number')) )
        print (sql)
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_parslogged(rec):
    """"""
    #print ("pars_logged: inserting data for PAR #." +  str(get_col_val(rec, 'par_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `pars_logged` (
                                               `par_number`,
                                               `par_descr`,
                                               `par_init`,
                                               `par_exclude_from_par_report`,
                                               `par_exclude_from_claim`,
                                               `par_status`,
                                               `par_create_date`,
                                               `par_created_by`,
                                               `par_logged_date`,
                                               `par_logged_by`,
                                               `par_insurance`,
                                               `par_branch`,
                                               `par_printed_by`,
                                               `par_faxed_by`,
                                               `par_purchase_quantity_limits_proc_code`,
                                               `par_purchase_quantity_limits_approved_qty`,
                                               `par_purchase_quantity_limits_returned_qty`,
                                               `par_purchase_quantity_limits_used_qty`,
                                               `par_purchase_quantity_limits_adjusted_qty`,
                                               `sales_order_number`,
                                               `patient_id`,
                                               `patient_key`,
                                               `insurance_pri_payor`,
                                               `insurance_pri_payor_id`,
                                               `insurance_pri_policy_x0023`,
                                               `cmncmn_form`,
                                               `cmncmn_exp`,
                                               `cmncmn_init`,
                                               `cmncmn_status`,
                                               `cmncmn_log_date`,
                                               `cmncmn_lengthof_need`,
                                               `cmn_excludefrom_cmn_report`,
                                               `cmncmn_faxed_by`,
                                               `cmncmn_placeholder`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s"
                                       )
    """ % (
                              get_col_val(rec, 'par_number'),
                              get_col_val(rec, 'par_descr'),
                              get_col_val(rec, 'par_init'),
                              get_col_val(rec, 'par_exclude_from_par_report'),
                              get_col_val(rec, 'par_exclude_from_claim'),
                              get_col_val(rec, 'par_status'),
                              get_col_val(rec, 'par_create_date'),
                              get_col_val(rec, 'par_created_by'),
                              get_col_val(rec, 'par_logged_date'),
                              get_col_val(rec, 'par_logged_by'),
                              get_col_val(rec, 'par_insurance'),
                              get_col_val(rec, 'par_branch'),
                              get_col_val(rec, 'par_printed_by'),
                              get_col_val(rec, 'par_faxed_by'),
                              get_col_val(rec, 'par_purchase_quantity_limits_proc_code'),
                              get_col_val(rec, 'par_purchase_quantity_limits_approved_qty'),
                              get_col_val(rec, 'par_purchase_quantity_limits_returned_qty'),
                              get_col_val(rec, 'par_purchase_quantity_limits_used_qty'),
                              get_col_val(rec, 'par_purchase_quantity_limits_adjusted_qty'),
                              get_col_val(rec, 'sales_order_number'),
                              get_col_val(rec, 'patient_id'),
                              get_col_val(rec, 'patient_key'),
                              get_col_val(rec, 'insurance_pri_payor'),
                              get_col_val(rec, 'insurance_pri_payor_id'),
                              get_col_val(rec, 'insurance_pri_policy_x0023'),
                              get_col_val(rec, 'cmncmn_form'),
                              get_col_val(rec, 'cmncmn_exp'),
                              get_col_val(rec, 'cmncmn_init'),
                              get_col_val(rec, 'cmncmn_status'),
                              get_col_val(rec, 'cmncmn_log_date'),
                              get_col_val(rec, 'cmncmn_lengthof_need'),
                              get_col_val(rec, 'cmn_excludefrom_cmn_report'),
                              get_col_val(rec, 'cmncmn_faxed_by'),
                              get_col_val(rec, 'cmncmn_placeholder')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with PAR #.' + str(get_col_val(rec, 'par_number')) )
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_payments(rec):
    """"""
    #print ("payments: inserting data for Payment " +  str(get_col_val(rec, 'payment_id')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `payments` (
                                               `payment_id`,
                                               `payment_check_x002_f_reference`,
                                               `payment_type`,
                                               `payment_created_by`,
                                               `payment_create_date`,
                                               `payment_date`,
                                               `payment_post_date`,
                                               `payment_posted_by`,
                                               `payment_description`,
                                               `payment_amount`,
                                               `payment_gl_period`,
                                               `payment_gl_year`,
                                               `payment_gl_start_date`,
                                               `payment_gl_end_date`,
                                               `receipt_type`,
                                               `receipt_check_x002_f_reference`,
                                               `receipt_note`,
                                               `deposit_created_by`,
                                               `deposit_posted_by`,
                                               `deposit_reference`,
                                               `deposit_description`,
                                               `invoice_number`,
                                               `invoice_status`,
                                               `invoice_sales_order_number`,
                                               `invoice_date_created`,
                                               `invoice_dateof_service`,
                                               `invoice_holdfromprinting_x002_f_submission`,
                                               `invoice_reprint_x002_f_re_submit_claim`,
                                               `invoice_branch`,
                                               `invoice_note`,
                                               `invoice_so_created_by`,
                                               `invoice_so_confirmed_by`,
                                               `invoice_balances_charge_total`,
                                               `invoice_balances_allow_total`,
                                               `invoice_balances_tax_total`,
                                               `invoice_balances_adjustments`,
                                               `invoice_balances_payments`,
                                               `invoice_balances_balance`,
                                               `invoice_biller_x002_f_collector`,
                                               `invoice_last_date_worked`,
                                               `invoice_follow_up_date`,
                                               `invoice_collection_type`,
                                               `invoice_collect_action_x002_f_status`,
                                               `invoice_pro_med_status_code`,
                                               `invoice_pro_med_status_code_date`,
                                               `invoice_appeals_due_date`,
                                               `sales_order_so_number`,
                                               `patient_id`,
                                               `policy_payor_name`,
                                               `policy_payor_id`,
                                               `policy_x0023`,
                                               `policy_pay`,
                                               `invoice_detail_id`,
                                               `invoice_detail_item_id`,
                                               `marketing_rep_last_name`,
                                               `marketing_rep_first_name`,
                                               `related_invoice_primary_invoice_nbr`,
                                               `related_invoice_secondary_invoice_nbr`,
                                               `related_invoice_tertiary_invoice_nbr`,
                                               `related_invoice_patient_invoice_nbr`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"
                                       )
    """ % (
                              get_col_val(rec, 'payment_id'),
                              get_col_val(rec, 'payment_check_x002_f_reference'),
                              get_col_val(rec, 'payment_type'),
                              get_col_val(rec, 'payment_created_by'),
                              get_col_val(rec, 'payment_create_date'),
                              get_col_val(rec, 'payment_date'),
                              get_col_val(rec, 'payment_post_date'),
                              get_col_val(rec, 'payment_posted_by'),
                              get_col_val(rec, 'payment_description'),
                              get_col_val(rec, 'payment_amount'),
                              get_col_val(rec, 'payment_gl_period'),
                              get_col_val(rec, 'payment_gl_year'),
                              get_col_val(rec, 'payment_gl_start_date'),
                              get_col_val(rec, 'payment_gl_end_date'),
                              get_col_val(rec, 'receipt_type'),
                              get_col_val(rec, 'receipt_check_x002_f_reference'),
                              get_col_val(rec, 'receipt_note'),
                              get_col_val(rec, 'deposit_created_by'),
                              get_col_val(rec, 'deposit_posted_by'),
                              get_col_val(rec, 'deposit_reference'),
                              get_col_val(rec, 'deposit_description'),
                              get_col_val(rec, 'invoice_number'),
                              get_col_val(rec, 'invoice_status'),
                              get_col_val(rec, 'invoice_sales_order_number'),
                              get_col_val(rec, 'invoice_date_created'),
                              get_col_val(rec, 'invoice_dateof_service'),
                              get_col_val(rec, 'invoice_holdfromprinting_x002_f_submission'),
                              get_col_val(rec, 'invoice_reprint_x002_f_re_submit_claim'),
                              get_col_val(rec, 'invoice_branch'),
                              get_col_val(rec, 'invoice_note'),
                              get_col_val(rec, 'invoice_so_created_by'),
                              get_col_val(rec, 'invoice_so_confirmed_by'),
                              get_col_val(rec, 'invoice_balances_charge_total'),
                              get_col_val(rec, 'invoice_balances_allow_total'),
                              get_col_val(rec, 'invoice_balances_tax_total'),
                              get_col_val(rec, 'invoice_balances_adjustments'),
                              get_col_val(rec, 'invoice_balances_payments'),
                              get_col_val(rec, 'invoice_balances_balance'),
                              get_col_val(rec, 'invoice_biller_x002_f_collector'),
                              get_col_val(rec, 'invoice_last_date_worked'),
                              get_col_val(rec, 'invoice_follow_up_date'),
                              get_col_val(rec, 'invoice_collection_type'),
                              get_col_val(rec, 'invoice_collect_action_x002_f_status'),
                              get_col_val(rec, 'invoice_pro_med_status_code'),
                              get_col_val(rec, 'invoice_pro_med_status_code_date'),
                              get_col_val(rec, 'invoice_appeals_due_date'),
                              get_col_val(rec, 'sales_order_so_number'),
                              get_col_val(rec, 'patient_id'),
                              get_col_val(rec, 'policy_payor_name'),
                              get_col_val(rec, 'policy_payor_id'),
                              get_col_val(rec, 'policy_x0023'),
                              get_col_val(rec, 'policy_pay'),
                              get_col_val(rec, 'invoice_detail_id'),
                              get_col_val(rec, 'invoice_detail_item_id'),
                              get_col_val(rec, 'marketing_rep_last_name'),
                              get_col_val(rec, 'marketing_rep_first_name'),
                              get_col_val(rec, 'related_invoice_primary_invoice_nbr'),
                              get_col_val(rec, 'related_invoice_secondary_invoice_nbr'),
                              get_col_val(rec, 'related_invoice_tertiary_invoice_nbr'),
                              get_col_val(rec, 'related_invoice_patient_invoice_nbr')
    )
    
    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with Payment ' + str(get_col_val(rec, 'payment_id')) )
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_invoicescreated(rec):
    """"""
    #print ("invoices_created: inserting data for Invoice #." +  str(get_col_val(rec, 'invoice_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `invoices_created` (
                                               `invoice_number`,
                                               `invoice_status`,
                                               `invoice_sales_order_number`,
                                               `invoice_date_created`,
                                               `invoice_dateof_service`,
                                               `invoice_holdfromprinting_x002_f_submission`,
                                               `invoice_medicare_deductible_hold`,
                                               `invoice_reprint_x002_f_re_submit_claim`,
                                               `invoice_span_date_hold`,
                                               `invoice_branch`,
                                               `invoice_so_reference`,
                                               `invoice_branch_group`,
                                               `invoice_box19`,
                                               `invoice_so_place_of_service`,
                                               `invoice_so_classification`,
                                               `invoice_so_note`,
                                               `invoice_so_manual_hold_reason`,
                                               `invoice_so_created_by`,
                                               `invoice_so_confirmed_by`,
                                               `invoice_submission_type`,
                                               `invoice_key`,
                                               `invoice_balances_charge_total`,
                                               `invoice_balances_allow_total`,
                                               `invoice_balances_tax_total`,
                                               `invoice_balances_adjustments`,
                                               `invoice_balances_payments`,
                                               `invoice_balances_balance`,
                                               `patient_id`,
                                               `policy_payor_name`,
                                               `policy_payor_id`,
                                               `policy_x0023`,
                                               `policy_group_x0023`,
                                               `policy_pay`,
                                               `policy_claim_form`,
                                               `policy_payor_level`,
                                               `policy_plan_type`,
                                               `policy_do_not_print_secondary_claims`,
                                               `invoice_detail_item_id`,
                                               `invoice_detail_item_name`,
                                               `invoice_detail_dos_from`,
                                               `invoice_detail_dos_to`,
                                               `invoice_detail_billing_period`,
                                               `invoice_detail_reprint_x002_f_resubmit_item`,
                                               `invoice_detail_charge`,
                                               `invoice_detail_allow`,
                                               `invoice_detail_tax`,
                                               `invoice_detail_payments`,
                                               `invoice_detail_balance`,
                                               `invoice_detail_qty`,
                                               `invoice_detail_inventory_qty`,
                                               `invoice_detail_proc_code`,
                                               `invoice_detail_modifier1`,
                                               `invoice_detail_modifier2`,
                                               `invoice_detail_modifier3`,
                                               `invoice_detail_modifier4`,
                                               `invoice_detail_abn_proc_code`,
                                               `invoice_detail_price_type`,
                                               `invoice_detail_so_item_note`,
                                               `invoice_detail_par_number`,
                                               `marketing_rep_full_name`,
                                               `ordering_doctor_key`,
                                               `ordering_doctor_npi`,
                                               `serial_numbers_serial_number`,
                                               `sales_order_hold_cmn_not_logged`,
                                               `sales_order_hold_cmn_expired`,
                                               `sales_order_hold_par_not_logged`,
                                               `sales_order_hold_par_expired`,
                                               `sales_order_hold_manual_hold`,
                                               `sales_order_stop_pending_pickup`,
                                               `sales_order_stop_multiple_pricing_options`,
                                               `sales_order_stop_policy_expired`,
                                               `sales_order_stop_no_pricing_found`,
                                               `sales_order_stop_policy_changed`,
                                               `sales_order_stop_manual_stop_date`,
                                               `work_in_progress_wip_state`,
                                               `work_in_progress_assigned_to`,
                                               `work_in_progress_completed`,
                                               `work_in_progress_wip_days_in_state`,
                                               `primary_invoice_primary_invoice_number`,
                                               `primary_invoice_primary_insurance_name`,
                                               `secondary_invoice_secondary_invoice_number`,
                                               `secondary_invoice_secondary_insurance_name`,
                                               `tertiary_invoice_tertiary_invoice_number`,
                                               `tertiary_invoice_tertiary_insurance_name`,
                                               `patient_invoice_patient_invoice_number`,
                                               `patient_invoice_patient_insurance_name`,
                                               `responsible_party_relationship`,
                                               `responsible_party_phone`,
                                               `responsible_party_email_address`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"
                                       )
    """ % (
                              get_col_val(rec, 'invoice_number'),
                              get_col_val(rec, 'invoice_status'),
                              get_col_val(rec, 'invoice_sales_order_number'),
                              get_col_val(rec, 'invoice_date_created'),
                              get_col_val(rec, 'invoice_dateof_service'),
                              get_col_val(rec, 'invoice_holdfromprinting_x002_f_submission'),
                              get_col_val(rec, 'invoice_medicare_deductible_hold'),
                              get_col_val(rec, 'invoice_reprint_x002_f_re_submit_claim'),
                              get_col_val(rec, 'invoice_span_date_hold'),
                              get_col_val(rec, 'invoice_branch'),
                              get_col_val(rec, 'invoice_so_reference'),
                              get_col_val(rec, 'invoice_branch_group'),
                              get_col_val(rec, 'invoice_box19'),
                              get_col_val(rec, 'invoice_so_place_of_service'),
                              get_col_val(rec, 'invoice_so_classification'),
                              get_col_val(rec, 'invoice_so_note'),
                              get_col_val(rec, 'invoice_so_manual_hold_reason'),
                              get_col_val(rec, 'invoice_so_created_by'),
                              get_col_val(rec, 'invoice_so_confirmed_by'),
                              get_col_val(rec, 'invoice_submission_type'),
                              get_col_val(rec, 'invoice_key'),
                              get_col_val(rec, 'invoice_balances_charge_total'),
                              get_col_val(rec, 'invoice_balances_allow_total'),
                              get_col_val(rec, 'invoice_balances_tax_total'),
                              get_col_val(rec, 'invoice_balances_adjustments'),
                              get_col_val(rec, 'invoice_balances_payments'),
                              get_col_val(rec, 'invoice_balances_balance'),
                              get_col_val(rec, 'patient_id'),
                              get_col_val(rec, 'policy_payor_name'),
                              get_col_val(rec, 'policy_payor_id'),
                              get_col_val(rec, 'policy_x0023'),
                              get_col_val(rec, 'policy_group_x0023'),
                              get_col_val(rec, 'policy_pay'),
                              get_col_val(rec, 'policy_claim_form'),
                              get_col_val(rec, 'policy_payor_level'),
                              get_col_val(rec, 'policy_plan_type'),
                              get_col_val(rec, 'policy_do_not_print_secondary_claims'),
                              get_col_val(rec, 'invoice_detail_item_id'),
                              get_col_val(rec, 'invoice_detail_item_name'),
                              get_col_val(rec, 'invoice_detail_dos_from'),
                              get_col_val(rec, 'invoice_detail_dos_to'),
                              get_col_val(rec, 'invoice_detail_billing_period'),
                              get_col_val(rec, 'invoice_detail_reprint_x002_f_resubmit_item'),
                              get_col_val(rec, 'invoice_detail_charge'),
                              get_col_val(rec, 'invoice_detail_allow'),
                              get_col_val(rec, 'invoice_detail_tax'),
                              get_col_val(rec, 'invoice_detail_payments'),
                              get_col_val(rec, 'invoice_detail_balance'),
                              get_col_val(rec, 'invoice_detail_qty'),
                              get_col_val(rec, 'invoice_detail_inventory_qty'),
                              get_col_val(rec, 'invoice_detail_proc_code'),
                              get_col_val(rec, 'invoice_detail_modifier1'),
                              get_col_val(rec, 'invoice_detail_modifier2'),
                              get_col_val(rec, 'invoice_detail_modifier3'),
                              get_col_val(rec, 'invoice_detail_modifier4'),
                              get_col_val(rec, 'invoice_detail_abn_proc_code'),
                              get_col_val(rec, 'invoice_detail_price_type'),
                              get_col_val(rec, 'invoice_detail_so_item_note'),
                              get_col_val(rec, 'invoice_detail_par_number'),
                              get_col_val(rec, 'marketing_rep_full_name'),
                              get_col_val(rec, 'ordering_doctor_key'),
                              get_col_val(rec, 'ordering_doctor_npi'),
                              get_col_val(rec, 'serial_numbers_serial_number'),
                              get_col_val(rec, 'sales_order_hold_cmn_not_logged'),
                              get_col_val(rec, 'sales_order_hold_cmn_expired'),
                              get_col_val(rec, 'sales_order_hold_par_not_logged'),
                              get_col_val(rec, 'sales_order_hold_par_expired'),
                              get_col_val(rec, 'sales_order_hold_manual_hold'),
                              get_col_val(rec, 'sales_order_stop_pending_pickup'),
                              get_col_val(rec, 'sales_order_stop_multiple_pricing_options'),
                              get_col_val(rec, 'sales_order_stop_policy_expired'),
                              get_col_val(rec, 'sales_order_stop_no_pricing_found'),
                              get_col_val(rec, 'sales_order_stop_policy_changed'),
                              get_col_val(rec, 'sales_order_stop_manual_stop_date'),
                              get_col_val(rec, 'work_in_progress_wip_state'),
                              get_col_val(rec, 'work_in_progress_assigned_to'),
                              get_col_val(rec, 'work_in_progress_completed'),
                              get_col_val(rec, 'work_in_progress_wip_days_in_state'),
                              get_col_val(rec, 'primary_invoice_primary_invoice_number'),
                              get_col_val(rec, 'primary_invoice_primary_insurance_name'),
                              get_col_val(rec, 'secondary_invoice_secondary_invoice_number'),
                              get_col_val(rec, 'secondary_invoice_secondary_insurance_name'),
                              get_col_val(rec, 'tertiary_invoice_tertiary_invoice_number'),
                              get_col_val(rec, 'tertiary_invoice_tertiary_insurance_name'),
                              get_col_val(rec, 'patient_invoice_patient_invoice_number'),
                              get_col_val(rec, 'patient_invoice_patient_insurance_name'),
                              get_col_val(rec, 'responsible_party_relationship'),
                              get_col_val(rec, 'responsible_party_phone'),
                              get_col_val(rec, 'responsible_party_email_address')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with Invoice #.' + str(get_col_val(rec, 'invoice_number')) )
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_invoicesstatus(rec):
    """"""
    #print ("invoices_status: inserting data for Invoice #." +  str(get_col_val(rec, 'invoice_number')))
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME, use_unicode=True, charset="utf8")

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `InvoicesStatus` (
                                               `invoice_number`,
                                               `invoice_status`,
                                               `invoice_sales_order_number`,
                                               `invoice_holdfromprinting_x002_f_submission`,
                                               `invoice_medicare_deductible_hold`,
                                               `invoice_user_manual_hold`,
                                               `invoice_holdfrom_billing_statement`,
                                               `invoice_so_manual_hold_reason`,
                                               `invoice_biller_x002_f_collector`,
                                               `invoice_last_date_worked`,
                                               `invoice_follow_up_date`,
                                               `invoice_collection_type`,
                                               `invoice_collect_action_x002_f_status`,
                                               `invoice_pro_med_status_code`,
                                               `invoice_pro_med_status_code_date`,
                                               `invoice_appeals_due_date`,
                                               `balances_charge_total`,
                                               `balances_allow_total`,
                                               `balances_tax_total`,
                                               `balances_adjustments`,
                                               `balances_balance`,
                                               `balances_payments`,
                                               `sales_order_hold_cmn_not_logged`,
                                               `sales_order_hold_cmn_expired`,
                                               `sales_order_hold_par_not_logged`,
                                               `sales_order_hold_par_expired`,
                                               `sales_order_hold_manual_hold`,
                                               `sales_order_stop_pending_pickup`,
                                               `sales_order_stop_multiple_pricing_options`,
                                               `sales_order_stop_policy_expired`,
                                               `sales_order_stop_no_pricing_found`,
                                               `sales_order_stop_policy_changed`,
                                               `sales_order_stop_manual_stop_date`,
                                               `sales_order_stop_automatic_eligibility_check`,
                                               `sales_order_stop_ineligible_policy`,
                                               `work_in_progress_wip_state`,
                                               `work_in_progress_assigned_to`,
                                               `work_in_progress_completed`,
                                               `work_in_progress_wip_days_in_state`
                              ) VALUES (
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", 
                                               "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s"
                                       )
    """ % (
                              get_col_val(rec, 'invoice_number'),
                              get_col_val(rec, 'invoice_status'),
                              get_col_val(rec, 'invoice_sales_order_number'),
                              get_col_val(rec, 'invoice_holdfromprinting_x002_f_submission'),
                              get_col_val(rec, 'invoice_medicare_deductible_hold'),
                              get_col_val(rec, 'invoice_user_manual_hold'),
                              get_col_val(rec, 'invoice_holdfrom_billing_statement'),
                              get_col_val(rec, 'invoice_so_manual_hold_reason'),
                              get_col_val(rec, 'invoice_biller_x002_f_collector'),
                              get_col_val(rec, 'invoice_last_date_worked'),
                              get_col_val(rec, 'invoice_follow_up_date'),
                              get_col_val(rec, 'invoice_collection_type'),
                              get_col_val(rec, 'invoice_collect_action_x002_f_status'),
                              get_col_val(rec, 'invoice_pro_med_status_code'),
                              get_col_val(rec, 'invoice_pro_med_status_code_date'),
                              get_col_val(rec, 'invoice_appeals_due_date'),
                              get_col_val(rec, 'balances_charge_total'),
                              get_col_val(rec, 'balances_allow_total'),
                              get_col_val(rec, 'balances_tax_total'),
                              get_col_val(rec, 'balances_adjustments'),
                              get_col_val(rec, 'balances_balance'),
                              get_col_val(rec, 'balances_payments'),
                              get_col_val(rec, 'sales_order_hold_cmn_not_logged'),
                              get_col_val(rec, 'sales_order_hold_cmn_expired'),
                              get_col_val(rec, 'sales_order_hold_par_not_logged'),
                              get_col_val(rec, 'sales_order_hold_par_expired'),
                              get_col_val(rec, 'sales_order_hold_manual_hold'),
                              get_col_val(rec, 'sales_order_stop_pending_pickup'),
                              get_col_val(rec, 'sales_order_stop_multiple_pricing_options'),
                              get_col_val(rec, 'sales_order_stop_policy_expired'),
                              get_col_val(rec, 'sales_order_stop_no_pricing_found'),
                              get_col_val(rec, 'sales_order_stop_policy_changed'),
                              get_col_val(rec, 'sales_order_stop_manual_stop_date'),
                              get_col_val(rec, 'sales_order_stop_automatic_eligibility_check'),
                              get_col_val(rec, 'sales_order_stop_ineligible_policy'),
                              get_col_val(rec, 'work_in_progress_wip_state'),
                              get_col_val(rec, 'work_in_progress_assigned_to'),
                              get_col_val(rec, 'work_in_progress_completed'),
                              get_col_val(rec, 'work_in_progress_wip_days_in_state')
    )

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        #print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error) as e:
        print ('Error inserting record with Invoice #.' + str(get_col_val(rec, 'invoice_number')) )
        print (e) 

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()

