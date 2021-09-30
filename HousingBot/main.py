from housingbot import HousingBot, DataEntry

QUEENSTOWN_HOUSING_URL = 'https://www.realestate.co.nz/residential/sale/central-otago-lakes-district/queenstown?maxp=500000&scat=1%2C9%2C2%2C4%2C8%2C7%2C6%2C5%2C3'
WANAKA_HOUSING_URL = 'https://www.realestate.co.nz/residential/sale/central-otago-lakes-district/wanaka?maxp=500000&scat=1%2C9%2C2%2C4%2C8%2C7%2C6%2C5%2C3'
FORM_URL = 'https://docs.google.com/forms/d/1MtuMm3GpAd46STtsgFlEXhbpLdw-URvJLa2R1MEI1hE/edit'
CHROME_DRIVER_PATH = "D:\Development\chromedriver_win32\chromedriver.exe"

queens_bot = HousingBot(QUEENSTOWN_HOUSING_URL, "Queenstown")
queens_data = queens_bot.gethousing()

wanaka_bot = HousingBot(WANAKA_HOUSING_URL, "Wanaka")
wanaka_data = wanaka_bot.gethousing()

DataEntry(wanaka_data, queens_data, form_url=FORM_URL, chrome_driver=CHROME_DRIVER_PATH)
