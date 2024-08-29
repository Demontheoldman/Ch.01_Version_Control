'''
1.0 Jedi Training (17pts)  Name:________________


1. Define Forking (1pt): 

2. Define Cloning (1pt): 

3. Define Branching (1pt):

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt):

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')

tina.speed(50)
tommy.speed(50)

tommy.pendown()
tommy.begin_fill()
tommy.color('cyan')
tommy.goto(200,200)
tommy.pendown()
tommy.goto(200,-200)
tommy.goto(-200,-200)
tommy.goto(-200,200)
tommy.goto(200,200)
tommy.penup()
tommy.end_fill()

#tina make the circle for the flag

tina.penup()
tina.begin_fill()
tina.color('red')
tina.goto(0,0)
tina.pendown()
tina.circle(50)
tina.penup()
tina.end_fill()

#tommy is making the square for the flag

tommy.penup()

tommy.color('green')
tommy.goto(-100,120)
tommy.begin_fill()
tommy.pendown()
tommy.forward(200)
tommy.right(90)
tommy.forward(150)
tommy.right(90)
tommy.forward(200)
tommy.right(90)
tommy.forward(150)
tommy.end_fill()

#tommy makes the white line for the flag 

tommy.left(90)
tommy.forward(10)
tommy.left(90)
tommy.forward(300)
tommy.left(90)






yoda.write('Sign Your Name Here',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
