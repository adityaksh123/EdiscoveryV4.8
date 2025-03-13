import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

def initialize_driver():
    service = Service(executable_path="/Users/adityakshirsagar/chromedriver-mac-x64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://qa.servient.net/ng/#/login")
    driver.maximize_window()
    return driver

def login(driver, username, password):
    driver.find_element(By.ID, 'mat-input-0').send_keys(username)
    driver.find_element(By.ID, 'mat-input-1').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="cardAction"]/button').click()
    time.sleep(10)  # Wait for OTP manually

def select_subscriber(driver, subscriber_name):
    subscribers = driver.find_elements(By.XPATH, '//table/tbody/tr/td[1]')
    for subscriber in subscribers:
        if subscriber.text == subscriber_name:
            subscriber.click()
            break
    time.sleep(5)

def select_case(driver, case_name):
    driver.find_element(By.XPATH, '//div[5]/div/div[1]').click()
    time.sleep(5)
    cases = driver.find_elements(By.XPATH, '//table/tbody/tr/td[1]')
    for case in cases:
        if case.text == case_name:
            case.click()
            break
    time.sleep(10)

def select_documents_for_briefcase(driver, pages=2):
    total_pages = int(driver.find_element(By.XPATH, '//*[@id="ksp-pane-content"]//kendo-pager-input/span').text.split()[2])
    for _ in range(pages):
        random_page = random.randint(1, total_pages)
        input_box = driver.find_element(By.XPATH, '//*[@id="ksp-pane-content"]//kendo-numerictextbox//input')
        time.sleep(1)
        input_box.click()
        input_box.send_keys(str(random_page))
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.ID, 'selectAllCheckboxId').click()

def create_briefcase(driver, briefcase_name):
    driver.find_element(By.XPATH, '//*[@id="icons-parent"]/div[2]/div/ser-batch-operations/button/span[1]/mat-icon').click()
    driver.find_element(By.XPATH, '//*[contains(@id, "mat-menu-panel")]/div/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[contains(@id, "mat-input")]').send_keys(briefcase_name)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-0"]/form/div[2]/button[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-1"]/label/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="mat-checkbox-2"]/label/span[1]').click()

def stamp_documents(driver):
    action = ActionChains(driver)
    element = driver.find_element(By.XPATH,'//*[@id="cdk-step-content-0-1"]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[4]/td[1]/div[1]/div/span')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    for i in range(1, 5):
        parent = driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[4]')
        action.move_to_element(parent).perform()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[contains(@id, "cdk-step-content")]/form/div[1]/div/div[7]/div/ser-stamps-grid-view/div/kendo-grid/div/kendo-grid-list/div/div[1]/table/tbody/tr[{i}]/td[4]/div[2]/span/button'))).click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[contains(@id, "mat-tab-content")]/div/div/kendo-editor/div/div').send_keys('Dynamic Briefcase')
        driver.find_element(By.XPATH, '//*[contains(@id, "mat-dialog")]/stamp-dialog/div/mat-card/form/mat-card-actions/button[1]').click()

def finalize_briefcase(driver):
    driver.find_element(By.XPATH, '//*[@id="cdk-step-content-0-1"]/form/div[2]/button[1]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-step-content-0-2"]/form/div[2]/button[1]'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-step-content-0-3"]/div[2]/button[1]'))).click()

def verify_briefcase_creation(driver, briefcase_name):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/ser-document-review/ser-main-app/mat-sidenav-container/mat-sidenav-content/ser-menu-header/div/mat-toolbar/button[1]'))).click()
    driver.find_element(By.XPATH, '//*[@id="nav-menu"]/ser-menu/mat-nav-list/div[6]/div/div').click()
    briefcases = driver.find_elements(By.XPATH, '//table/tbody/tr/td[2]/div[1]/div')
    for briefcase in briefcases:
        if briefcase.text == briefcase_name:
            print(f"{briefcase_name} briefcase was successfully created")
            break

def main():
    driver = initialize_driver()
    login(driver, "automation2@servient.com", "Servient@123")
    select_subscriber(driver, "Tomcat 9")
    select_case(driver, "15OctSmoke")
    select_documents_for_briefcase(driver)
    create_briefcase(driver, "5Feb Dynamic BFC3")
    stamp_documents(driver)
    finalize_briefcase(driver)
    verify_briefcase_creation(driver, "5Feb Dynamic BFC")
    driver.quit()

if __name__ == "__main__":
    main()
