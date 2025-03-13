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
driver.find_element(By.ID,'mat-input-0').send_keys("automation2@servient.com")   #Login
driver.find_element(By.ID,'mat-input-1').send_keys("Servient@123")
driver.find_element(By.XPATH,'//*[@id="cardAction"]/button').click()
time.sleep(10)   #OTP manually
noRows = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
noColumns = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td'))
# print(noRows, noColumns)
# Select Subscriber
for r in range (1, noRows+1):
    sub_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{r}]/td[1]')
    for subscriber in sub_list:
        if subscriber.text == 'Tomcat 9':
            subscriber.click()
            break
time.sleep(5)
#Select Case
driver.find_element(By.XPATH,'/html/body/app-root/ser-app-list/div/div[2]/div[1]/div[5]/div/div[1]').click()
time.sleep(5)
noCase = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
for c in range (1,noCase+1):
    case_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{c}]/td[1]')
    driver.implicitly_wait(5)
    for case in case_list:
        if case.text == '15OctSmoke':
            case.click()
            break
time.sleep(10)

#Select Docs for Briefcase Creation
total_pages_text = driver.find_element(By.XPATH,'//*[@id="ksp-pane-content"]/div/ser-result-page/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane/div/ser-results-grid/div/kendo-grid/kendo-pager/div/kendo-pager-input/span').text
total_pages = int(total_pages_text.split()[2])

for i in range (2):
    random_no = random.randint(1, total_pages)
    ip_box = driver.find_element(By.XPATH,'//*[@id="ksp-pane-content"]//kendo-numerictextbox//input')
    time.sleep(5)
    ip_box.click()
    time.sleep(1)
    ip_box.send_keys(str(random_no))
    time.sleep(1)  # Optional: Wait a bit for changes to take effect
    print(f"Navigating to page: {random_no}")
    time.sleep(3)
    ip_box.send_keys(Keys.ENTER)  # Simulate pressing Enter after setting the value
    time.sleep(1)
    driver.find_element(By.ID, 'selectAllCheckboxId').click()

driver.find_element(By.XPATH,'//*[@id="icons-parent"]/div[2]/div/ser-batch-operations/button/span[1]/mat-icon').click() #Batch opn
driver.find_element(By.XPATH,'//*[contains(@id, "mat-menu-panel")]/div/button[2]').click() #Select BFC
time.sleep(3)
bfc_name = "5Feb Dynamic BFC"
driver.find_element(By.XPATH,'//*[contains(@id, "mat-input")]').send_keys(bfc_name) # BFC name
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-0"]/form/div[2]/button[1]').click()  # Next button
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="mat-checkbox-1"]/label/span[1]').click()     #Generate PDF
driver.find_element(By.XPATH,'//*[@id="mat-checkbox-2"]/label/span[1]').click()     #Apply stamps
element = driver.find_element(By.XPATH,'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[1]/div[1]/div/span')
driver.execute_script("arguments[0].scrollIntoView();", element)
act = ActionChains(driver)
for i in range (1,5):  #Stamping
    parent = driver.find_element(By.XPATH,f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]')
    act.move_to_element(parent).perform()
    edit_stamp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]/div[2]/span/button'))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@id, "mat-tab-content")]/div/div/kendo-editor/div/div').send_keys('Dynamic Briefcase')  # Stamp value
    driver.find_element(By.XPATH,'//*[contains(@id, "mat-dialog")]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]').click()   #Save button
driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div[2]/button[1]').click()  #Next
time.sleep(3)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cdk-step-content-0-2"]/form/div[2]/button[1]'))).click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cdk-step-content-0-3"]/div[2]/button[1]'))).click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/ser-menu-header/div/mat-toolbar/button[1]'))).click()
driver.find_element(By.XPATH,'//*[@id="nav-menu"]/ser-menu/mat-nav-list/div[6]/div/div').click()    #Select BFC from menu
no_briefcase = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/div[1]/div'))
for b in range (1, no_briefcase+1):
    all_bfc = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{b}]/td[2]/div[1]/div')
    for name in all_bfc:
        if name.text == bfc_name:
            time.sleep(2)
            print(f"{bfc_name} briefcase was successfully created")
            break
            

