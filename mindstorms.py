import turtle

def draw_square(some_turtle):
    for i in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)
    

def drwa_trinagle(some_turtle):    
    for i in range (0,3):
        some_turtle.backward(200)
        some_turtle.left(120)

def drwa_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    jhon = turtle.Turtle()
    jhon.shape("arrow")
    jhon.color("green")
    drwa_trinagle(jhon)
    
    window.exitonclick()

def draw_square_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    grade = 0;
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_square_circle()
