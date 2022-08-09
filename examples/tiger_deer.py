import os
import sys 
import pandas as pd
from typing import List

from helpers import build_env
from data.config import EnvConfig

# Build custom exceptions 
## Highly optimzied pettingZoo wrapper designed to facilitate distributed learning.
## This wrapper wraps around the parallel game APIs.
class Game:
    def __init__(self, config: EnvConfig):
        self.config = config
        self.env_name = config.env_name
        try:
            self.env = build_env(config)
        except:
            print("Environment could not be created. Check logs for more information.")
            
        self._agent_ids = self.env.possible_agents 
        self._num_agents = self.env.max_num_agents

    def observation_space(self, agent_id = None):
        if agent_id:
            return self.env.observation_space(agent_id)
        return self.env.observation_spaces

    def action_space(self, agent_id = None):
        if agent_id:
            return self.env.action_space(agent_id)
        return self.env.action_spaces
    
    @property
    def num_agents(self):
        return self._num_agents
    
    @property
    def agent_ids(self):
        return self._agent_ids
    
    @property
    def global_state(self):
        try:
            return self.env.state()
        except:
            print(f"Error: function not supported for env: {self.env_name}")
        return None
    
    @property
    def agents(self):
        return self.env.agents
    
    def reset(self):
        self.last_observations = self.env.reset()
        self.dones = False
        self.last_rewards = None
        self.last_infos = None

    def step(self, actions: List):
        assert len(actions) == len(self.agent_ids), "Invalid action(s) list!"
        self.last_observations, self.last_rewards, self.dones, self.infos = self.env.step(actions)
    
    def is_terminal(self):
        # do binary 'and' of all elements in a dict
        return not bool(self.agents)
    
    def get_observation(self, agent_id: str):
        assert agent_id in self._agent_ids, "Invalid id or agent is dead!"
        return self.last_observations[agent_id]

    def is_agent_alive(self, agent_id):
        assert agent_id in self._agent_ids, "Invalid agent id!"
        return agent_id in self.agents

    def __repr__(self):
        return f"Env: {self.env_name} with {self.num_agents} agents."

if __name__ == "__main__":
    # FOR DEBUGGING ONLY 
    # breakpoint
    # create a parallel env instead.
    
    #env = tiger_deer_v3.parallel_env(map_size=10, minmap_mode=False, max_cycles=50, extra_featuers=False)
    breakpoint()

