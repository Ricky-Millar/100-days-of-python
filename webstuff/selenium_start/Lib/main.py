from selenium import webdriver
CHROME_DRIVER_PATH = "D:\Development\chromedriver_win32\chromedriver.exe"
events = {}

driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
driver.get("https://www.python.org/")

#This alwas works! woop, there are tonnes of way to search in selenuim but this one is fullproof
text_bit = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
num_of_events = int((text_bit.text.count("\n") + 1)/2) #retreives list of events then counts the lines (each event takes 2 lines)

for i in range(num_of_events):
    list_number = i+1
    date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{list_number}]/time').text
    name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{list_number}]/a').text
    events[i] = { 'name': name,
                  'date': date}
print(events)


driver.quit()