from InternetSpeedTwitterBot import internetspeedtwitterBot
import time

CHROME_DRIVER_PATH = 'D:\Development\chromedriver_win32\chromedriver.exe'
email = '@RickyMIllar3'
password = 'twITal1sker1994'

bot = internetspeedtwitterBot(CHROME_DRIVER_PATH, email,password)

Data = bot.get_internet_speed()

message = f"Hey {Data['provider']} my upload speed is {Data['up']}Mb/s and my download speed is {Data['down']}Mb/s. {Data['img_url']}"

bot2 = internetspeedtwitterBot(CHROME_DRIVER_PATH, email,password)


bot2.tweet_at_provider(message)