#-----------------SETUP----------------------------------#
import smtplib
import datetime as dt
import random

# #--------------------Date/Time Module-----------------------------#
now = dt.datetime.now()
print(now)
year = now.year
date_of_birth = dt.datetime(year=1994, month= 9, day = 23) # this creates a date time object with those values

#-------------------------Quote Listerizer-----------------------#
with open('quotes.txt', 'r') as quotes:
    quote_list = quotes.readlines()
    quote_of_the_day = random.choice(quote_list)
    print (quote_of_the_day)

if now.weekday() == 0: #IF it is a monday (0th day of the week)
# --------------------Sending an Email-----------------------------#
    my_email = "rickysemailforpythonprojects@gmail.com"
    with smtplib.SMTP('smtp.gmail.com',
                      587) as connection:  # new object SMTP from the smtplib library, the smtp.gmail.com is the service we are connecting too.
        connection.starttls()  # TLS = Transport layer security, it is encryption for the connection
        connection.login(user=my_email, password='abcd1234()###')
        connection.sendmail(from_addr=my_email,
                            to_addrs='Ricky.j.millar@gmail.com',
                            msg=f'Subject: Quote Of the Day, Bro.\n\n{quote_of_the_day}')
