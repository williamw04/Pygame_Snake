import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()


font = pygame.font.Font('arial.ttf', 25)

#reset : agent can reset game and restart game
#reward : reward agent receives
#play function play(action) -> direction
#game_iteration
#is_collision

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
SPEED = 40
class SnakeGameAI:
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        # initalize display
        self.display = pygame.display.set_mode((self.w, self.h)) 
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()

    # Refactored initalizer and seperated code to initalizing game state
    # into its own reset func
    def reset(self):
        # initalize game state
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2,self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        #1. User Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #commented out since we get action from agent.    
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         self.direction = Direction.LEFT
            #     elif event.key == pygame.K_RIGHT:
            #         self.direction = Direction.RIGHT
            #     elif event.key == pygame.K_UP:
            #         self.direction = Direction.UP
            #     elif event.key == pygame.K_DOWN:
            #         self.direction = Direction.DOWN
                
        #2. Move
        self._move(action) #takes action from agent instead of using self.direction
        self.snake.insert(0, self.head)

        #3. Check game state
        reward = 0 # there is a reward base on the given action so we need store it
        game_over = False
        # extra condition which terminates session if the agent doesn't 
        # progess/grow (goes in circle and doesn't go for food)
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10 # return -10 for losing due to actions
            return reward, game_over, self.score # now we also return reward

        #4. Place food or next move
        if self.head == self.food:
            self.score += 1
            reward = 10 #reward is +10 because snake gets food
            self._place_food()
        else:
            self.snake.pop()    

        #5. Update UI and game clock
        self._update_ui()
        self.clock.tick(SPEED)
        #6. game over and return score
        return reward, game_over, self.score # we return reward as well
    
    def is_collision(self, pt = None): 
        if(pt == None): #using pt since we need to check danger around snake
            pt = self.head

        #hits bounday
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        #or hits itself
        if pt in self.snake[1:]:
            return True
        
        return False
    
    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action): #takes action instead of self.direction
        # [straight, right, left]

        clock_wise = [Direction.RIGHT,Direction.DOWN, Direction.LEFT, Direction.UP]
        #setting index
        index = clock_wise.index(self.direction)

        if np.array_equal(action, [1,0,0]):
            new_dir = clock_wise[index]
        elif np.array_equal(action, [0,1,0]): #right turn (close wise)
            next_index = (index + 1) % 4 #next is right -> down -> left -> up -> right ...
            new_dir = clock_wise[index]
        else:
            next_index = (index - 1) % 4  #next is right -> up -> left -> down -> right ...
            new_dir = clock_wise[index]

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE 
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE 
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE 
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE 

        self.head = Point(x, y)


# Don't need main function since we controll from agent
# if __name__ == '__main__': #if we run script as main process
#     game = SnakeGame()

#     # game loop
#     while True:
#         game_over, score = game.play_step()
#         # break if game over
#         if game_over == True:
#             break

#     print('Final Score', score)


    # pygame.quit()