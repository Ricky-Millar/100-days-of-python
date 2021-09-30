from bs4 import BeautifulSoup
import requests
import smtplib

bot_email = "rickysemailforpythonprojects@gmail.com"
bot_password = 'abcd1234()###'
rickys_email = 'ricky.j.millar@gmail.com'
# HTTP Headers that the site pulls from the browser
headers = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

threshold_price = 50

def send_email(final_price):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # TLS = Transport layer security, it is encryption for the connection
        connection.login(user=bot_email, password=bot_password)
        connection.sendmail(from_addr=bot_email,
                            to_addrs=rickys_email,
                            msg=f'Subject: CatanBot \n\nCatan price has dropped to ${final_price}'
                            )


# get raw html then convert it into a soupy object of the raw text
response = requests.get(
    url='https://www.amazon.com/Catan-Studios-cantan2017/dp/B00U26V4VQ/ref=sr_1_2?dchild=1&keywords=catan&qid=1630787532&sr=8-2',
    headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# take the soupyboy and search for the specific ID of the price (taken from the amazon website) then convert to text and strip off the "$"
price = float(soup.find(name='span', id='priceblock_ourprice').getText().strip("$"))
print(price)

if price <= threshold_price:
    send_email(price)