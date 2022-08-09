from typing import Callable, List, Dict
from dataclasses import dataclass


from trainers.utils import *

@dataclass
class EnvConfig:
    env_name: str = "tiger_deer"
    # environment specific paramters 
    map_size: int = 10
    max_cycles: int = 100
    minmap_mode: bool = False
    tiger_step_recover: float = -0.1
    deer_attacked: float = -0.1
    extra_features: bool = False

    def __repr__(self):
        return f"Env: {self.env_name} with size: {self.map_size}"

@dataclass
class TrainerConfig:
    agent_class: str = "random"
    agent_init_func: Callable = initialize_random_agents

    def __repr__(self):
        return "repr"

@dataclass
class Config:
    name: str = "config"
    env_config = EnvConfig()
    trainer_config = TrainerConfig()

    def __repr__(self):
        return "repr"
