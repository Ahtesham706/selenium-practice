from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login import loginPage
import time
class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Driver/chromedriver_win32/chromedriver.exe")
        self.login = loginPage(self.driver)

    def test_login(self):
        #get web link
        self.driver.get("https://www.edx.org/")
        #check element on brwoser
        self.assertTrue(self.login.is_browser_on_the_page())
        #check text on home page
        self.driver.find_element_by_link_text('Sign In').click()
        #check is browser on same page
        self.assertTrue(self.login.is_browser_on_the_loginpage())
        # fill form methon
        self.login.fill_form()
        #submit button
        self.login.submit_btn()
        self.login.is_browser_on_the_logoutmenu()
        #logout method
        self.login.logout()
        time.sleep(10)

        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
