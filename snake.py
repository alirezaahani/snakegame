from turtle import *
import random
import time

def up():
    snake.setheading(90)
def down():
    snake.setheading(270)
def left():
    snake.setheading(180)
def right():
    snake.setheading(0)

def move():
    if snake.heading() == 90:
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.heading() == 270:
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.heading() == 180:
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.heading() == 0:
        x = snake.xcor()
        snake.setx(x + 20)

segments = []

snake = Pen()
snake.shape('square')
snake.penup()
snake.goto(0,0)

food = Pen()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(100,0)

listen()

onkeypress(up, "Up")
onkeypress(down, "Down")
onkeypress(left, "Left")
onkeypress(right, "Right")

while True:
    snake.fd(1)
    if snake.distance(food) < 20:
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        food.goto(x,y)
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    
    for index in range(len(segments) - 1,0,-1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)
    
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)
    
    move()

    time.sleep(0.1)

mainloop()
