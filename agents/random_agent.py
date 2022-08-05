import numpy as np

from agents.agent import BaseAgent

class RandomAgent(BaseAgent):
    def __init__(self, _id, observation_space, action_space):
        super.__init__(_id, observation_space, action_space)

    def get_action(self, observation):
        return np.random.choice([i for i in range(self.action_space[0])])

