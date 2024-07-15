import numpy as np

from gym.envs.registration import register

from gym_toytext.guessing_game import GuessingGame
from gym_toytext.hotter_colder import HotterColder
from gym_toytext.kellycoinflip import KellyCoinflipEnv, KellyCoinflipGeneralizedEnv
from gym_toytext.nchain import NChainEnv
from gym_toytext.roulette import RouletteEnv


register(
    id="GuessingGame-v0",
    entry_point="gym_toytext:GuessingGame",
    max_episode_steps=200,
    kwargs={
        "low": -1000,
        "high": 1000,
        "low_bound": -10000,
        "high_bound": 10000,
        "rtol": 0,
        "atol": 10,
        "guess_max": 200,
        "rewarder": None,
        "obs_format": "range",
        "dtype": np.float32,
    }
)

register(
    id="GuessingGameRange-v0",
    entry_point="gym_toytext:GuessingGame",
    max_episode_steps=200,
    kwargs={
        "low": -1000,
        "high": 1000,
        "low_bound": -10000,
        "high_bound": 10000,
        "rtol": 0,
        "atol": 10,
        "guess_max": 200,
        "rewarder": None,
        "obs_format": "range",
        "dtype": np.float32,
    }
)

register(
    id="GuessingGame-v1",
    entry_point="gym_toytext:GuessingGame",
    max_episode_steps=200,
    kwargs={
        "low": 0,
        "high": 1023,
        "guess_max": 200,
        "rewarder": None,
        "obs_format": "range",
        "dtype": np.int32,
    }
)

register(
    id="GuessingGameRange-v1",
    entry_point="gym_toytext:GuessingGame",
    max_episode_steps=200,
    kwargs={
        "low": 0,
        "high": 1023,
        "rewarder": None,
        "obs_format": "range",
        "dtype": np.int32,
    }
)

register(
    id="HotterColder-v0",
    entry_point="gym_toytext:HotterColder",
    max_episode_steps=200,
)

register(
    id="KellyCoinflip-v0",
    entry_point="gym_toytext:KellyCoinflipEnv",
    reward_threshold=246.61,
)

register(
    id="KellyCoinflipGeneralized-v0",
    entry_point="gym_toytext:KellyCoinflipGeneralizedEnv",
)

register(
    id="NChain-v0",
    entry_point="gym_toytext:NChainEnv",
    max_episode_steps=1000,
)

register(
    id="Roulette-v0",
    entry_point="gym_toytext:RouletteEnv",
    max_episode_steps=100,
)


