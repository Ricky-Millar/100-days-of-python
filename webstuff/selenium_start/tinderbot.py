from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

CHROME_DRIVER_PATH = "D:\Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
driver.get("https://tinder.com/")

login_button = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()
time.sleep(1)
facebook_login_one = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login_one.click()
time.sleep(1)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

facebook_email = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
facebook_password = driver.find_element_by_xpath('//*[@id="pass"]')
facebook_login_two = driver.find_element_by_xpath('//*[@id="loginbutton"]')

facebook_email.send_keys('ricky.j.millar@gmail.com')
facebook_password.send_keys('FacTal1sker1994')
facebook_login_two.click()

driver.switch_to.window(base_window)

time.sleep(5)
try:
    allow_location = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]/span')
    allow_location.click()
except :
    pass
try:
    block_notifications = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[2]/span')
    block_notifications.click()
except:
    pass
time.sleep(7)
i=0
while i < 10:
    try:
        print('banana')
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.LEFT)
        print('melon')
        i += 1
        time.sleep(1)
    except:
        time.sleep(2)
        pass



