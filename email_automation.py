from email.message import EmailMessage  # Importing the EmailMessage class from the email.message module
from app_pass import app_password  # Importing the app_password from a separate file
import ssl  # Importing the ssl module for secure connections
import smtplib  # Importing the smtplib module for sending emails

sender_email = ' '  # insert the email address of the sender
password = app_password  # The application password used for authentication
receiver_email = ' '  # inser the email address of the receiver

subject = " "  # insert the subject of the email

body = """   """ # insert the he body of the email

msg = EmailMessage()  # Creating an instance of the EmailMessage class
msg['From'] = sender_email  # Setting the 'From' address of the email
msg['To'] = receiver_email  # Setting the 'To' address of the email
msg['Subject'] = subject  # Setting the subject of the email
msg.set_content(body)  # Setting the body content of the email

context = ssl.create_default_context()  # Creating a default SSL context

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Creating an SMTP_SSL instance for secure email transmission using Gmail SMTP server
    smtp.login(sender_email, password)  # Logging in to the SMTP server
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    # Sending the email by providing the sender, receiver, and the email content as a string

