from selenium import webdriver
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class internetspeedtwitterBot():

    def __init__(self,driver_path, email, password):
        CHROME_DRIVER_PATH = driver_path
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.wait = WebDriverWait(driver=self.driver, timeout = 100)
        self.email = email
        self.password = password

        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()

        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[2]/div/div/ul[1]')))
        share = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/a[1]')
        share.click()
        user_id = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
        print (img_url, user_id, type(img_url), type(user_id))
        urllib.request.urlretrieve(img_url, f"{user_id}.jpg")

        img_url = f'https://www.speedtest.net/result/{user_id}.png'
        down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        ping = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        provider = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/a').text

        self.data_pack = {
            'down' : down,
            'up' : up,
            'ping': ping,
            'img_url' : img_url,
            'provider' : provider
        }
        print(self.data_pack)
        self.driver.quit()
        return self.data_pack


    def tweet_at_provider(self, message):
        self.driver.get("https://twitter.com/home")
        #log in
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')))
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        username.send_keys(self.email)
        password.send_keys(self.password)
        button.click()
        #use page
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]')))
        textbox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        textbox.send_keys(message)
        tweeter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweeter.click()






