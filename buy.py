from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from seleniumrequests import Chrome
import time



driver_path = './chromedriver'
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(30)


url = 'https://www.trplus.com.tw/memberGetMyCoupon'
driver.get(url)
to_go = str(input("go?"))
if to_go == 'go':
    while True:
        try:
            get_goods = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div/div/div/div[1]/a[1]')
            get_goods.click()
            time.sleep(0.1)
            
            try:
                WebDriverWait(driver, 0.5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except TimeoutException:
                print("no alert")
            driver.refresh()
            driver.implicitly_wait(30)
        except:
            print('刷新')
            try:
                WebDriverWait(driver, 0.5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
                driver.refresh()
                driver.implicitly_wait(30)
            except TimeoutException:
                print("no alert")

        