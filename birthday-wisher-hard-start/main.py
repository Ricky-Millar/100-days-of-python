import pandas
import datetime as dt
import smtplib
import random

my_email = "rickysemailforpythonprojects@gmail.com"

letter_list = ['','','']
def randomletter():
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as file:
        letter = file.read()
    return letter



with open('birthdays.csv','r') as birthdays:
    birthdays_data_frame = pandas.read_csv(birthdays)
    birthdays_dict = birthdays_data_frame.to_dict()

for i in range(len(birthdays_dict['name'])):
    now = dt.datetime.now()
    if birthdays_dict['month'][i] == now.month and birthdays_dict['day'][i] == now.day:
        with smtplib.SMTP('smtp.gmail.com',587) as connection:  # new object SMTP from the smtplib library, the smtp.gmail.com is the service we are connecting too.
            custom_letter = randomletter().replace('[NAME]', birthdays_dict['name'][i])
            connection.starttls()  # TLS = Transport layer security, it is encryption for the connection
            connection.login(user=my_email, password='abcd1234()###')
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthdays_dict['email'][i],
                                msg=f'Subject: Happy Birthday!\n\n{custom_letter}'
                                )
            connection.sendmail(from_addr=my_email,
                                to_addrs='ricky.j.millar@gmail.com',
                                msg=f'Subject: Birthday Alert!\n\nIts {birthdays_dict["name"][i]}s birthday'
                                )
