try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a numerical response, such as 16.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"Sorry, You can not drive at age {age}.")
