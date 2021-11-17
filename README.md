# Turtle_roadcross_OOP

the task is to create a game , in which a turtle has to cross a road from bottom to the top of the screen , while cars(objects) keep on moving from right to left like a road. 
if the turtle reaches the top , the score is increased by 1 , and if it collides with any car then it's game over.

the project is divided into 3 classes - Player , scoreboard and car generator.

## Class 1 - Player
a. we start by importing the Turtle module from turtle class , and defining our constants ie Starting position , move distance and finish line coordinates.
b. we initialise the class 'Player' with superclass 'turtle' and determine the attributes such as shape and starting position.
c. we create 2 functions , one for moving the turtle forward and second one for resetting the turtle.

## Class 2 - Scoreboard
a. we start by importing the Turtle module from turtle class , and defining our constants ie Font and alignment.
b. we initialise the class 'Player' with superclass 'turtle' and determine the attributes such as shape , starting position and include the function to write the score.
c. we create 3 functions , one for writing the score , second for increasing the score and third one when it's game over. 

## Class 3 - Car Manager
a. we start by importing the Turtle module from turtle class and randrange , randint and choice module from random class.
b. we define these constants 'colors' , 'starting move distance' and 'move increment' . 
c. we initialise the class with a blank list named 'cars' and an attribute named 'car_speed' that is equal to constant 'starting move distance' . 
d. we define 3 functions inside this class. 
    Function A ) make_cars - we create a new object 'new_car' that is an 'turtle' object and define it's attributes such as shape , starting position and color.
    at the end , we append this object to the class 'cars' . 
    NOTE : the creation of objects was too fast , so to slow down the process we declared a new variable 'random_number' , that generates a random number between 1 and 6 and 
    if the number generated is 1 , then only the object is created. 
    
    Function B ) move_cars - this function iterates in the 'cars' list and move all items forward by the variable 'car_speed' . 
    
    Function C ) increase_level - this function increases the variable 'car_speed' by 'car_speed' + constant 'Move increment' . It increases the speed of movement of the cars.
    
## Main File 
a. we import the necessary modules i.e time , randint , Screen , Player , Car manager and Scoreboard. 
b. we start by creating an object named 'screen' that is an object of 'Screen' module of 'turtle' class.
c. we set the screen up by setting it's width as 600 , height as 600 and by turning the tracer off.
d. we create separate objects of the classes mentioned above.
e. we activate the listen function of the screen , and map the up key to move_turtle function of the player class.
f. we declare a variable 'game is on' to start and stop the game.
g. we start a while loop , which keeps on running till 'game is on' is true. 
    i) inside this while loop , we call the function to create cars and then to move cars from the carmanager class.
    ii) we create a for loop , that iterates over 'cars' list in car manager class that detects collision inbetween the turtle by measuring the distance inbetween
    the current object in the for loop and the turtle. If the distance is less than 20 pixels , then it turns the variable 'game is on' to False so that while loop will end 
    and reset the turtle position and display the final scoreboard.
    iii) if no collision is detected and the player reaches the top of the screen , that is ycoordinates of 280 , then we call increase_score function from scoreboard class , 
    increase level function from car manager class and reset position function from turtle class to increase the difficulty level of the game.
    
h. we activate the 'exitonclick' function of the screen object so that the program doesn't automatically end.
