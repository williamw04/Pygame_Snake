# Game Documentation
In this docuementation I will explain the process of creating the game. I will provide insight 
into techniques that were utilized and an explaination of each component of the program.

## Step 1 Initalizing neccessary modules, classes variables etc for game function

### Importing Modules
``` python
import pygame
import random
from enum import Enum
from collections import namedtuple
```

### Enumations 
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

### rest of initalized instances
```python
#rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 20
```

## Step 2 Initalizing Main Function

```python
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

## Step 3 Creating SnakeGame PyGame

```python
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

We first define the SnakeGame class and the initalizer. 

### Defining initalizer
Within the initalizer two variables w & h
which represents the width and height of the game. 

#### Initalizing the display
Self.display is set by calling
pygame.display.set_mode((self.w, self.h)). Caption is set to Sanke and the game clock is initalized.

#### Initalizing the game state
First set the direction of the snake to right. Then we build the components of the snake.
We will define the snake as a list of coordinates (Note: self.snake will also contain food and 
the reasoning will be clearer). Self.head coordinates is the center of the display
and the body ofthe snake coordinates are set as offsets of the head.

The score is then set as zero and food as none initally.

Finally self._place_food() is called to place the first food and we define our first helper function.

### _place_food()


###
    