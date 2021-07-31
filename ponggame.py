import turtle

#Window
wind = turtle.Screen()  #creating a window
wind.title('PYTHON PONG GAME')  #title os the window
wind.bgcolor('black')   #background colour of the window
wind.setup(width = 800, height = 600)  #dimensions of the window
wind.tracer(0)

#Slider bar A for first player
bar_A = turtle.Turtle()
bar_A.shape('square')
bar_A.color('white')
bar_A.shapesize(stretch_wid = 5, stretch_len = 1)
bar_A.penup()
bar_A.goto(-350, 0)

#Slider bar B for first player
bar_B = turtle.Turtle()
bar_B.shape('square')
bar_B.color('white')
bar_B.shapesize(stretch_wid = 5, stretch_len = 1)
bar_B.penup()
bar_B.goto(+350, 0)

#ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball_x = 0.3
ball_y = 0.3

#score
sboard = turtle.Turtle()
sboard.shape('square')
sboard.color('white')
sboard.penup()
sboard.hideturtle()
sboard.goto(0,260) 
sboard.write("Player A: 0 Player B: 0", align = 'center', font=("Courier", 24,'normal'))

score_a = 0
score_b = 0

#Functions
def bar_A_up():    #the y cordinate of the bar A will increase by 30
    y = bar_A.ycor()
    y += 30
    bar_A.sety(y)

def bar_A_down():    #the y cordinate of the bar A will decrease by 30
    y = bar_A.ycor()
    y -= 30
    bar_A.sety(y)

def bar_B_up():    #the y cordinate of the bar B will increase by 30
    y = bar_B.ycor()
    y += 30
    bar_B.sety(y)

def bar_B_down():    #the y cordinate of the bar B will decrease by 30
    y = bar_B.ycor()
    y -= 30
    bar_B.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(bar_A_up, 'w')
wind.onkeypress(bar_A_down, 's')
wind.onkeypress(bar_B_up, 'Up')
wind.onkeypress(bar_B_down, 'Down')

while True:
    wind.update()

    #Ball movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    #Border
    if ball.ycor() > 290:  #290 because the height of our screen is 600 and half of it is 300
        ball.sety(290)
        ball_y *= -1   #reverse the speed of the ball
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_y *= -1   #reverse the speed of the ball

    #score
    if ball.xcor() > 350:
        ball.goto(0,0)
        ball_x *= -1
        score_a += 1
        sboard.clear()
        sboard.write("Player A: {} Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
        
    elif ball.xcor() < -350:
        ball.goto(0, 0)
        ball_x *= -1
        score_b += 1
        sboard.clear()
        sboard.write("Player A: {} Player B: {}".format(score_a, score_b), align='center',
                     font=('Courier', 24, 'normal'))
        

    #Collision with the sliding bars
    if ball.xcor() < -340 and (ball.ycor() < bar_A.ycor() + 50) and (ball.ycor() > bar_A.ycor() - 50):
        ball_x *= -1
    elif ball.xcor() > 340 and (ball.ycor() < bar_B.ycor() + 50) and (ball.ycor() > bar_B.ycor() - 50):
        ball_x *= -1

    