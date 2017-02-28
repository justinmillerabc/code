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
         }


def get_col_val(rec, key):
    """"""
    if SO_MAP[key] in rec.keys() and type(rec[SO_MAP[key]]) in [type(''), type(u'')]:
       val = rec[SO_MAP[key]]
       if val == 'false': 
          val = 0
       elif val == 'true':
          val = 1
    else:
       val = ''
    val = val.replace('"', '&quote;')
    return val


def insert_data_so(rec):
    """"""
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = """INSERT INTO `sales_order` (`so_number`,
                                        `so_date_created`,
                                        `so_created_by`,
                                        `so_branch_office`,
                                        `so_status`,
                                        `so_location`,
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
                                VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",
                                        "%s", "%s", "%s", "%s", "%s", "%s", "%s"  ) 
    """ % (

                       get_col_val(rec, 'so_number'),
                       get_col_val(rec, 'so_date_created'),
                       get_col_val(rec, 'so_created_by'),
                       get_col_val(rec, 'so_branch_office'),
                       get_col_val(rec, 'so_status'),
                       get_col_val(rec, 'so_location'),
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
        print (e) 
        print (sql)

        # Rollback in case there is any error
        db.rollback()

    # disconnect from the DB server
    db.close()


def insert_data_soc(rec):
    """"""
    # Open database connection
    db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)

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

    
#    print (sql_soc)
#    print (sql_dlvry)
#    print (sql_patient)
#    print (sql_odoc)
#    print (sql_dgns)
#    print (sql_rfrl)
#    print (sql_insrnc)

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
        print (e)
        print (sql_soc)

        # Rollback in case there is any error
        db.rollback()
