from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_num)
print(dice_images[dice_num])

# the module randint will print number from 1 to 6 inclusive,
# and it will become the number for index.
# Since index start with 0 not 1 so that we need to decrease the number by 1 or change the randint ( 0, 5)
# Or it will get the bug occasionally when reach index 6 (the is no index 6 in the dice_images

