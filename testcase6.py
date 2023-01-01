from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Project2_6():
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

#xpath to myinfo details
        driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/viewMyDetails"]').click()
        time.sleep(3)

#xpath to contact details
        driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/contactDetails/empNumber/7"]').click()
        time.sleep(4)

#xpath to street1
        street1_element=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input')
        street1_element.send_keys(Keys.CONTROL, 'a')
        street1_element.send_keys(Keys.BACKSPACE)
        street1_element.send_keys("2nd ward")
        time.sleep(4)


        street2_eleement=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input')
        street2_eleement.send_keys(Keys.CONTROL, 'a')
        street2_eleement.send_keys(Keys.BACKSPACE)
        street2_eleement.send_keys("medar street")
        time.sleep(4)


        City_eleement=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input')
        City_eleement.send_keys(Keys.CONTROL, 'a')
        City_eleement.send_keys(Keys.BACKSPACE)
        City_eleement.send_keys("karanataka")
        time.sleep(4)


        state_eleemnt=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input')
        state_eleemnt.send_keys(Keys.CONTROL, 'a')
        state_eleemnt.send_keys(Keys.BACKSPACE)
        state_eleemnt.send_keys("bangalore")
        time.sleep(4)


        zip_element=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input')
        zip_element.send_keys(Keys.CONTROL, 'a')
        zip_element.send_keys(Keys.BACKSPACE)
        zip_element.send_keys("583124")
        time.sleep(4)


        driver.find_element(By.XPATH, '//label[text()="Country"]/following::div[3]').click()
        time.sleep(4)

        driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="India"][1]').click()
        time.sleep(4)


        homeph_number=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input')
        homeph_number.send_keys(Keys.CONTROL, 'a')
        homeph_number.send_keys(Keys.BACKSPACE)
        homeph_number.send_keys("9108805560")
        time.sleep(4)


        mobile_xpath=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input')
        mobile_xpath.send_keys(Keys.CONTROL, 'a')
        mobile_xpath.send_keys(Keys.BACKSPACE)
        mobile_xpath.send_keys("9108805560")
        time.sleep(4)


        otheremail_id=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input')
        otheremail_id.send_keys(Keys.CONTROL, 'a')
        otheremail_id.send_keys(Keys.BACKSPACE)
        otheremail_id.send_keys("karibasavaraj77@gmail.com")
        time.sleep(4)

        driver.find_element(By.XPATH,'//label[text()="Work Email"]/following::button[1]').click()
        time.sleep(5)

        print("Contact Details of the employee has been updated successfully")

        driver.close()
ss=Project2_6()
ss.test()


