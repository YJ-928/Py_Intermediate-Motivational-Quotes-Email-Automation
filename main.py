# Motivational Quotes Automation App
import smtplib
import random
from datetime import datetime

# --------------------------- CONSTANTS ------------------------------ #
SENDER_EMAIL = "Your Email id Here"
SENDER_PASSWORD = "Your Email Password Here"
RECIEVER_EMAIL = "Recievers Email id here"

# -------------------------- Fetch Quotes ------------------------- #


def fetch_quotes():
    """Generates random quote from quote.txt file"""
    with open("quotes.txt") as file:
        for _ in range(random.randint(1, 102)):
            data = file.readline()

        return data


# ------------------- setting up Email-SMTP ------------------- #


def send_email():
    # you can put your host email smtp code here
    # i have given gmail smtp as an example here
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.starttls()
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECIEVER_EMAIL,
                            msg=f"Subject:Quote for the day\n\n{fetch_quotes()}")


# calling and executing the function
# first change the constants to correct Credentials
# or else you will get error's
send_email()
