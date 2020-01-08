from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class loginPage():
    
    def __init__(self,driver):
        self.driver = driver
    
    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-blue')))
        return True

    def is_browser_on_the_loginpage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]')))
        return True

    def fill_form(self):
        email_ele = self.driver.find_element_by_css_selector("#login-email")
        email_ele.send_keys("edx.edx@yopmail.com")
        pass_ele = self.driver.find_element_by_css_selector("#login-password")
        pass_ele.send_keys("edxedx123")
    
    def submit_btn(self):
        btn_ele = self.driver.find_element_by_css_selector('button[type="submit"]')
        btn_ele.click()

    def is_browser_on_the_logoutmenu(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".fa-caret-down")))
        
    def logout(self):
        self.driver.find_element_by_css_selector(".toggle-user-dropdown").click()
        self.driver.find_element_by_link_text("Sign Out").click()
        