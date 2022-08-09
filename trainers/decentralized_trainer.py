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

    # TODO create wrapper to send data back and forth
    def run_episodes(self, num_games: Optional[int]):
        
        for episode in range(num_games):
            breakpoint()
            game = self.game.copy()
            done = self.game.is_terminal()
            
            game_steps = 0
            while not done:
                actions = {}
                for agent_id, agent in self.agents:
                    agent_observation = game.get_observations(agent_id)
                    action = agent.get_action(agent_obseravtion)
                    actions[agent_id] = action

                # assert that all actions are present
                # TODO for any agent, check that action is not out of bounds
                
                game.step(actions)
                done = game.is_terminal()
                
                # check training type
                # and save experience to buffer in accordance. 

