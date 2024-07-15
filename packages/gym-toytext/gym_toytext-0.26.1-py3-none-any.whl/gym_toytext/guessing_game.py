from functools import partial
import six

import numpy as np

import gym
from gym import spaces
from gym.utils import seeding



class GuessingGame(gym.Env):
    """Number guessing game

    The object of the game is to guess within 1% of the randomly chosen number
    within 200 time steps

    After each step the agent is provided with one of four possible observations
    which indicate where the guess is in relation to the randomly chosen number

    0 - No guess yet submitted (only after reset)
    1 - Guess is lower than the target
    2 - Guess is equal to the target
    3 - Guess is higher than the target

    The rewards are:
    0 if the agent's guess is outside of 1% of the target
    1 if the agent's guess is inside 1% of the target

    The episode terminates after the agent guesses within 1% of the target or
    200 steps have been taken

    The agent will need to use a memory of previously submitted actions and observations
    in order to efficiently explore the available actions

    The purpose is to have agents optimize their exploration parameters (e.g. how far to
    explore from previous actions) based on previous experience. Because the goal changes
    each episode a state-value or action-value function isn't able to provide any additional
    benefit apart from being able to tell whether to increase or decrease the next guess.

    The perfect agent would likely learn the bounds of the action space (without referring
    to them explicitly) and then follow binary tree style exploration towards to goal number
    
    Parameters
    ----------
    low: int | float=-1000
    high: int  | float=1000
    low_bound: Optional[int | float]=None
    high_bound: int | float=None
    rtol: Optional[int | float]=1e-5
    atol: Optional[int | float]=1e-8
    guess_max: Optional[int]=None
    rewarder: Optional[str | callable]=None  function parameters: action, number, guess_count, done
    obs_format: Optional[str]=None
    """
    INIT, LT, EQ, GT = range(4)
    
    def __init__(self, low=-1000, high=1000, low_bound=None, high_bound=None, rtol=1e-5, atol=1e-8, guess_max=None, rewarder=None, obs_format=None, dtype=np.float32):
        self.low = low
        self.high = high
        self.low_bound = low if low_bound is None else low_bound
        self.high_bound = high if high_bound is None else high_bound
        self.rtol = rtol
        self.atol = atol
        self.rewarder = rewarder
        self.dtype = dtype
        self.obs_format = obs_format
        
        self.action_space = spaces.Box(
            low=np.array([self.low_bound], dtype=dtype),
            high=np.array([self.high_bound], dtype=dtype),
        )
        if obs_format is None:
            self.observation_space = spaces.Discrete(4)
        elif obs_format == "range":
            self.observation_space = spaces.Box(
                low=np.array([self.low_bound, self.low_bound], dtype=dtype),
                high=np.array([self.high_bound, self.high_bound], dtype=dtype),
            )
        else:
            raise NotImplementedError()

        self.number = 0
        self.guess_count = 0
        self.guess_max = guess_max
        self.observation = 0

        self.reset()

    def step(self, action):
        if isinstance(action, (int, float)):
            action = np.array([action])
        elif isinstance(action, list):
            action = np.array(action)

        assert self.action_space.contains(action)

        if action < self.number:
            self.observation = GuessingGame.LT
            self.obs_low = action

        elif action == self.number:
            self.observation = GuessingGame.EQ
            self.obs_low = action
            self.obs_high = action

        elif action > self.number:
            self.observation = GuessingGame.GT
            self.obs_high = action

        act = action[0]
        done = bool(np.isclose(act, self.number, rtol=self.rtol, atol=self.atol))
        
        if self.rewarder is None:
            reward = int(done)
        else:
            kwargs = {"action": act, "number": self.number, "guess_count":  self.guess_count, "done": done}
            if isinstance(self.rewarder, six.string_types):
                reward = eval(self.rewarder, kwargs)
            else:
                reward = self.rewarder(**kwargs)

        self.guess_count += 1
        if self.guess_max is not None and self.guess_count >= self.guess_max:
            done = True

        results = (self._get_obs(), reward, done, self._get_info())
        try:
            from gym.utils.step_api_compatibility import step_api_compatibility
            return step_api_compatibility(results, True)
        except:
            return results

    def _get_obs(self):
        if self.obs_format is None:
            return self.observation
        else:
            return np.array([self.obs_low, self.obs_high], dtype=self.dtype)

    def _get_info(self):
        return {"number": self.number, "guesses": self.guess_count}

    def reset(self, *, seed=None, return_info=True, options=None):
        super().reset(seed=seed)
        self.number = self.dtype(self.np_random.uniform(self.low, self.high))
        self.guess_count = 0
        self.observation = GuessingGame.INIT
        self.obs_low = self.low_bound
        self.obs_high = self.high_bound
        if return_info:
            return self._get_obs(), self._get_info()
        else:
            return self._get_obs()
