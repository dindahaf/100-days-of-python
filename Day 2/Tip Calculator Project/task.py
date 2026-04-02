# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

print("Welcome to the tip calculator!")

# Because it will get str result so we have to convert it into number, and in this case, float data type will be more accurate because you rarely get bill with rounded number
bill = float(input("What was the total bill? $"))

# This is also happened with the tip and so on, change it into more accurate data type
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill

bill_per_person = float(bill_with_tip / people)
final_amoount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amoount}")

