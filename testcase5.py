from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_5():
    def test(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)

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

        xpath_to_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM = driver.find_element(By.XPATH, xpath_to_pim).click()
        time.sleep(4)

        xpath_to_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD = driver.find_element(By.XPATH, xpath_to_add).click()
        time.sleep(4)

        xpath_to_Fn = '//input[@placeholder="First Name"]'
        FIRSTNAME = driver.find_element(By.XPATH, xpath_to_Fn).send_keys("Azarudin")
        time.sleep(4)

        xpath_to_Mn = '//input[@placeholder="Middle Name"]'
        MIDDLENAME = driver.find_element(By.XPATH, xpath_to_Mn).send_keys("M")
        time.sleep(4)

        xpath_to_Ln = '//input[@placeholder="Last Name"]'
        LASTNAME = driver.find_element(By.XPATH, xpath_to_Ln).send_keys("Asharaf")
        time.sleep(4)

        xpath_to_submit = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, xpath_to_submit).click()
        time.sleep(7)

        driver.find_element(By.XPATH,'//label[text()="Nickname"]/following::input[1]').send_keys("BASU")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Other Id"]/following::input[1]').send_keys("1234567")
        time.sleep(3)

        driver.find_element(By.XPATH,'''//label[text()="Driver's License Number"]/following::input[1]''').send_keys("20222023")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="License Expiry Date"]/following::input[1]').send_keys("2026-12-24")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="SSN Number"]/following::input[1]').send_keys("4000")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="SIN Number"]/following::input[1]').send_keys("6000")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Nationality"]/following::div[2]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Indian"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Marital Status"]/following::div[3]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Married"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::input[1]').send_keys("1999-01-01")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Gender"]/following::span[1]').click()
        time.sleep(3)

        service_1=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input').send_keys("No")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Smoker"]/following::i[1]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::button[1]').click()
        time.sleep(6)

        driver.find_element(By.XPATH,'//label[text()="Blood Type"]/following::div[3]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="AB+"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::button[2]').click()
        time.sleep(5)
        print("Successfully created")

        driver.close()

ss=Project2_5()
ss.test()