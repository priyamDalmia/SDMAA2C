import sys
from typing import List, Optional

from utils import *
from trainers.trainer import Trainer


class DecentralizedTrainer(Trainer):
    def __init__(self, 
            config: TrainerConfig, 
            agent_ids: List, 
            agents: List,
            game: Game):
        super.__init__(config, agent_ids)
        self.agents = agents
        self.game = game

        # Techincally config should contain the mode for agent inti
        self.agent_init = initialize_random_agents

        # initialize agents 
        # reset game 

        pass
    def run_episodes(self, num_games: Optional[int]):
        breakpoint()

