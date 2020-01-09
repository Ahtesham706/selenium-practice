from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login import loginPage
from pages.dashboard import dashboard
from pages.register_page import Register
import time
class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Driver/chromedriver_win32/chromedriver.exe")
        self.login = loginPage(self.driver)
        self.dashboard = dashboard(self.driver)
        self.register = Register(self.driver)

    def test_login(self):
        #get web link
        self.driver.get("https://www.edx.org/")
        #check element on brwoser
        self.assertTrue(self.login.is_browser_on_the_page())
        #check text on home page
        self.driver.find_element_by_link_text('Sign In').click()
        #check is browser on same page
        self.assertTrue(self.login.is_browser_on_the_loginpage())
        self.login.fill_form('#email', '#password')
        #submit button
        self.login.submit_btn()
        # time.sleep(5)
       
        #logout method
        self.dashboard.is_browser_on_the_logoutmenu()
        self.login.logout()
        # time.sleep(5)
        #check browser is on register page
        self.assertTrue(self.login.is_browser_on_the_page())
        
        self.driver.find_element_by_link_text("Register").click()
        self.register.is_browser_on_register_page()
        self.register.register_form(','','','')
        self.register.select_regin()
        self.register.submit_btn()
        self.dashboard.is_browser_on_the_logoutmenu()
        self.login.logout()
        #time.sleep(10)
        
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
