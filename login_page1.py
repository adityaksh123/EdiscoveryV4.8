import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
serv_object = Service(executable_path="/Users/adityakshirsagar/chromedriver-mac-x64/chromedriver")
driver = webdriver.Chrome(service=serv_object)

class LoginPage():
    def __init__(self,driver, config):
        self.driver = driver
        self.config = config

    def login(self):
        username = self.config['username']
        password = self.config['password']
        self.driver.find_element(By.ID, 'mat-input-0').send_keys(username)  # Login
        self.driver.find_element(By.ID, 'mat-input-1').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="cardAction"]/button').click()

    def subscriber(self):
        subscriber_name = self.config['subscriber_name']
        noRows = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
        for r in range(1, noRows + 1):
            sub_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{r}]/td[1]')
            for subscriber in sub_list:
                if subscriber.text == subscriber_name:
                    subscriber.click()
                    break
        time.sleep(5)

    def case(self):
        case_name = self.config['case_name']
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/ser-app-list/div/div[2]/div[1]/div[5]/div/div[1]'))).click()
        time.sleep(5)
        noCase = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
        for c in range(1, noCase + 1):
            case_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{c}]/td[1]')
            driver.implicitly_wait(5)
            for case in case_list:
                if case.text == case_name:
                    case.click()
                    break
