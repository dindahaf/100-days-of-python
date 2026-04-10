# Day 6 - Reeborg Maze and Hurdles

## What I learned
Today I learned about loops and functions using the Reeborg online environment at reeborg.ca

## Challenge 1: Hurdles 1 to 4
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```

## Challenge 2: Maze
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
                        
while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
```