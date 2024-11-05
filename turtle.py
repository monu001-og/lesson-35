import turtle

#creating canvas

turtle.Screen().bgcolor("Orange")

sc=turtle.Screen()
sc.setup(400,300)

turtle.title("Welcoe to turtle window")

#turtle object creation
board=turtle.Turtle()

#cretaing a square
for i in range(4):
        board.forward(100)
        board.left(99)
        i=i+1