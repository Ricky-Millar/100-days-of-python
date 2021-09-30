#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_data, flight_search, notification_manager, data_manager
RICKYS_SHEETY_ENDPOINT = 'https://api.sheety.co/5b1e332caa8c97f81eb2d0f576cdf4d9/flightDeals/prices'
SEARCH_API_KEY =  {
            "apikey": "CFh_nU3LPmJvuOrqjndk5SxSAhXUXdhC"
        }
bot_email = "rickysemailforpythonprojects@gmail.com"
bot_password = 'abcd1234()###'
rickys_email = 'ricky.j.millar@gmail.com'


#-------------------#initialise classes#----------------------#
search = flight_search.FlightSearch(api_key = SEARCH_API_KEY) #initialise a flight searchign object
email_bot = notification_manager.NotificationManager(bot_email=bot_email, bot_password=bot_password)
sheety = data_manager.DataManager(endpoint=RICKYS_SHEETY_ENDPOINT) #initialise sheety object for handing google sheet

def new_user():
    first_name = input('What is your first name?')
    last_name = input('What is your last name?')
    email_not_match = True

    while email_not_match:
        email_1 = input('What is your email?')
        email_2 = input('Confirm email')
        if email_1 == email_2:
            email_not_match = False
            sheety.new_user(first_name,last_name,email_1)
            email_1 = ''
            email_2 = ''
        else:
            print('Emails did not match, try again.')
            email_1 = ''
            email_2 = ''

new_user()






# rickys_formatter = flight_data.FlightData(data_manager_object=sheety, flight_search_object=search) # initialist the object that combines the sheet data and formats it to be used for search stuff
#
# message = rickys_formatter.format_and_search() #Takes
#
# formatted_message = email_bot.message_from_dict(message=message)
# email_bot.send_mail(message=formatted_message, email=rickys_email)
#



# search.generate_abriviations(sheety_object=rickys_sheety) # create the abriviations of the airports and put them in the google sheet

