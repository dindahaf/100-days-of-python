# There us bi Block Scope in Python!

# Variable within block scope can be accessible outside the scope
# Example in if, while loop, for loop (that has indentation and colon)

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)




