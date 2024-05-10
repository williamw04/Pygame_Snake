# Game Documentation
In this docuementation I will explain the process of creating the game. I will provide insight 
into techniques that were utilized and an explaination of each component of the program.

## Concepts

### Enumerations 
``` python
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
```
Enumerations (enums) in Python are used to assign constants or unique values to symbolic names. 
The purpose of enumerations is to enhance readability, maintainability, and make it easier to 
work with a fixed set of values. In this case, we define a class Direction used to represent 
possible directions the snake can face.


### namedtuple from collections
``` python 
Point = namedtuple('Point', 'x, y') 
```
namedtuple is a factory function, meaning it's a special kind of function that creates 
instances of objects. In object-oriented programming, it's a design pattern used to 
simplify the process of creating objects. namedtuple is specifically designed to create 
tuples with custom labels for each element. In the example provided, we define a Point namedtuple, 
which allows us to create tuples representing coordinates (Point(x, y)). This makes it
easy to work with data that has named fields, such as x and y representing the coordinates 
in this case.

Example:
``` python
from collections import namedtuple
# Creating a Point namedtuple with 'x' and 'y' fields
Point = namedtuple('Point', 'x, y')
# Creating a Point instance with x=0 and y=0
coordinate = Point(0, 0)
# Accessing individual components of the Point
print(coordinate.x)  # Output: 0
print(coordinate.y)  # Output: 0
```
note namedtuple objects are immutable.


## Step 1 Initalizing Main Function and modules
```python
import pygame
import random
from enum import Enum
from collections import namedtuple

# Direction Class Inherits Enum - Using class to represent constants as variables.
# This makes the code more readable.
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# namedtuple is a lightweight class and is used to create a lightweight object Point
# Point represents a point with attributes x coordiante and y coordinate
Point = namedtuple('Point', 'x, y')

#rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 20

if __name__ == '__main__': #if we run script as main process

  # game loop
    while True:
       #game returns condition when over and assoicated score
        game_over, score = game.play_step() # game.play_step() continuously runs the game
        # break if game over
        if game_over == True:
            break
    print('Final Score', score)
    pygame.quit()
```
Our game runs continuously scanning for inputs by calling game.play_step. 


## Step 2 Creating SnakeGame PyGame
## Defining initalizer
``` python
   def __init__(self, w=640, h=480):
       self.w = w
        self.h = h
```
We first define the SnakeGame class and the initalizer. 
Within the initalizer two variables w & h 
which represents the width and height of the game. 


#### Initalizing the display
``` python
# initalize display
        self.display = pygame.display.set_mode((self.w, self.h)) 
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
```
Self.display is set by calling
pygame.display.set_mode((self.w, self.h)). Caption is set to Snake and the game clock is initalized.


#### Initalizing the game state
``` python
# initalize game state
        self.direction = Direction.RIGHT
        
        
        self.head = Point(self.w/2,self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
```
1. First set the direction of the snake to right. 
2. Then we initalize the list that stores the components of the snake. We will define the snake as a 
list of coordinates Self.head coordinates is the center of the display and the body of the snake coordinates 
are set as offsets of the head. The offset value is BLOCK_SIZE represnting the space between each 
snake body part and the size of the body. The coordinates are represented as a custom namedtuple Points
which is defined outside the class
3. The score is then set as zero and food as none initally.
4. Finally self._place_food() is called to place the first food and we define our first helper function.

Together End Code:
``` python 
class SnakeGame:
    
    def __init__(self, w=640, h=480):
       self.w = w
        self.h = h

        # initalize display
        self.display = pygame.display.set_mode((self.w, self.h)) 
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        # initalize game state
        self.direction = Direction.RIGHT
        
        
        self.head = Point(self.w/2,self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
```
end.


#### _place_food():
``` python
def _place_food(self):
  x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE)*BLOCK_SIZE
  y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE)*BLOCK_SIZE
  self.food = Point(x, y)
  if self.food in self.snake:
      self._place_food()
```
chooses a random point in the game and if the food already exists in self.snake
pick a new point to store


## Defining play_step(self):
``` python
def play_step(self):
    #1. User Input
                
    #2. Move

    #3. Check game state

    #4. Place food or next move

    #5. Update UI and game clock

    #6. game over and return score
```
First we want to plan the flow of the game and what we need to code. 

#### Defining UI, game clock and return values (#5 & #6)
  ``` python
    #5. Update UI and game clock
    self._update_ui()
    self.clock.tick(SPEED)
    #6. game over and return score
    return game_over, self.score
  ```
  self.clock.tick(SPEED) arguement determines how fast the frames updates

  ``` python
  def _update_ui():
    self.display.fill(BLACK) #  self.display.fill(BLACK) fills in the display blackground as black

    for pt in self.snake:  # For each part of the snake
        #1st Arg: Where being drawn 2nd: Color 3rd: What is being drawn (Rect(position x, position y, width, height))
        pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE)) 
        pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

    #draws the food
    pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

    #Inialize text to render score
    text = font.render("Score: " + str(self.score), True, WHITE)
    self.display.blit(text, [0, 0]) #Put it on the display 1st Arg: Text 2nd Arg: coordinate
    pygame.display.flip() #updates the display surface on the screen
  ```


#### Defining #1. User Input
``` python
  #1. User Input
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          quit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              self.direction = Direction.LEFT
          elif event.key == pygame.K_RIGHT:
              self.direction = Direction.RIGHT
          elif event.key == pygame.K_UP:
              self.direction = Direction.UP
          elif event.key == pygame.K_DOWN:
              self.direction = Direction.DOWN
  ```
  The game first takes in a user input by checking for an input from pygame.
  If there is an input we then parse the input and according to the key pressed/input
  we set the direction of the snake by updating self.direction to corresponding direction.
  Here we check if the key equals a corresponding direction in pygame.(direction) and then
  set the direction of the snake by updating self.direction.

  example: if the user inputs right arrow key the input matches condition pygame.K_RIGHT
  then self.direction is updated to Direction.RIGHT. Direction.RIGHT is an enum which is a
  class that has symbols representing constants. In this example the class Direction has
  four symbols RIGHT, LEFT, UP, DOWN which represents the respective constants 1
  2, 3, 4. In this case Direction.RIGHT represents 1.
  
  #### Defining #2. Move
  ``` python
  #2. Move
      self._move(self.direction)
      self.snake.insert(0, self.head)
  ```
  After checking the user input we then move the snake using the current direction the snake is 
  facing/is stored in self.direction. We do this by calling the helping function self._move(self.dircetion) 
  and inputing the direction stored as the arguement.

  #### Defining _move(self.direction)
  ``` python
  def _move(self.direction):
    x = self.head.x
    y = self.head.y
    if direction == Direction.RIGHT:
        x += BLOCK_SIZE 
    elif direction == Direction.LEFT:
        x -= BLOCK_SIZE 
    elif direction == Direction.DOWN:
        y += BLOCK_SIZE 
    elif direction == Direction.UP:
        y -= BLOCK_SIZE 

    self.head = Point(x, y)
  ```
  _move offsets the coordinates of self.head by the BLOCK_SIZE in the direction the snake is moving.
  self.snake.insert(0, self.head) inserts the updated head in the front of the snake container. This
  doesn't edit the original head in the container since namedTuples are immutable. Meaning in helper
  function _move editing self.head doesn't edit the orignal but changes the reference to the updated
  initalized namedtuple with the offsetted values.

  #### Defining #3. Check game state
  ``` python
  #3. Check game state
      game_over = False
      if self._is_collision():
          game_over = True
          return game_over, self.score
  ```
  if _is_collision() returns true
  set game_over to true and return current game status and score.

  ``` python
  def _is_collision(self):
        #hits bounday
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        #or hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
  ```

  #### Defining #4
  ``` python 
   #4. Place food or next move
    if self.head == self.food:
        self.score += 1
        self._place_food()
    else:
        self.snake.pop()    
  ```
  if the location of self.head is on a food then place a new food otherwise remove the last pt on the snake to make the
  illusion the snake is moving.

  Finished


