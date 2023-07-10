
# PyMailSender: Secure Email Sending with Gmail SMTP

This project is a Python script that demonstrates how to send emails using the Gmail SMTP server. It uses the `smtplib` library and supports secure email transmission using SSL.

## Prerequisites
Before running the script, make sure you have the following:
- Python 3 installed on your system
- Required Python packages: `email`, `ssl`, and `smtplib`
- Gmail account with "Less Secure Apps" enabled or an app password generated

## Installation
    1. Clone the repository to your local machine
    2. Navigate to the project directory
    3. Install the required dependencies using pip

## Configuration
    1. Open the `app_pass.py` and `email_automation.py` files.
    2. Replace the placeholders with your Gmail email address in `email_automation.py` file
        `email_sender = 'your-email@gmail.com'`
        `email_receiver = 'recipient-email@example.com'`
    3. Replace the place holder with your app password in `app_pass.py`
        `email_password = 'your-app-password'` 
    4. Save and close the file.

## Usage
To send an email follow these steps:

    1. Open the `email_automation.py` file.
    2. Modify the subject and body of the email according to your needs.
      `subject = "subject of the email"`
      `body = """The message you want to send"""`
    3. Save and close the file.
    4. Run the Script
The script will establish a secure connection to the Gmail SMTP server and send the email using the provided credentials.








# FAQ
### How to setup app password in Gmail?
Please follow the instructions in the following link and you will be able to setup an app_password:

`https://support.google.com/mail/answer/185833?hl=en`
