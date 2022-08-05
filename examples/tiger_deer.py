import os
import sys 
import pandas as pd
from typing import List

from helpers import build_env
from pettingzoo.magent import tiger_deer_v3

## Highly optimzied pettingZoo wrapper designed to facilitate distributed learning.
## This wrapper wraps around the parallel game APIs.
class Game:
    def __init__(self, config, env_name):
        self.config = config
        self.env_name = env_name
        try:
            self.env = build_env(config, env)
        except:
            print("Environment could not be created. Check logs for more information.")

        self.agent_ids = self.env.agents
        self.num_agents = self.env.num_agents

    @property
    def observation_spaces(self, agent_id = None):
        if agent_id:
            return self.env.observation_space(agent_id)
        return self.env.observation_spaces()

    @property
    def action_spaces(self, agent_id = None):
        if agent_id:
            return self.env.action_space(agent_id)
        return self.env.action_spaces()

    def reset(self):
        self.env.reset()
        self.dones = False
        self.last_observations = None
        self.last_rewards = None
        self.last_infos = None
        breakpoint()

    def step(self, actions: List):
        assert len(actions) == len(self.agent_ids), "Invalid action(s) list!"
        self.env.step(actions)
        self.last_observations, self.last_rewards, self.dones, self.infos = env.last()
    
    def is_terminal(self):
        # do binary 'and' of all elements in a dict
        breakpoint()

if __name__ == "__main__":
    
    # breakpoint
    # create a parallel env instead.
    env = tiger_deer_v3.parallel_env(map_size=10, minmap_mode=False, max_cycles=50, extra_featuers=False)
    breakpoint()

