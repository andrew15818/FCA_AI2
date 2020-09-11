import gym 
import numpy as np
import math 
from collections import deque
# Constants & Hyperparameters
EPISODES = 500 
GAMMA = 1.0         # Discount factor
LEARNING_RATE = 0.1
EPSILON = 0.1       # Exploration rate

class CartPole():
    def __init__(self, env, buckets=(1, 2, 6, 12)):
        # Making the ranges into discrete ranges



        # Q table


    # Turn a continuous state space into discrete one
    def discretize(self, obs):
        upper_bounds = [self.env.observation_space.high[0], 0.5, self.env.observation_space.high[2], math.radians(50)] 
        lower_bounds = [self.env.observation_space.low[0], -0.5, self.env.observation_space.low[2], -math.radians(50)]
        ratios = [(obs[i] + abs(lower_bounds[i])) / (upper_bounds[i] - lower_bounds[i]) for i in range(len(obs))]
        new_obs = [int(round((self.buckets[i] - 1) * ratios[i])) for i in range(len(obs))]
        new_obs = [min(self.buckets[i] - 1, max(0, new_obs[i])) for i in range(len(obs))]
        return tuple(new_obs)

    def get_alpha(self, ep):
        return max(LEARNING_RATE, min(1.0, 1.0 - math.log10((ep + 1) / 25)))

    def get_epsilon(self, ep):
        return max(EPSILON, min(1, 1.0 - math.log10((ep + 1) / 25)))

    def get_action(self, state, epsilon):


    def update_q(self, state, action, reward, new_state, alpha):
        

def main():
    # Create the environment

    # Create our agent 

    
    for ep in range(EPISODES):
        print(f'Episode: {ep}')

        # Get the initial state

        # Turn continuous state space into discrete

        
        # Get Learning and Exploration rates





        while not done:
            # Render the frame


            # Choose the action


            # Take the action in game



            # update our Q-Table





    env.close()
if __name__=='__main__':
    main()

