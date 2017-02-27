import csv
import time 
import MySQLdb
import requests
import urlparse
import xmltodict
import bt_custom

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
DBPASS = "test123"


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
            print (report_link)
            print (report_filename)
            records = doc['Reports']['Detail']['Table1']

            # Save a local copy of the report (no required)
            f = open(report_filename, "w")
            f.write(report_contents)
            f.close()

            if type(records) != type([]):
                records = [records]

            for record in records:
                if report_name.endswith('SalesOrdersXML'):
#                    print ("insert_data_so(record)")
#                    print ('==>', records, type(records) )
#                    print ('==>', record, type(record) )
#                    exit()
                    #insert_data_so(record)
                     pass
                else:
#                    print ("insert_data_soc(record)")
#                    print ('==>', records, type(records) )
#                    print ('==>', record, type(record) )
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

