import turtle

def draw_square(some_turtle):
    for i in range (0,4):
        some_turtle.forward(70)
        some_turtle.right(90)

def draw_flower():
    window = turtle.Screen()
    grade = 0;
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(500)
    for i in range (1,73):
        draw_square(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(200)

    window.exitonclick()

draw_flower()

