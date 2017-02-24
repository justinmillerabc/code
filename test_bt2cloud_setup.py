import unittest
import MySQLdb
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

FIREFOX_BIN = "/root/scripts/firefox/firefox"

class TestFirefox(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Firefox(firefox_binary=FirefoxBinary(
            firefox_path=FIREFOX_BIN
        ))
        self.website_url = "https://brightree.net/"

    def test_url(self):
        self.driver.get(self.website_url)
        website_title = self.driver.title
        self.assertEqual('Brightree Login', website_title)

    def tearDown(self):
        self.driver.quit()
        self.display.stop()


class TestPhantomJS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.website_url = "https://brightree.net/"

    def test_url(self):
        self.driver.get(self.website_url)
        website_title = self.driver.title
        self.assertEqual('Brightree Login', website_title)

    def tearDown(self):
        self.driver.quit()


class TestMySQLdb(unittest.TestCase):

    def setUp(self):
        self.dbhost = "localhost"
        self.dbname = "btdb"
        self.dbuser = "root"
        self.dbpass = "*******"
        self.db = MySQLdb.connect(self.dbhost, self.dbuser, self.dbpass, self.dbname)

    def notest_db(self):
        self.mycursor = self.db.cursor()
        self.mycursor.execute("SELECT * FROM numbers")
        self.mycursor.fetchone()

    def test_dummy(self):
        pass

    def tearDown(self):
        self.db.close()


if __name__ == '__main__':
    unittest.main()

