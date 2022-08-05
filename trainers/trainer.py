from typing import List
from utils import *

# use trainer config class
# use  logger config calss

class Trainer:
    def __init__(self, config, agent_ids: List):
        self.config = config
        self.agent_ids = agent_ids
