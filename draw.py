#Draw a shape with red and blue color

import turtle

pen = turtle.Pen()

##seting the speed
pen.speed(1)

##defining the width of the pen
pen.width(10)

##setting the color of the pen to red
pen.color('red')

#moving the pen to draw the expected shape
pen.right(-135)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)


##changing the color of the pen to blue
pen.color('blue')
pen.right(-90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)

pen.shape('blank')

##for making our graphicstay
turtle.done()
