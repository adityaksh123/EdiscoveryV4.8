import time

import openpyxl
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
# act = ActionChains(driver)
# norows = len(driver.find_elements(By.XPATH,'xyz/tr'))
# element = driver.find_element(By.XPATH,f'xyz/tr[{r}]/td[5]')
# for i in range (1,norows):

# # arr = {1,2,4,5,6,6,7,8,8}
# str = ("aditya")
# for i in range (0,7):
#     print(str[i])

driver.get("https://www.example.com")
driver.execute_script("window.open('https://www.google.com');")
driver.execute_script("window.open('https://www.wikipedia.org');")
time.sleep(5)

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(f"Window titles=",{driver.title})
    if driver.title=='Google':
        print(f"Switched to desired window,",{driver.title})
        driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys('Black holes')
        time.sleep(5)
    driver.close()
driver.switch_to.new_window("tab")

# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     print(f"Checking window: {driver.title}")  # Debugging
#     if driver.title == "Google":  # Change this title to your target
#         print("Switched to Window4")
#         break