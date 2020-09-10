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
        self.buckets = buckets
        self.env = env

        # Q table
        self.Q = np.zeros(self.buckets + (self.env.action_space.n,))

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
        return self.env.action_space.sample() if (np.random.random() <= epsilon ) else np.argmax(self.Q[state])

    def update_q(self, state, action, reward, new_state, alpha):
        self.Q[state][action] += alpha * (reward + GAMMA * np.max(self.Q[new_state]) - self.Q[state][action])

def main():
    # Create the environment
    env = gym.make('CartPole-v0')
    # Create our agent 
    agent = CartPole(env)
    
    for ep in range(EPISODES):
        print(f'Episode: {ep}')

        # Get the initial state
        observation = env.reset()
        # Turn continuous state space into discrete
        state = agent.discretize(observation)
        
        # Get Learning and Exploration rates
        alpha = agent.get_alpha(ep) 
        epsilon = agent.get_epsilon(ep)

        done = False
        i = 0
        while not done:
            # Render the frame
            env.render()

            # Choose the action
            action = agent.get_action(state, epsilon)

            # Take the action in game
            observation, reward, done, _ = env.step(action)
            new_state = agent.discretize(observation)

            # update our Q-Table
            agent.update_q(state, action, reward, new_state, alpha)
            state = new_state
            i += 1


    env.close()
if __name__=='__main__':
    main()

