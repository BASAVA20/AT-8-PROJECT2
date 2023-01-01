from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_9():
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

        driver.find_element(By.XPATH,'//a[text()="Immigration"]/following::div[1]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("2022-04-12")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Job Title"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Account Assistant"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Job Category"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Craft Workers"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Sub Unit"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Administration"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Location"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="New York Sales Office"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Employment Status"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Full-Time Contract"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Employment Status"]/following::div[7]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input').send_keys("2022-04-20")
        time.sleep(4)

        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input').send_keys("2023-02-15")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Contract Details"]/following::button[1]').click()
        time.sleep(4)

        driver.close()

ss=Project2_9()
ss.test()
