from Briefcase.login_page1 import LoginPage
import yaml
import time
from selenium import webdriver

def execution (driver,config):
    driver.get(config["base_url"])
    driver.maximize_window()
    time.sleep(3)
    login_page1 = LoginPage(driver,config)
    login_page1.login()
    time.sleep(3)
    login_page1.subscriber()
    time.sleep(3)
    login_page1.case()


if __name__ == "__main__":
    # Load config.yaml
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Call execution function
    execution(driver, config)

    # Optional: Close browser after test
    driver.quit()