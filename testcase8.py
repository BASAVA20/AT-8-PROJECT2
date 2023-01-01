from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_8():
    def test(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/"
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


        driver.find_element(By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//a[text()="Emergency Contacts"]/following::div[1]').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'//h6[text()="Assigned Dependents"]/following::button[1]').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("BASU")
        time.sleep(4)
        driver.find_element(By.XPATH,'//label[text()="Relationship"]/following::div[3]').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Child"]').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input').send_keys("1999-01-01")
        time.sleep(4)
        driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::button[2]').click()
        time.sleep(5)

        driver.close()

ss = Project2_8()
ss.test()

