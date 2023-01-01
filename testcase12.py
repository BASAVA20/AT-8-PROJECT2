from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_12():
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

        xpath_to_pim='//a[@href="/web/index.php/pim/viewPimModule"]'
        PIM=driver.find_element(By.XPATH,xpath_to_pim).click()
        time.sleep(4)


        xpath_to_add='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        ADD=driver.find_element(By.XPATH,xpath_to_add).click()
        time.sleep(4)


        xpath_to_Fn='//input[@placeholder="First Name"]'
        FIRSTNAME=driver.find_element(By.XPATH,xpath_to_Fn).send_keys("Azarudin")
        time.sleep(4)


        xpath_to_Mn='//input[@placeholder="Middle Name"]'
        MIDDLENAME=driver.find_element(By.XPATH,xpath_to_Mn).send_keys("Mohamed")
        time.sleep(4)

        xpath_to_Ln='//input[@placeholder="Last Name"]'
        LASTNAME=driver.find_element(By.XPATH,xpath_to_Ln).send_keys("Asharaf")
        time.sleep(4)

        xpath_to_submit = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        submit = driver.find_element(By.XPATH, xpath_to_submit).click()
        time.sleep(7)

        driver.find_element(By.XPATH,'//a[text()="Immigration"]/following::div[2]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//h6[text()="Assigned Salary Components"]/following::button[1]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Basic Salary")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Pay Grade"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Grade 1"]').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'//label[text()="Pay Frequency"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Monthly"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Currency"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="United States Dollar"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys("44220")
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea').send_keys("Salary Amount per month")
        time.sleep(4)

        driver.find_element(By.XPATH,'//p[text()="Include Direct Deposit Details"]/following::div[1]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input').send_keys("957605704272")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Account Type"]/following::div[3]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Savings"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input').send_keys("583124")
        time.sleep(3)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input').send_keys("40000")
        time.sleep(3)

        driver.find_element(By.XPATH,'//label[text()="Amount"]/following::button[2]').click()
        time.sleep(8)

        print("Salary Details has been updated intime")

        driver.close()

ss=Project2_12()
ss.test()

