import turtle

window = turtle.Screen()
window.bgcolor('red')

def draw_square():
    brad = turtle.Turtle()

    brad.shape("classic")
    brad.color("yellow")
    brad.speed("fastest")

    for j in range(40):
        brad.right(10)    
        
        for i in range(4):
            brad.forward(100)
            brad.right(90)

    brad.speed("slow")
    brad.right(50)
    brad.forward(300)

draw_square()


window.exitonclick()