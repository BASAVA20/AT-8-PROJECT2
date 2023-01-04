from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Project2_10():
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

        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Denvin")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Sub Unit"]/following::button[2]').click()
        time.sleep(6)

        driver.find_element(By.XPATH,'//div[text()="0360"]/following::div[1]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//a[text()="Immigration"]/following::div[1]').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input').send_keys("2022-12-12")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Termination Reason"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Contract Not Renewed"]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea').send_keys("Nil")
        time.sleep(4)
        driver.find_element(By.XPATH,'//label[text()="Note"]/following::button[2]').click()
        time.sleep(7)

        driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(7)
      # because if we terminate and again tried to reactivate the terminated user. It's displaying error that no records found. So, I've terminated and activated the same employee with in the same code

ss=Project2_10()
ss.test()

