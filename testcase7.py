from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_7():
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

        driver.find_element(By.XPATH,'//a[text()="Contact Details"]/following::div[1]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//h6[text()="Assigned Emergency Contacts"]/following::button[1]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("BASU")
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("Friend")
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys("147852963")
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys("9108805560")
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys("143265278")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Mobile"]/following::button[2]').click()
        time.sleep(6)

        driver.close()


ss=Project2_7()
ss.test()
