from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# EASY = 0.1
# NORMAL = 0.08
# HARD = 0.06

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Snake Game#")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

# if screen.textinput(title="CHOOSE DIFFICULTY LEVEL", prompt="NORMAL / HARD").lower() == normal:
#     speed = NORMAL
# else:
#     speed = HARD

# TO BE WORKED ON^


game = True
while game:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.new_foodini()
        scoreboard.increase_score()
        snake.extend()

    # Collision with wall
    if snake.head.xcor() > 430 or snake.head.xcor() < -450 or snake.head.ycor() > 430 or snake.head.ycor() < -450:
        game = False
        scoreboard.game_over()

    # Collision with tail
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            game = False
            scoreboard.game_over()


screen.exitonclick()
