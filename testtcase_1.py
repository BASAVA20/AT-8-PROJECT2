from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class Project2_1():
    def test(self):

        driver = webdriver.Chrome()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        xpath_to_username = '//input[@name="username"]'
        username_element = driver.find_element(By.XPATH, xpath_to_username)
        username_element.send_keys("Admin")
        time.sleep(2)

        xpath_to_password = '//input[@name="password"]'
        password_element = driver.find_element(By.XPATH, xpath_to_password)
        password_element.send_keys("admin123")
        time.sleep(2)

        xpath_to_login = '//button[@type="submit"]'
        login_button = driver.find_element(By.XPATH, xpath_to_login)
        login_button.click()
        time.sleep(2)

        xpath_to_searchbox = '//input[@placeholder="Search"]'
        searchbox_element = driver.find_element(By.XPATH, xpath_to_searchbox)
        print(searchbox_element.is_displayed())
        print(searchbox_element.is_enabled())
        time.sleep(2)

        #  Xpath for search button
        xpath_for_search_button = '//input[@placeholder="Search"]'
        search_button = driver.find_element(By.XPATH, xpath_for_search_button)


        # Using for loop to search in upper
        list = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory",
                "Maintenance", "Buzz"]

        for k in list:
            search_button.send_keys(k.upper())
            time.sleep(2)
            # Clearing existing text
            search_button.send_keys(Keys.CONTROL, 'k')
            search_button.send_keys(Keys.BACKSPACE)
            time.sleep(2)
        # Using for loop to search in upper
        for k in list:
            search_button.send_keys(k.lower())
            time.sleep(1)
            # Clearing existing text
            search_button.send_keys(Keys.CONTROL, 'k')
            search_button.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        print("INDIVDUAL MENU NAMES SHOULD APPER UNDER SEARCH BOX")

        driver.close()

ss = Project2_1()
ss.test()






