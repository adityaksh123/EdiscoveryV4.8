import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def initialise_driver():
    serv_object = Service(executable_path="/Users/adityakshirsagar/chromedriver-mac-x64/chromedriver")
    driver = webdriver.Chrome(service=serv_object)
    driver.get("https://qa.servient.net/ng/#/login")
    driver.maximize_window()
    return driver

def login(driver, username, password):
    driver.find_element(By.ID, 'mat-input-0').send_keys(username)  # Login
    driver.find_element(By.ID, 'mat-input-1').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="cardAction"]/button').click()
    time.sleep(5)

def subscriber(driver,sub_name):
    noRows = len(driver.find_elements(By.XPATH, '/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
    noColumns = len(driver.find_elements(By.XPATH,'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td'))
    for r in range(1, noRows + 1):
        sub_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-select-subscriber/div/div[2]/ser-subscriber-grid/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{r}]/td[1]')
        for subscriber in sub_list:
            if subscriber.text == sub_name:
                subscriber.click()
                break
        time.sleep(5)

def case(driver,case_name):
    driver.find_element(By.XPATH, '/html/body/app-root/ser-app-list/div/div[2]/div[1]/div[5]/div/div[1]').click()
    time.sleep(5)
    noCase = len(driver.find_elements(By.XPATH, '/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr'))
    for c in range(1, noCase + 1):
        case_list = driver.find_elements(By.XPATH,f'/html/body/app-root/ser-switchboard/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-case-list/div/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{c}]/td[1]')
        driver.implicitly_wait(5)
        for case in case_list:
            if case.text == case_name:
                case.click()
                break
time.sleep(5)

def select_prod(driver):
    driver.find_element(By.XPATH, '//*[@id="page-content"]/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane[1]/kendo-splitter/kendo-splitter-bar/div[1]').click()  # Facet open
    driver.find_element(By.XPATH, '//*[@id="facetAreaPane"]/div/ser-facet-area/div/mat-tree/mat-tree-node[5]/div').click()  # Select Production
    time.sleep(3)
    n = random.randint(6, 7)
    bates_name = (driver.find_element(By.XPATH, f'//*[@id="facetAreaPane"]/div/ser-facet-area/div/mat-tree/mat-tree-node[{n}]/div'))
    bates_name.click()
    selected_bate = bates_name.text.split()[0]
    driver.find_element(By.XPATH, '//*[@id="selectAllCheckboxId"]').click()  # Select all docs checkbox
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ksp-pane-content"]/div/ser-result-page/mat-drawer-container/mat-drawer-content/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane/div/ser-results-grid/div/kendo-grid/kendo-grid-toolbar/div/button[1]/span[1]'))).click()  # Select all docs link
    time.sleep(5)

def briefcase (driver,bfc_name):
    act = ActionChains(driver)
    driver.find_element(By.XPATH, '//*[@id="icons-parent"]/div[2]/div/ser-batch-operations/button/span[1]/mat-icon').click()  # Batch opn
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "mat-menu-panel-")]/div/button[2]'))).click()  # Select BFC
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@id,"mat-input")]').send_keys(bfc_name)  # BFC name
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[contains(@id, "cdk-step-content-")]/form/div[2]/button[1]').click()  # Next
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-1"]/label/span[2]').click()  # Generate PDF checkbox
    stamp = driver.find_element(By.XPATH, '//*[contains(@id, "mat-checkbox-")]/label/span[2]')
    driver.execute_script("arguments[0].scrollIntoView();", stamp)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-2"]/label/span[2]').click()  # Apply stamps checkbox  # Hover in 1s row of apply stamps
    element = driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[1]/div[1]/div/span')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    act.move_to_element(driver.find_element(By.XPATH, f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[4]')).perform()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[1]/td[4]/div[2]/span/button/span[1]/i'))).click()  # edit row 1
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="mat-select-16"]/div/div[2]').click()  # Adhoc Dropdown
    time.sleep(3)

def apply_stamps(driver):
    act = ActionChains(driver)
    driver.find_element(By.XPATH, '//span[@class="mat-option-text" and normalize-space(.)="DB Field"]').click()  # DB Fields type
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "mat-dialog")]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]'))).click()  # Save
    time.sleep(5)
    for i in range(2, 5):
        parent = driver.find_element(By.XPATH, f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]')  # Hover in 2nd row of apply stamps
        act.move_to_element(parent).perform()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]/div[2]/span/button/span[1]/i'))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[contains(@id, "mat-tab-content")]/div/div/kendo-editor/div/div').send_keys("AK Bated BFC")  # Add stamp
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(@id, "mat-dialog")]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]'))).click()  # Save
    driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div[2]/button[1]').click()  # File types Next
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cdk-step-content-0-2"]/form/div[2]/button[1]'))).click()  # File Next
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-step-content-0-3"]/div[2]/button[1]'))).click()  # Create

def bfc_success(driver, bfc_name):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/ser-menu-header/div/mat-toolbar/button[1]'))).click()
    driver.find_element(By.XPATH,
                        '//*[@id="nav-menu"]/ser-menu/mat-nav-list/div[6]/div/div').click()  # Select BFC from menu
    time.sleep(5)
    no_briefcase = len(driver.find_elements(By.XPATH,
                                            '/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr/td[2]/div[1]/div'))
    for b in range(1, no_briefcase + 1):
        all_bfc = driver.find_elements(By.XPATH,
                                       f'/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/div/main/ser-briefcases/ser-briefcase-list/div/kendo-splitter/kendo-splitter-pane/kendo-splitter/kendo-splitter-pane[2]/div[2]/ser-briefcase-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{b}]/td[2]/div[1]/div')
        for name in all_bfc:
            if name.text == bfc_name:
                time.sleep(2)
                print(f"{bfc_name} briefcase was successfully created")
                break

def main():
    driver = initialise_driver()
    login(driver, "automation2@servient.com", "Servient@123")
    subscriber(driver, "Tomcat 9")
    case(driver, "15OctSmoke")
    select_prod(driver)
    briefcase(driver, "25Feb Dynamic BFC3")
    apply_stamps(driver)
    bfc_success(driver,"25Feb Dynamic BFC3")
    driver.quit()

if __name__ == "__main__":
    main()
