import csv
import time 
import MySQLdb
import requests
import urlparse
import xmltodict

#import urllib.parse as urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

URL = "https://brightree.net"
FIREFOX_BIN = "/home/muhammad/development/tdd/firefox/firefox"
USERS_FILE = "brightree_users.txt"

DBHOST = "localhost"
DBNAME = "btdb"
DBUSER = "root"
DBPASS = "*******"

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
    else:
       val = ''
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
                                        "%s", "%s", "%s", "%s", "%s", "%s", "%s"  ) """

    sql = sql % (get_col_val(rec, 'so_number'),
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
                 get_col_val(rec, 'referral_state'))

    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error, MySQLdb.Warning) as e:
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
    sql = ""
    # .
    # .
    # .
    #


    try:
        # Execute the SQL commands
        r = cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        print ('so_number: ', get_col_val(rec, 'so_number'), r, 'record inserted')

    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print (e)
        print (sql)

        # Rollback in case there is any error
        db.rollback()




def process_data(username, password, browser):
    """"""
    username_elmnt = browser.find_element_by_xpath("//*[@id='txtLoginName']")
    password_elmnt = browser.find_element_by_xpath("//*[@id='txtPassword']")
    username_elmnt.send_keys(username)
    password_elmnt.send_keys(password)
    time.sleep(5)
    password_elmnt.send_keys(Keys.RETURN)
    time.sleep(7)

    homepage_url = browser.current_url
    reports_url = homepage_url.replace('Default.aspx', 'SystemSetup/frmReportScheduleOutput.aspx')

    browser.get(reports_url)

    time.sleep(5)

    session = requests.Session()
    cookies = browser.get_cookies()

    for cookie in cookies: 
        session.cookies.set(cookie['name'], cookie['value'])

    #download_links = browser.find_elements_by_xpath("//a[@title='Preview Report']")
    trs1 = browser.find_elements_by_xpath("//tr[@class='rgRow']")
    trs2 = browser.find_elements_by_xpath("//tr[@class='rgAltRow']")

    trs = trs1 + trs2

    #print (len(download_links), download_links)
    #print (len(trs), trs)
    #print (trs[0], dir(trs[0]))

    for tr in trs:
        tds = tr.find_elements_by_xpath('.//td')
        tr_links = tr.find_elements_by_tag_name('a')
        report_link = tr_links[0].get_attribute('href')
        report_status = tds[2].text
        report_name = tds[3].text
        report_type = tds[4].text
        if report_status == 'Completed' and report_type == 'XML' and \
           (report_name.endswith('SalesOrdersXML') or report_name.endswith('SalesOrdersConfirmedXML')):
            response = session.get(report_link)
            report_contents = response.content
            parsed = urlparse.urlparse(report_link)
            report_filename = urlparse.parse_qs(parsed.query)['FileName'][0]
            doc = xmltodict.parse(report_contents)
            records = doc['Reports']['Detail']['Table1']

            # Save a local copy of the report (no required)
            f = open(report_filename, "w")
            f.write(report_contents)
            f.close()

            for record in records:
                if report_name.endswith('SalesOrdersXML'):
                    insert_data_so(record)
                else:
                    insert_data_soc(record)


def main():
    """"""
    browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
        firefox_path=FIREFOX_BIN
    ))

    browser.get(URL)
    time.sleep(5)

    users = []
    with open(USERS_FILE, 'r') as users_file:
        users_rows = csv.reader(users_file)
        for u in users_rows:
            users.append(u) 

    for user in users:
        process_data(user[0], user[1], browser)

    time.sleep(3)
    #browser.close()
    ##display.stop()

if __name__ == "__main__":

    main()

    print ('done!')

