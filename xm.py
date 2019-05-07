import turtle 

painter = turtle.Turtle()

painter.pensize(3)
painter.speed(1)


#Draw face

painter.color('black', 'black')
painter.pendown()
painter.circle(100)


#Draw right ear

painter.penup()
painter.setx(50)
painter.sety(185)
painter.pendown()

painter.begin_fill()
painter.right(90)
painter.circle(30, -260)
painter.end_fill()


#Draw left ear

painter.penup()
painter.setx(-50)
painter.sety(185)
painter.pendown()

painter.left(170)
painter.begin_fill()
painter.right(90)
painter.circle(30, 260)
painter.end_fill()


#Draw left eye

painter.penup()
painter.setx(-40)
painter.sety(90)
painter.pendown()

painter.begin_fill()
painter.circle(30)
painter.end_fill()

painter.left(10)
painter.penup()
painter.setx(-30)
painter.sety(110)
painter.pendown()

painter.color('white', 'white')
painter.begin_fill()
painter.circle(15)
painter.end_fill()

painter.penup()
painter.setx(-30)
painter.sety(115)
painter.pendown()

painter.color('black', 'black')
painter.begin_fill()
painter.circle(5)
painter.end_fill()


#Draw right eye

painter.penup()
painter.setx(40)
painter.sety(90)
painter.pendown()

painter.color('black', 'black')
painter.begin_fill()
painter.circle(30)
painter.end_fill()

painter.penup()
painter.setx(30)
painter.sety(110)
painter.pendown()

painter.color('white', 'white')
painter.begin_fill()
painter.circle(15)
painter.end_fill()

painter.penup()
painter.setx(30)
painter.sety(115)
painter.pendown()

painter.color('black', 'black')
painter.begin_fill()
painter.circle(5)
painter.end_fill()


#Draw mouth and nose

painter.color('black', 'black')
painter.penup()
painter.setx(0)
painter.sety(50)
painter.pendown()

painter.begin_fill()
painter.circle(10)
painter.end_fill()

painter.right(90)
painter.circle(20, 180)

painter.penup()
painter.setx(0)
painter.sety(50)
painter.pendown()

painter.circle(20, -180)

turtle.done()