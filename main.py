from turtle import Turtle,Screen
my_turtle = Turtle()
my_screen = Screen()


def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.forward(-10)
def move_left():
    my_turtle.left(10)

def move_right():
    my_turtle.right(10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()


my_screen.listen()
my_screen.onkey(key="w",fun=move_forwards)
my_screen.onkey(key="s",fun=move_backwards)
my_screen.onkey(key="a",fun=move_left)
my_screen.onkey(key="d",fun=move_right)
my_screen.onkey(key="c",fun=clear)
my_screen.exitonclick()