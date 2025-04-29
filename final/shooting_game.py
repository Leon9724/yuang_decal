import os
os.chdir(os.path.dirname(__file__))

import turtle  
import random  
import time   

#screen
wn = turtle.Screen()
wn.title("Simple Shooting Game")
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)  # ! disable auto update screen 
 

# player
wn.register_shape("spaceship.gif")
player = turtle.Turtle()
player.shape("spaceship.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)

# bullet
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()
bullet.speed(0)
bullet_state = "ready"  # Ready to fire

#enemy
enemy = turtle.Turtle()
enemy.shape("turtle")
enemy.color("red")
enemy.shapesize(stretch_wid=2, stretch_len=2)
enemy.penup()
enemy.goto(random.randint(-280, 280), 250)

#score 
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

#timer
start_time = time.time()
time_limit = 30  # 30 seconds game

# player movement
def move_left():
    x = player.xcor()
    x -= 20
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# bullet hit
def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False

# Key binds 
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# game loop run
while True:
    wn.update()
    time.sleep(0.01)

    #  enemy move
    y = enemy.ycor()
    y -= .75
    enemy.sety(y)

    # Reset enemy 
    if y < -300:
        enemy.goto(random.randint(-280, 280), 250)

    # Move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += 20
        bullet.sety(y)

    # reset bullt
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet_state = "ready"

    # Check bullet hit
    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.goto(0, -400)  # Move bullet off screen
        enemy.goto(random.randint(-280, 280), 250)
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

    # check time_limit
    current_time = time.time()
    if current_time - start_time > time_limit:
        score_display.write(f"Time's up! Your score: {score}", align="center", font=("Arial", 24, "normal"))
        break

wn.mainloop()  
