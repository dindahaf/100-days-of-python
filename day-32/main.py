# Learn about SMTP

# import smtplib
#
# my_email ="randomunboxing.id@gmail.com"
# password = "gvuzzkclwsqhdsxb"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr= my_email,
#         to_addrs="dindahaf@gmail.com",
#         msg="Subject:Hello\n\nThis is the body email"
#     )
#     print("Email sent successfully")

# Learn datetime module

# import datetime as dt
#
# now= dt.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
#
# date_of_birth = dt.datetime(year=1997, month=6, day=22, hour=4  )
# print(date_of_birth)

import random
import datetime as dt
import smtplib

MY_EMAIL ="randomunboxing.id@gmail.com"
MY_PASSWORD = "gvuzzkclwsqhdsxb"


now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:

        with open("quotes.txt", "r") as data:
            quotes = data.readlines()
            selected_quote = random.choice(quotes)

        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs="dindahaf@gmail.com",
            msg=f"Subject:Quote of the day\n\n{selected_quote}".encode("utf-8")
        )
        print("Email sent successfully")