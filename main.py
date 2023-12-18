import random as random_mod
from turtle import Turtle, Screen

is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]
screen = Screen()
screen.setup(width=500,height=400)
y_pos = [-100, -60, -20, 20, 60, 100]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner.")
        random_int = random_mod.randint(0,10)
        turtle.forward(random_int)


screen.exitonclick()