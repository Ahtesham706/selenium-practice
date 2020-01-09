from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Register():
    def __init__(self, driver):
        self.driver = driver
    
    def is_browser_on_register_page(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

    def register_form(self, reg_email,fullname, username,password):
        self.driver.find_element_by_css_selector("#register-email").send_keys(reg_email)
        self.driver.find_element_by_css_selector("#register-name").send_keys(fullname)
        self.driver.find_element_by_css_selector("#register-username").send_keys(username)
        self.driver.find_element_by_css_selector("#register-password").send_keys(password)
        #time.sleep(60)
        
    
    def select_regin(self):
        
        select_ele = Select(self.driver.find_element_by_css_selector('#register-country'))
        select_ele.select_by_visible_text('Pakistan')
        time.sleep(5)

    def submit_btn(self):
        btn_ele = self.driver.find_element_by_css_selector('button[type="submit"]')
        btn_ele.click()
