import os
import random
import math
import smtplib

OTP=random.randint(100000,999999)
print(OTP)
msg=OTP
print(type(msg)) 
email=smtplib.SMTP("smtp.gmail.com", 587)
email.starttls()
Email_id=input("Enter: ")
password="esbu hpqi szds iysm"
email.login('vt1733620@gmail.com',password)
email.sendmail("your OTP is", Email_id, str(msg))
d=int(input("Enter your otp: "))
if d==msg:
    print('verified')
else:
    print('not verified')