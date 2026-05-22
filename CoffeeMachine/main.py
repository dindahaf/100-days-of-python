MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 250,
    "coffee": 100,
}

# TODO 1. Asking the user what “ What would you like? (espresso/latte/cappuccino): ” including the secrete prompt called "report"
# TODO 2. Computer checks the user input and decide what to do next
# TODO 3. There are some possibilities:
## a. turn off the coffee machine by entering "off" to the prompt and the computer should end the execution
## b. print "report" prompt to see the stock of all the ingredients

def available_ingredients():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}gr")


def calculate_money():
    """ return the total of money that user's inserted"""
    print("Please insert coins.")
    total_money = float(input("How many quarters? ")) * 0.25
    total_money += float(input("How many dimes? ")) * 0.10
    total_money += float(input("How many nickels? ")) * 0.05
    total_money += float(input("How many pennies? ")) * 0.01
    return total_money

def make_coffee(order, user_money):
    """Return True if the order is in the menu and the user_money is sufficient. Otherwise, return False."""
    if order in MENU and user_money > MENU[order]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def check_resources(order_ingredients):
    """ return True if the ingredients to make coffee is sufficient. Otherwise, return False."""
    # Using for loop to check all the ingredients without calling it one by one manually
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def reduce_ingredients(coffee_type_ingredients):
    """do not need to check whether is there any resources[item] or not in the coffee_type["ingredients"][item]
     because it is only reduce item(ingredients) in the coffee_type"""
    for item in coffee_type_ingredients:
            resources[item] -= coffee_type_ingredients[item]

def calculate_change(user_money, order):
    """return change of user's money"""
    change = user_money - MENU[order]["cost"]
    return change


is_running = True
machine_money = 0
while is_running:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if response == "report":
        available_ingredients()
        print(f"Money: ${machine_money}")
    elif response == "off":
        is_running = False
    else:
        if check_resources(MENU[response]["ingredients"]):
            coins= calculate_money()
            if make_coffee(response, coins): # will be extract into two of separated parts
                machine_money += round(MENU[response]["cost"], 2)
                print("yes money is enough, we will reduce the ingredients")
                reduce_ingredients(MENU[response]["ingredients"])
                user_change = round(calculate_change(coins, response), 2)
                print(f"Here is ${user_change} in change")
                print(f"Here is your {response} ☕ Enjoy!")


## c. if the user ask to make one of the available coffee, then the computer should:
## - check what kind of drink that the user wants
## - check if the ingredients are sufficient, if no then print "Sorry there is not enough water." if yes, then:
## - ask the user to insert the coin. ask the user "How many quarters?", "How many dimes?", "How many nickles?", "How many pennies?"
## - calculate the coins that have inserted based on the coins' rules. It is required math calculation (add, subtract, and multiplication)
## - check if the coins are enough or not, if no then print "Sorry that's not enough money. Money refunded
## - if the coins are enough:
## - Making the coffee by reducing the ingredients and calculate the change then displaying the change and deliver the coffee to the user
## - the change should be rounded by 2 decimal points
## There are a variable called money that save amount of money that the coffee machine's revenue.


