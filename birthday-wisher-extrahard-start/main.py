##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "randomunboxing.id@gmail.com"
MY_PASSWORD = "gvuzzkclwsqhdsxb"

data = pandas.read_csv("birthdays.csv")

today = dt.date.today()
today_month = today.month
today_day = today.day

# we also can create a dict from dataframe. The key is a tuple and value is the data row
# today_tuple = (today_month, today_day)
# birthday_dict = {(data.row["month"], data.row["day"]): data.row for (index, data) in data.iterrows()}

match = data[(data.month == today_month) & (data.day == today_day)]

print(match)
print(type(match))

if len(match) > 0:
    for index, row in match.iterrows():
        name = row["name"]
        email = row["email"]
        number_of_letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{number_of_letter}.txt") as wish_letter:
            chosen_letter = wish_letter.read()
            new_letter = chosen_letter.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: HAPPY BIRTHDAY!!🎉\n\n{new_letter}".encode("utf-8"))
            print("SENT")






