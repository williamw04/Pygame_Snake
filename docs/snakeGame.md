# Game Documentation

## Initalizing neccessary modules, classes variables etc for game function

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

Enumations (enums) in python is used to assign constants/unqiue values to symbloic names.
The purpose of enumerations is to enchance readability, maintainbility and make it easier to
work with a fixed set of values. In this case we define a class Direction used to represent which
contains the symbols of possible directions the snake can face.

### namedtuple from collections
``` python 
Point = namedtuple('Point', 'x, y') 
```
namedtuple is a factory function (a function that returns instances of objects or other 
functions. It is a design pattern utilized in object-oriented programming to encapsulate the
process of creating objects. Basically namedtuple is a special function that creates a tuple with
custom labels. ).