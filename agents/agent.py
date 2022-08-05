import random



class BaseAgent:
    def __init__(self, _id, observation_space, action_space):
        self.id = _id
        self.observation_space = observation_space
        self.action_space = action_space


        
