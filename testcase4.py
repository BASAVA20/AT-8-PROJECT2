from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_4():
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


        xpath_to_personal='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'
        print(driver.find_element(By.XPATH,xpath_to_personal).accessible_name)
        time.sleep(3)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a').accessible_name)
        time.sleep(2)


        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a').accessible_name)
        time.sleep(2)

        driver.close()

ss=Project2_4()
ss.test()