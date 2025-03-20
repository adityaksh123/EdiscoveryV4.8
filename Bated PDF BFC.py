import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_object = Service(executable_path="/Users/adityakshirsagar/chromedriver-mac-x64/chromedriver")
driver = webdriver.Chrome(service=serv_object)
act = ActionChains(driver)
driver.get("https://qa.servient.net/ng/#/login")
driver.maximize_window()
driver.find_element(By.ID,'mat-input-0').send_keys("automation2@servient.com")   #Login
driver.find_element(By.ID,'mat-input-1').send_keys("Servient@1234")
driver.find_element(By.XPATH,'//*[@id="cardAction"]/button').click()
time.sleep(5)   #OTP manually

#Subscriber
noRows = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
noColumns = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td'))
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
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="page-content"]/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane[1]/kendo-splitter/kendo-splitter-bar/div[1]').click()     #Facet open
driver.find_element(By.XPATH,'//*[@id="facetAreaPane"]/div/ser-facet-area/div/mat-tree/mat-tree-node[5]/div').click()       #Select Production
time.sleep(3)
n = random.randint(6,7)
bates_name = (driver.find_element(By.XPATH,f'//*[@id="facetAreaPane"]/div/ser-facet-area/div/mat-tree/mat-tree-node[{n}]/div'))
bates_name.click()
selected_bate = bates_name.text.split()[0]
print(f"Selected bate =", selected_bate)
driver.find_element(By.XPATH,'//*[@id="selectAllCheckboxId"]').click()     #Select all docs checkbox
WebDriverWait(driver,7).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ksp-pane-content"]/div/ser-result-page/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane/div/ser-results-grid/div/kendo-grid/kendo-grid-toolbar/div/button[1]/span[1]'))).click()     #Select all docs link
driver.find_element(By.XPATH,'//*[@id="icons-parent"]/div[2]/div/ser-batch-operations/button/span[1]/mat-icon').click() #Batch opn
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@id, "mat-menu-panel-")]/div/button[2]'))).click() #Select BFC
time.sleep(2)
bfc_name = "24Feb Trial BFC12"
driver.find_element(By.XPATH,'//*[contains(@id,"mat-input")]').send_keys(bfc_name) # BFC name
time.sleep(3)
driver.find_element(By.XPATH,'//*[contains(@id, "cdk-step-content-")]/form/div[2]/button[1]').click()    #Next
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="mat-checkbox-1"]/label/span[2]').click()     #Generate PDF checkbox
stamp = driver.find_element(By.XPATH,'//*[contains(@id, "mat-checkbox-")]/label/span[2]')
driver.execute_script("arguments[0].scrollIntoView();", stamp)
time.sleep(3)

# noofbates=len(driver.find_elements(By.XPATH,'//*[@id="cdk-drop-list-2"]/li'))        #number 34 in this xpath will vary from case to case
# print(f"No of bates=", noofbates)
# priorities = driver.find_elements(By.XPATH,'//*[@id="cdk-drop-list-2"]/li')
# for priority in priorities:
#     print(priority.text)

# prod_name = driver.find_element(By.XPATH,'//*[@id="cdk-drop-list-5"]/li[4]')    #Drag and Drop in View priority
# driver.execute_script("arguments[0].scrollIntoView();", prod_name)
# driver.execute_script("arguments[0].style.border='3px solid red'", prod_name)
# print(prod_name.text)
# target_drop = driver.find_element(By.XPATH,f'//li[contains(@id, "cdk-drop-list-34")]//div[contains(text(), "Redacted File")]')
# print(target_drop.text)
# act.drag_and_drop(prod_name, target_drop).perform()
# time.sleep(10)

driver.find_element(By.XPATH,'//span[@class="mat-option-text" and normalize-space(.)="DB Field"]').click()    #DB Fields type
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@id, "mat-dialog")]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]'))).click()    #Save
time.sleep(5)
# driver.find_element(By.XPATH,'//*[contains(@id, "mat-option-")]/span').click()     #Bates Stamp values
# driver.find_element(By.XPATH,'//*[@id="mat-dialog-1"]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]').click()    #save
for i in range (2,5):
    parent = driver.find_element(By.XPATH,f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]')  # Hover in 2nd row of apply stamps
    act.move_to_element(parent).perform()
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]/div[2]/span/button/span[1]/i'))).click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[contains(@id, "mat-tab-content")]/div/div/kendo-editor/div/div').send_keys("AK Bated BFC")    #Add stamp
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@id, "mat-dialog")]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]'))).click()    #Save
driver.find_element(By.XPATH,'//*[@id="cdk-step-content-0-1"]/form/div[2]/button[1]').click()     #File types Next
time.sleep(2)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cdk-step-content-0-2"]/form/div[2]/button[1]'))).click()    #File Next
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="cdk-step-content-0-3"]/div[2]/button[1]'))).click()    #Create

#Check if BFC is successful
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/ser-menu-header/div/mat-toolbar/button[1]'))).click()
driver.find_element(By.XPATH,'//*[@id="nav-menu"]/ser-menu/mat-nav-list/div[6]/div/div').click()  # Select BFC from menu
time.sleep(5)
no_briefcase = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/div[1]/div'))
for b in range(1, no_briefcase + 1):
    all_bfc = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{b}]/td[2]/div[1]/div')
    for name in all_bfc:
        if name.text == bfc_name:
            time.sleep(2)
            print(f"{bfc_name} briefcase was successfully created")
            break

