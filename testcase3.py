from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Project2_3():
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

        xpath_to_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        pim_element = driver.find_element(By.XPATH, xpath_to_pim)
        pim_element.click()
        time.sleep(3)

        xpath_to_pimmenu = '//a[@href="/web/index.php/pim/viewPimModule"]'
        pimmenu_element = driver.find_element(By.XPATH, xpath_to_pimmenu)
        print(pimmenu_element.is_displayed())
        time.sleep(3)

        xpath_to_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        add_button = driver.find_element(By.XPATH, xpath_to_add)
        add_button.click()
        time.sleep(3)

        xpath_to_firstname = '//input[@placeholder="First Name"]'
        firstname_element = driver.find_element(By.XPATH, xpath_to_firstname)
        firstname_element.send_keys("Ricky")
        time.sleep(3)

        xpath_to_middlename = '//input[@placeholder="Middle Name"]'
        middlename_element = driver.find_element(By.XPATH, xpath_to_middlename)
        middlename_element.send_keys("Thomas")
        time.sleep(3)

        xpath_to_lastname = '//input[@placeholder="Last Name"]'
        lastname_element = driver.find_element(By.XPATH, xpath_to_lastname)
        lastname_element.send_keys("Hughes")
        time.sleep(3)

        xpath_to_enablelogin = '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        enablelogin = driver.find_element(By.XPATH, xpath_to_enablelogin)
        enablelogin.click()
        time.sleep(4)

        xpath_to_usernamepim = "//label[text()='Username']/following::div[1]/input"
        time.sleep(4)
        usernamepim_element = driver.find_element(By.XPATH, xpath_to_usernamepim)
        usernamepim_element.send_keys("BASU VALMIKI")
        time.sleep(3)

        xpath_to_enablestatus = '//label[normalize-space()="Enabled"]'
        enablestatus_element = driver.find_element(By.XPATH, xpath_to_enablestatus)
        enablestatus_element.click()
        time.sleep(3)

        xpath_to_password_pim = "//div/label[text()='Password']/following::div[1]/input"
        password_pim_element = driver.find_element(By.XPATH, xpath_to_password_pim)
        time.sleep(3)
        password_pim_element.send_keys("Basu@4111")

        xpath_to_confirmpassword_pim = "//div/label[text()='Confirm Password']/following::div[1]/input"
        confirmpassword_pim_element = driver.find_element(By.XPATH, xpath_to_confirmpassword_pim)
        time.sleep(3)
        confirmpassword_pim_element.send_keys("Basu@4111")
        time.sleep(3)

        xpath_to_save = '//button[@type="submit"]'
        save_button = driver.find_element(By.XPATH, xpath_to_save)
        save_button.click()
        time.sleep(3)
        print("SUCCESSFULLY CREATED NEW EMPLOYEE LIST AND SAVE IT ")
        driver.close()

ss = Project2_3()
ss.test()






