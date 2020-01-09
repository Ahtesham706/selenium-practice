from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class dashboard():

    def __init__(self, driver):
        self.driver = driver
        
    
    def is_browser_on_the_logoutmenu(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".fa-caret-down")))
        return True