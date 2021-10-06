import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

x_cord = 0
y_cord = 0
score = 0
user_gussed_states = []
while score < 50:
    answer_state = screen.textinput(title=f"Guess the state {score}/50", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if not data[data['state'] == answer_state].empty:

        user_guess = data[data['state'] == answer_state]
        x_cord = user_guess['x'].values[0]
        y_cord = user_guess['y'].values[0]
        user_guessed_state = user_guess['state'].values[0]
        # increase user score
        if user_guessed_state not in user_gussed_states:
            score += 1
        # add that state to gussed states so user cant score again
        user_gussed_states.append(user_guessed_state)

        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x_cord, y_cord)

        state_turtle.write(f"{answer_state}")

turtle.mainloop()
