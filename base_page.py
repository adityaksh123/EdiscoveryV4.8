from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def click(self,locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self,locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text)

