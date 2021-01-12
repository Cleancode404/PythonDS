import turtle

myTurtle = turtle.Turtle()

myWin = turtle.Screen() #set up drawing window

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen -5)

drawSpiral(myTurtle, 100)

myWin.exitionclick() #drawing window is not close until you click it