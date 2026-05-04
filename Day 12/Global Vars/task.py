# Modifying Global Scope


enemies = 1

def increase_enemies1():
    global enemies
    enemies += 1
    print(f"this is the {enemies}")

# the second way of doing an actions from global scope

def increase_enemies(enemy):
    print(f"enemies inside function before return: {enemies}")
    return enemy + 1

increase_enemies1()
enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

