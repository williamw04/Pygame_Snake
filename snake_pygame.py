import pygame
import random
from enum import Enum
pygame.init()

# Direction Class Inherits Enum to
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        # initalize display
        self.display = pygame.display_set.set_mode((self.w, self.h)) 
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        # initalize game state
        self.direction =  "E"

    def play_step(self):
        pass


if __name__ == '__main__': #if we run script as main process
    game = SnakeGame()

    # game loop
    while True:
        print('A line of Text')
        game.play_step()

    # break if game over

pygame.quit()