from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class HousingBot:

    def __init__(self, url, area_name):
        self.area_name = area_name
        self.data_pack = {}
        self.FORM_URL = 'https://forms.gle/QgtVeJaZqz5TQJzf6'
        self.headers = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }

        self.html = requests.get(url=url, headers=self.headers).text
        self.soup = BeautifulSoup(self.html, "html.parser")

        # Finds class that has the tern super fetures within a longer string and then deleted those divs
        for div in self.soup.find_all(class_=re.compile(r'^listing-tile-super-featured')):
            # print(div.text, 'banana')
            div.decompose()

        for div in self.soup.find_all(class_='showcase'):
            # print(div.text, 'banana')
            div.decompose()

    def gethousing(self):

        self.all_price = self.soup.find_all(class_='md:w-1/2 text-navy-500 text-right leading-tight')

        self.all_link = self.soup.select(selector="div > div > div > div > div > div > div > a")
        self.all_address = self.soup.find_all(name="h3")

        self.PriceList = [price.getText() for price in self.all_price]
        self.LinkList = [link.get("href") for link in self.all_link][
                        ::2]  # by default this returns duplicates, [::2] reads every 2nd in the list
        self.AddressList = [Address.getText() for Address in self.all_address]

        # print(self.AddressList)
        # print(self.LinkList)
        # print(self.PriceList)
        # print(len(self.AddressList))
        # print(len(self.LinkList))
        # print(len(self.PriceList))

        if len(self.PriceList) == len(self.AddressList) == len(self.LinkList):
            print("Scraping appears successful")
            i = 0
            for address in self.AddressList:
                self.data_pack[address] = {
                    'price': self.PriceList[i],
                    'link': self.LinkList[i],
                    'area': self.area_name
                }
                i += 1
            return self.data_pack
        else:
            print("ERROR: Scraping was not successful")
            pass


class DataEntry:

    def __init__(self, *args: dict, form_url: str, chrome_driver: str):

        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.get(form_url)

        for property_dict in args:
            print(property_dict)
            for property in property_dict:
                self.address = property[5:-3]
                self.price = property_dict[property]['price']
                self.link = f"https://www.realestate.co.nz{property_dict[property]['link']}"
                self.area = property_dict[property]['area']

                self.input_area = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div')
                self.input_address = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div')
                self.input_address = self.input_address
                self.input_price = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div')
                self.input_link = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div')
                self.submit_button = self.driver.find_element_by_xpath(
                    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

                ActionChains(self.driver).send_keys_to_element(self.input_area, self.area).perform()
                ActionChains(self.driver).send_keys_to_element(self.input_address, self.address).perform()
                ActionChains(self.driver).send_keys_to_element(self.input_price, self.price).perform()
                ActionChains(self.driver).send_keys_to_element(self.input_link, self.link).perform()
                self.submit_button.click()
                self.back_button = self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                self.back_button.click()
