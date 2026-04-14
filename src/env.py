import gymnasium as gym
from gymnasium import spaces
import numpy as np

class SimpleTradingEnv(gym.Env):
    def __init__(self, data):
        super(SimpleTradingEnv, self).__init__()
        self.data = data
        self.current_step = 0
        
        # Actions: 0 (Hold), 1 (Buy), 2 (Sell)
        self.action_space = spaces.Discrete(3)
        # Observation space: 5 days of history, 1 feature (price)
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(5,), dtype=np.float32)

    def reset(self, seed=None):
        super().reset(seed=seed)
        self.current_step = 5
        self.balance = 10000
        self.shares = 0
        return self._next_observation(), {}

    def _next_observation(self):
        obs = self.data[self.current_step-5:self.current_step]
        return np.array(obs, dtype=np.float32)

    def step(self, action):
        current_price = self.data[self.current_step]
        
        # Very simplified trading logic for demonstration
        if action == 1 and self.balance > current_price:  # Buy
            self.shares += 1
            self.balance -= current_price
        elif action == 2 and self.shares > 0:  # Sell
            self.shares -= 1
            self.balance += current_price
            
        self.current_step += 1
        
        done = self.current_step >= len(self.data) - 1
        reward = self.balance + (self.shares * current_price) - 10000 # Profit as reward
        
        return self._next_observation(), reward, done, False, {}
