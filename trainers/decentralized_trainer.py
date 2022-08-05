import sys
from typing import List, Optional

from trainers.trainer import Trainer


class dec_trainer(Trainer):
    def __init__(self, config: TrainerConfig, agent_ids: List, agents: List):
        super.__init__(agent_ids)
        self.agents = agents
        self.game = game

    def run_episodes(self, num_games: Optional[int]):
        breakpoint()

