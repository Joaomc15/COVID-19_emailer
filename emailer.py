import smtplib
import config

def send_email(subject, msg, mail_list):
    # try: 
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    message = f"""Subject: {subject}\n\n{msg}"""
    
    # message = 'Subject: {}\n\n'.format(subject, msg)
    for item in mail_list:

        server.sendmail(config.EMAIL_ADDRESS, item, message)
        # server.sendmail(config.MAIL_LIST, mail_list, message)
        print(f'success, email sent to {item}')

    # except :
    #     print("email failed")
        
    server.quit()
    