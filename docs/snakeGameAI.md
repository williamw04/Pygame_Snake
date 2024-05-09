# Theory

## Reinforcement Learning
Reinforcement learning(RL) is an area of machine learning concerned with how software agents 
should take actions in an enviornment to maximize the notion of cumulative reward.

RL is teaching a software agent how to behave in an enviornment by telling how good the agent is doing using rewards and punishments. 

Agent: Computer player
Enviorment: Snake Game
Give Agent Award: Base on this it should 
try to find the next best action.

### Deep Q Learning
Apprach extends reinforcement leraning by using a deep neural network to predict actions

## Overview

**Game(Pygame)**
-play_step(action)
  -> reward, game_over, score

There is a game loop which there is a play_step (which performs an action) in this case the a 
player inputs an action and the snake moves. Base on the action it returns the current reward, 
if the agent has lost and the current score.

**Agent**
Agent puts everything together so the agent must be aware of the game and model which is stored 
in the agent.

**Training**
-state = get_state(game) : On the current conditions of the game calculate a state
-action = get_move(state) : Using the state decide the nxet action
  -> model.predict() : which uses model.predict()
-reward, game_over, score = game.play_step(action) : Execute action to get reward, game over status and score
-new_state = get_state(game) : cacluate a new state
-remember : store old state and new state and the reward, game over status and score
-model.train() and with the stored information train the model


**Model**
Linear_QNet(DQN) Feed foward neural network with few linear layers
Takes in new state, old state to train the model and passing the current state
in model will output a predicted output

**Deep Dive into Variables**
Action
[1,0,0] -> Straight
[0,1,0] -> right turn
[0,0,1] -> left turn

Reasoning we don't have directions up, left, right and down is in the following case where
the actions are go right then go left resulting in a 180 degree turn and instant game over.

Predicting less states will make it easier for the model.

State (11 values): State is the information the agent needs to know about to enviornment
[danger straight, danger right, danger left,

direction left, direction right,
direction up, direction down,

food left, food right
food up, food down

]
All the values are booleans




Reward: 
  -eat food +10
  -game over: -10
  - everything else 0