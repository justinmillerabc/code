#!/usr/bin/env python

import os
import sys
import csv
import time 
import MySQLdb
import requests
import xmltodict
from btconfig import *
from btdbutils import *
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

if sys.version_info[0] == 3:
    import urllib.parse as urlparse
else:
    import urlparse

script_path = '/'.join(os.path.abspath(__file__).split('/')[:-1])
xmlfiles_path = '/'.join(os.path.abspath(__file__).split('/')[:-1]) + '/' + XML_FILES_FOLDER
users_filename = script_path + '/' + USERS_FILE
reports_list = ["salesordersxml", "salesordersconfirmedxml", "socitemsxml", "paymentsxml", "parscreatedxml", "parsloggedxml",\
                "rcmclosedxml", "sovoidxml", "invoicesstatusxml", "invoicescreatedxml"]

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

    trs1 = browser.find_elements_by_xpath("//tr[@class='rgRow']")
    trs2 = browser.find_elements_by_xpath("//tr[@class='rgAltRow']")

    trs = trs1 + trs2

    for tr in trs:
        tds = tr.find_elements_by_xpath('.//td')
        tr_links = tr.find_elements_by_tag_name('a')
        report_link = tr_links[0].get_attribute('href')
        report_status = tds[2].text
        report_name = tds[3].text.split("\\")[-1]
        report_type = tds[4].text
        
        try:
            parsed = urlparse.urlparse(report_link)
            report_filename = urlparse.parse_qs(parsed.query)['FileName'][0]
            report_file = xmlfiles_path + '/' + report_name + '_' + report_filename
            print ("Processing: " + report_name + " (" + report_filename + ") ...")
        except:
            continue

        if report_status == 'Completed' and report_type == 'XML' and (report_name.lower() in reports_list):
            response = session.get(report_link)
            report_contents = response.content

            if sys.version_info[0] == 3:
                report_contents_str = report_contents.decode().replace("&#x1F;", "")
                doc = xmltodict.parse(report_contents_str)
            else:
                report_contents = report_contents.replace("&#x1F;", "")
                doc = xmltodict.parse(report_contents)

            try:
                records = doc['Reports']['Detail']['Table1']
            except:
                records = []

            # Save a local copy of the report (no required)
            f = open(report_file, "wb")
            f.write(report_contents)
            f.close()

            if type(records) != type([]):
                records = [records]

            for record in records:
                if report_name.endswith('SalesOrdersXML'):
                    insert_data_so(record)
                elif report_name.endswith('SalesOrdersConfirmedXML'):
                    insert_data_soc(record)
                elif report_name.endswith('SOVoidXML'):
                    insert_data_sovoid(record)
                elif report_name.endswith('SOCItemsXML'):
                    insert_data_socitems(record)
                elif report_name.endswith('RCMClosedXML'):
                    insert_data_rcmclosed(record)
                elif report_name.endswith('PARsCreatedXML'):
                    insert_data_parscreated(record)
                elif report_name.endswith('ParsLoggedXML'):
                    insert_data_parslogged(record)
                elif report_name.endswith('PaymentsXML'):
                    insert_data_payments(record)
                elif report_name.endswith('InvoicesCreatedXML'):
                    insert_data_invoicescreated(record)
                elif report_name.endswith('InvoicesStatusXML'):
                    delete_data_invoicesstatus()
                    insert_data_invoicesstatus(record)


def main():
    """"""
    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ': Started')

#    browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
#        firefox_path=FIREFOX_BIN
#    ))
    browser = webdriver.PhantomJS()

    browser.get(URL)
    time.sleep(5)

    users = []
    with open(users_filename, 'r') as users_file:
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

    print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ': Finished')
