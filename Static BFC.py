import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_object = Service(executable_path="/Users/adityakshirsagar/chromedriver-mac-x64/chromedriver")
driver = webdriver.Chrome(service=serv_object)
driver.get("https://qa.servient.net/ng/#/login")
driver.maximize_window()
driver.find_element(By.ID,'mat-input-0').send_keys("aditya.kshirsagar@servient.com")   #Login
driver.find_element(By.ID,'mat-input-1').send_keys("Maxhusky@41")
driver.find_element(By.XPATH,'//*[@id="cardAction"]/button').click()
time.sleep(10)   #OTP manually
noRows = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
noColumns = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td'))
# print(noRows, noColumns)
# Select Subscriber
for r in range (1, noRows+1):
    sub_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{r}]/td[1]')
    for subscriber in sub_list:
        if subscriber.text == 'QA_EDis481Canvas0841':
            subscriber.click()
            break
time.sleep(5)
#Select Case
driver.find_element(By.XPATH,'/html/body/app-root/ser-app-list/div/div[2]/div[1]/div[5]/div/div[1]').click()
time.sleep(5)
noCase = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
print(noCase)
for c in range (1, noCase+1):
    case_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{c}]/td[1]')
    driver.implicitly_wait(5)
    for case in case_list:
        if case.text == 'Matter1_Case1':
            case.click()
            break
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="selectAllCheckboxId"]').click()  #Select all docs checkbox
last_doc = driver.find_element(By.XPATH,'//*[@id="2"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="icons-parent"]/div[2]/div/ser-batch-operations/button/span[1]/mat-icon').click()  #Batch operation
driver.find_element(By.XPATH,'//*[@id="mat-menu-panel-22"]/div/button[2]').click() #Select BFC
time.sleep(2)
bfc_name = 'Static BFC5'
driver.find_element(By.XPATH,'//*[contains(@id, "mat-input")]').send_keys(bfc_name) # BFC name
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-0"]/form/div[2]/button[1]').click()  # Next button
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div[2]/button[1]').click()  #Next
time.sleep(3)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cdk-step-content-0-2"]/form/div[2]/button[1]'))).click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cdk-step-content-0-3"]/div[2]/button[1]'))).click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/ser-menu-header/div/mat-toolbar/button[1]'))).click()
driver.find_element(By.XPATH,'//*[@id="nav-menu"]/ser-menu/mat-nav-list/div[6]/div/div').click()
no_briefcase = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/div[1]/div'))
for b in range (1, no_briefcase+1):
    bfc_name1 = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{b}]/td[2]/div[1]/div')
    for name in bfc_name1:
        if name.text == bfc_name:
            time.sleep(2)
            print(f"{bfc_name} briefcase was successfully created")
            break

