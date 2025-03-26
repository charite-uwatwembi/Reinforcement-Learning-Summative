import gym
from gym import spaces
import numpy as np
import random

class MaternalHealthEnv(gym.Env):
    def __init__(self):
        super(MaternalHealthEnv, self).__init__()
        
        # Grid size (5x5 village environment)
        self.grid_size = 5
        
        # Action space: 4 possible movements (up, down, left, right)
        self.action_space = spaces.Discrete(4)
        
        # Observation space: (Agent's position in a 5x5 grid)
        self.observation_space = spaces.Box(low=0, high=self.grid_size-1, shape=(2,), dtype=np.int32)
        
        # Define grid elements
        self.HEALTH_CENTER = (2, 0)   # Where the agent starts (🏥)
        self.PREGNANT_MOTHER = (4, 4) # Goal (👩‍🍼)
        self.OBSTACLES = [(1, 1), (1, 3), (2, 2), (3, 3)] # Blocked paths (🚧)
        
        # Reset the environment
        self.reset()
    
    def reset(self):
        # Start agent at health center
        self.agent_pos = list(self.HEALTH_CENTER)
        return np.array(self.agent_pos, dtype=np.int32)
    
    def step(self, action):
        x, y = self.agent_pos
        
        # Move agent based on action
        if action == 0:  # Move Up
            y = max(y - 1, 0)
        elif action == 1:  # Move Down
            y = min(y + 1, self.grid_size - 1)
        elif action == 2:  # Move Left
            x = max(x - 1, 0)
        elif action == 3:  # Move Right
            x = min(x + 1, self.grid_size - 1)
        
        new_pos = (x, y)
        
        # Check if agent hits an obstacle
        if new_pos in self.OBSTACLES:
            reward = -5  # Penalty for hitting obstacles
            done = False
        elif new_pos == self.PREGNANT_MOTHER:
            reward = 10  # Reward for reaching the mother
            done = True
        else:
            reward = -1  # Small penalty for each step to encourage efficiency
            done = False
        
        # Update agent position
        self.agent_pos = list(new_pos)
        
        return np.array(self.agent_pos, dtype=np.int32), reward, done, {}
    
    def render(self):
        grid = [['🟩' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        # Place Obstacles
        for ox, oy in self.OBSTACLES:
            grid[oy][ox] = '🚧'
        
        # Place Health Center, Mother, and Agent
        grid[self.HEALTH_CENTER[1]][self.HEALTH_CENTER[0]] = '🏥'
        grid[self.PREGNANT_MOTHER[1]][self.PREGNANT_MOTHER[0]] = '👩‍🍼'
        grid[self.agent_pos[1]][self.agent_pos[0]] = '🤖'
        
        for row in grid:
            print(' '.join(row))
        print('\n')
