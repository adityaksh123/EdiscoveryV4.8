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

#Subscriber
noRows = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
noColumns = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td'))
for r in range (1, noRows+1):
    sub_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{r}]/td[1]')
    for subscriber in sub_list:
        if subscriber.text == 'Tomcat 9':
            subscriber.click()
            break
time.sleep(10)

driver.find_element(By.XPATH,'/html/body/app-root/ser-app-list/div/div[2]/div[2]/div[2]/div/div/div[2]/h1').click()    #SELECT MP
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="mat-expansion-panel-header-2"]/span[1]/mat-panel-title').click()    #Click Module mgmt
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@id, "cdk-accordion-child-)"]/div/div/mat-nav-list/a[3]/div'))).click()     #Click S&C
time.sleep(5)
matter_rows = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-management-portal/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-modules/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div/ser-landing-page/div[2]/ser-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
print(matter_rows)
for r in range (10, matter_rows):
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,f'/html/body/app-root/ser-management-portal/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-modules/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div/ser-landing-page/div[2]/ser-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{r}]/td[2]'))).click()    #edit matter entry
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@id, "mat-tab-label-")]/div[text()= "User Assignments"]'))).click()     #user assignment
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@id, "mat-tab-content-") and contains(@id, "-1")]/div/div/ser-user-assignment/div[1]/mat-toolbar/button'))).click()      #assign users
    time.sleep(4)
    user = driver.find_element(By.XPATH,'//span[contains(text(),"automation2@servient.com")]')
    driver.execute_script("arguments[0].scrollIntoView();", user)
    driver.execute_script("arguments[0].style.border='3px solid red'", user)    #red mark user
    row = user.find_element(By.XPATH, './ancestor::tr')
    row_index = len(row.find_elements(By.XPATH, 'preceding-sibling::tr'))
    driver.find_element(By.XPATH,f'//*[@id="{row_index}"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/app-root/ser-management-portal/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-modules/mat-drawer-container/mat-drawer/div/div[1]/div/mat-card/mat-card-actions/button[1]').click()    #Next
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectAllItems"]'))).click()   #Select Admin role
    driver.find_element(By.XPATH,'/html/body/app-root/ser-management-portal/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-modules/mat-drawer-container/mat-drawer/div/div[1]/div/mat-card/mat-card-actions/button[1]/span[1]').click()     #Apply
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/ser-management-portal/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-modules/mat-drawer-container/mat-drawer-content/div/mat-toolbar/div[2]/button'))).click()
    time.sleep(5)


