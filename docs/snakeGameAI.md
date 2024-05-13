# Theory

### Reinforcement Learning
Reinforcement learning(RL) is an area of machine learning concerned with how software agents 
should take actions in an enviornment to maximize the notion of cumulative reward.

RL is teaching a software agent how to behave in an enviornment by telling how good the agent is doing using rewards and punishments. 

Agent: Computer player
Enviorment: Snake Game
Give Agent Award: Base on this it should 
try to find the next best action.

### Deep Q Learning
Apprach extends reinforcement leraning by using a deep neural network to predict actions

(Deep) Q Learning 
Note: Skip/or come back to this section after reading the overview
Q Value = Quality of action : We want to improve Q value so each action to improve the quality of the predicted action

0. Init Q Value (=init model) :Initalize model with random parameters
1. Choose action (model.predict(state)) : Choose an action or a random move 
(Done at the beginning of training since model is not trained enough to choose a good action. Later tradeoff is done
when we train the model enough to only get an action using the model instead of randomness. This tradeoff is between
exploration and expliotation).
2. Perform action
3. Measure reward
4. Update Q value(+ train model) repeat step 1

To train a model we need to use a loss functino to optimize/minimize.

### **Bellman Equation**
Predicts the value of a decision in terms of the payoff from some inital

NewQ(s,a) = Q(s,a) + α[R(s,a) + γmaxQ'(s',a') - Q(s,a)]  
- NewQ(s,a): New Q value for the state and action
- Q(s,a): current value Q
- α: Learning rate
- R(s,a): Reward for taking the action at that state
- γ: discount rate
- maxQ'(s',a') - Q(s,a): max expected future reward given the new s' and all possible actions at that new state

Qinital = model.predict(state0)
Qnew = R + γ * (max Q(state1))

**Training:**
- state = get_state(game) : On the current conditions of the game calculate a state
- action = get_move(state) : Using the state decide the nxet action
  - -> model.predict() : which uses model.predict() 
**Qinital:** Is calculated by first taking state and calling  
- reward, game_over, score = game.play_step(action) : Execute action to get reward, game over status and score
- new_state = get_state(game) : cacluate a new state
**Qnew:** Aftering taking the play step the new q ss calculated by using the state after the play step.
- remember : store old state and new state and the reward, game over status and score
- model.train() and with the stored information train the model

Loss Function:
loss = (Qnew - Q)^2
    

# Overview

### **Game(Pygame)**
-play_step(action)
  -> reward, game_over, score

There is a game loop which there is a play_step (which performs an action) in this case the a 
player inputs an action and the snake moves. Base on the action it returns the current reward, 
if the agent has lost and the current score.

### **Agent:**
Agent puts everything together so the agent must be aware of the game and model which is stored 
in the agent.

### **Training:**
- state = get_state(game) : On the current conditions of the game calculate a state
- action = get_move(state) : Using the state decide the nxet action
  - -> model.predict() : which uses model.predict()
- reward, game_over, score = game.play_step(action) : Execute action to get reward, game over status and score
- new_state = get_state(game) : cacluate a new state
- remember : store old state and new state and the reward, game over status and score
- model.train() and with the stored information train the model


### **Model:**
Linear_QNet(DQN) Feed foward neural network with few linear layers
Takes in new state, old state to train the model and passing the current state
in model will output a predicted output

### **Deep Dive into Variables:**
**Action**
``` python
[1,0,0] -> Straight
[0,1,0] -> right turn
[0,0,1] -> left turn
```

Reasoning we don't have directions up, left, right and down is in the following case where
the actions are go right then go left resulting in a 180 degree turn and instant game over.

Predicting less states will make it easier for the model.

**State** (11 values): State is the information the agent needs to know about to enviornment
```
[danger straight, danger right, danger left,

direction left, direction right,
direction up, direction down,

food left, food right
food up, food down

]
```
All the values are booleans


**Reward:** 
  -eat food +10
  -game over: -10
  - everything else 0


