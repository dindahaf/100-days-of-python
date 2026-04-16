from art import logo

print(logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bidder(participants):
    find_max = 0
    winner_name = ""

    # max(participants, key=participants.get)

    for name in participants:
        participants_amount = participants[name]
        if participants_amount > find_max:
            find_max = participants_amount
            winner_name = name
    print(f"The winner is {winner_name} with a bid of ${find_max}.")

new_participants = True
participants = {}
while new_participants:
    name = input("What is your name? ").lower()
    price = int(input("What is your bid? $"))

    participants[name] = price
    print(participants)

    restart = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if restart == "no":
        new_participants = False
        find_highest_bidder(participants)
    else:
        print("\n" * 100)



