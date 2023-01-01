from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Project2_2():
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

        xpath_to_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        switch_to_admin = driver.find_element(By.XPATH, xpath_to_admin)
        switch_to_admin.click()
        time.sleep(3)

        xpath_to_usermanagement='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
        usermanagement=driver.find_element(By.XPATH,xpath_to_usermanagement).click()
        time.sleep(4)

        xpath_to_usertab='//a[@href="#"]'
        usertab_element=driver.find_element(By.XPATH,xpath_to_usertab).click()
        time.sleep(3)

        xpath_to_userrole='//label[text()="User Role"]/following::div[3]'
        userrole_eleemnt=driver.find_element(By.XPATH,xpath_to_userrole).click()
        time.sleep(3)

        xpath_to_admin ='//div[@role="listbox"]//span[text()="Admin"]'
        dropdown_admin=driver.find_element(By.XPATH,xpath_to_admin).click()
        time.sleep(3)

        xpath_to_status='//label[text()="Status"]/following::div[3]'
        status=driver.find_element(By.XPATH,xpath_to_status).click()
        time.sleep(3)

        xpath_to_enabled='//div[@role="listbox"]//span[text()="Enabled"]'
        dropdown_enabled=driver.find_element(By.XPATH,xpath_to_enabled).click()
        time.sleep(3)

        xpath_to_userrole = '//label[text()="User Role"]/following::div[3]'
        userrole_eleemnt = driver.find_element(By.XPATH, xpath_to_userrole).click()
        time.sleep(3)

        xpath_to_ESS='//div[@role="listbox"]//span[text()="ESS"]'
        ESS_ELEEMNT=driver.find_element(By.XPATH,xpath_to_ESS).click()
        time.sleep(3)

        xpath_to_status1 = '//label[text()="Status"]/following::div[3]'
        status1_eleemnt = driver.find_element(By.XPATH, xpath_to_status1).click()
        time.sleep(3)

        xpath_to_disabled='//div[@role="listbox"]//span[text()="Disabled"]'
        dropdown_disabled=driver.find_element(By.XPATH,xpath_to_disabled).click()
        time.sleep(3)

        driver.close()

ss=Project2_2()
ss.test()
