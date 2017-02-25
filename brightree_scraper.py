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

SO_MAP = { 'so_number': 'SalesOrderNumber',
           'so_date_created': 'SalesOrderDateCreated', 
           'so_created_by': 'SalesOrderCreatedby',
           'so_branch_office': 'SalesOrderBranchOffice',
           'so_status': 'SalesOrderStatus',
           'so_location': 'SalesOrderLocation', 
           'so_reference': 'SalesOrderReference',
           'so_confirm_date': 'SalesOrderConfirmDate',
           'work_in_progress_state': 'WorkInProgressWIPState',
           'patient_id': 'PatientID',
           'ordering_doctor_city': 'OrderingDoctorCity',
           'ordering_doctor_state': 'OrderingDoctorState',
           'insurance_pri_payor': 'InsurancePriPayor',
           'marketing_rep_fullname': 'MarketingRepFullName',
           'referral_name': 'ReferralName',
           'referral_city': 'ReferralCity',
           'referral_state': 'ReferralState',
         }


def get_col_val(rec, key):
    """"""
    if SO_MAP[key] in rec.keys() and type(rec[SO_MAP[key]]) in [type(''), type(u'')]:
       val = rec[SO_MAP[key]]
    else:
       val = ''
    return val


def insert_data(rec):
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
        if report_status == 'Completed' and report_name.endswith('SalesOrdersXML') and report_type == 'XML':
            response = session.get(report_link)
            report_contents = response.content
            parsed = urlparse.urlparse(report_link)
            report_filename = urlparse.parse_qs(parsed.query)['FileName'][0]

            # Save a local copy of the report (no required)
            f = open(report_filename, "w")
            f.write(report_contents)
            f.close()

            doc = xmltodict.parse(report_contents)
            for record in doc['Reports']['Detail']['Table1']:
                insert_data(record)


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

