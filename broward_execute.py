import emailer
from datetime import date, timedelta, time
import config
import datetime
from time import sleep
import test

def run():
    date = datetime.date.today()
    today = (date.today()).strftime('%d %B %Y')
    now = datetime.datetime.now()
    time = f'{now.hour}:{now.minute}:{now.second}'


    # updates = deploy.request()
    mail_list = config.MAIL_LIST_Broward


    subject = f'{date} Broward COVID-19 Updates'
    msg = f'''The latest COVID-19 statistics as of today, {today}, at {time} are as follows:\n\n'''
    #     \n\
    #      \n{updates} \
    #     \n\
    #     \nData from:\
    #     \nhttps://coronavirus.1point3acres.com/en\
    #     \n\nhttps://experience.arcgis.com/experience/96dd742462124fa0b38ddedb9b25e429 '''
    thanks = "\n\n\nData from:\
            \n\nhttps://www.bing.com/covid\
            \n\nhttps://experience.arcgis.com/experience/96dd742462124fa0b38ddedb9b25e429 "


    emailer.send_email(subject, msg + test.make_msg() + thanks, mail_list)
    

run()   

print(config.MAIL_LIST)