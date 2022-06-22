import turtle
import random
import time

window = turtle.Screen()
window.title("DVD")
window.bgcolor("black")
window.setup(width=700, height=700)
window.tracer(0)
window.addshape('dvdlogored.gif')
window.addshape('dvdlogoblue.gif')
window.addshape('dvdlogoyellow.gif')
window.addshape('dvdlogogreen.gif')
window.addshape('dvdlogoorange.gif')
window.addshape('dvdlogopink.gif')
window.addshape('dvdlogoteal.gif')
window.addshape('dvdlogowhite.gif')
window.addshape('dvdlogopurple.gif')
#window.addshape()

box = turtle.Turtle()
box.speed(0)
box.shape("dvdlogored.gif")
box.penup()
box.goto(0,0)
box.dx = 5
box.dy = 5
box.shapesize(5)
print(box.dx)
print(box.dy)

#testbox = turtle.Turtle()
#testbox.shape('square')
#testbox.penup()
#testbox.goto(100, 0)
#testbox.color('green')


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']
shapes = ['dvdlogoblue.gif', 'dvdlogored.gif', 'dvdlogoyellow.gif', 'dvdlogoorange.gif', 'dvdlogogreen.gif', 'dvdlogoteal.gif', 'dvdlogopurple.gif', 'dvdlogopink.gif', 'dvdlogowhite.gif' ]
def reject_sample(shapes):
    while True:
        choice = random.choice(shapes)
        if choice != box.shape():
            box.shape(choice)
            break

def collision(box, testbox):
    return abs(box.xcor() - testbox.xcor()) < 10 and abs(box.ycor() - testbox.ycor() < 10)
while True:
    time.sleep(1/240)
    window.update()

    box.setx(box.xcor() + box.dx)
    box.sety(box.ycor() + box.dy)
    t = random.choice(colors)

    #if collision(box, testbox):
        #print(testbox.pos())
        #print("hit", box.distance(testbox))
        #box.setx(box.xcor())
        #box.sety(box.ycor())
        #box.dx *= -1
        #box.dy *= -1

    if box.ycor() > 280:
        box.sety(280)
        box.dy *= -1
        reject_sample(shapes)

    if box.ycor() < -280:
        box.sety(-280)
        box.dy *= -1
        reject_sample(shapes)

    if box.xcor() > 200:
        box.setx(200)
        box.dx *= -1
        reject_sample(shapes)

    if box.xcor() < -200:
        box.setx(-200)
        box.dx *= -1
        reject_sample(shapes)
