import smtplib
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,bot_email : str, bot_password: str ):

        self.bot_email = bot_email
        self.bot_password = bot_password

    def send_mail(self, message : str, email : str):
        self.email_address = email
        self.message = message

        with smtplib.SMTP('smtp.gmail.com',587) as connection:

            connection.starttls()  # TLS = Transport layer security, it is encryption for the connection
            connection.login(user=self.bot_email, password=self.bot_password)
            connection.sendmail(from_addr=self.bot_email,
                                to_addrs=self.email_address,
                                msg=f'Subject: Flight Deals! \n\n{self.message}'
                                )


    def message_from_dict(self, message : dict):
        self.formated_message = ""
        for i in message:
            flyfrom = message[i]["flyfrom"]
            flyto = message[i]["flyto"]
            price = message[i]["price"]
            self.formated_message += f'Fly from {flyfrom} to {flyto} for {price} NZD!\n'
        print(self.formated_message)
        return self.formated_message
