import turtle
import pandas

screen = turtle.Screen()
t = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(data.state)
state_list = data.state.to_list()
print(state_list)
screen.tracer(0)
guessed_states = []

while len(guessed_states) < len(state_list):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(state_list)} States Correct", prompt="What's another state?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.penup()
        t.hideturtle()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state, font=("calibre", 11))
        screen.update()
    print(guessed_states)

