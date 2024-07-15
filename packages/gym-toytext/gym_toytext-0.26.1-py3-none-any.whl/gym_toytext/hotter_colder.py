import numpy as np

import gym
from gym import spaces
from gym.utils import seeding


class HotterColder(gym.Env):
    """Hotter Colder
    The goal of hotter colder is to guess closer to a randomly selected number

    After each step the agent receives an observation of:
    0 - No guess yet submitted (only after reset)
    1 - Guess is lower than the target
    2 - Guess is equal to the target
    3 - Guess is higher than the target

    The rewards is calculated as:
    (min(action, self.number) + self.range) / (max(action, self.number) + self.range)

    Ideally an agent will be able to recognize the 'scent' of a higher reward and
    increase the rate in which is guesses in that direction until the reward reaches
    its maximum
    """

    def __init__(self):
        self.range = 1000  # +/- the value number can be between
        self.bounds = 2000  # Action space bounds

        self.action_space = spaces.Box(
            low=np.array([-self.bounds]).astype(np.float32),
            high=np.array([self.bounds]).astype(np.float32),
        )
        self.observation_space = spaces.Discrete(4)

        self.number = 0
        self.guess_count = 0
        self.guess_max = 200
        self.observation = 0

        self.reset()

    def step(self, action):
        if isinstance(action, (int, float)):
            action = np.array([action])
        elif isinstance(action, list):
            action = np.array(action)

        assert self.action_space.contains(action)

        if action < self.number:
            self.observation = 1

        elif action == self.number:
            self.observation = 2

        elif action > self.number:
            self.observation = 3

        reward = (
            (min(action, self.number) + self.bounds)
            / (max(action, self.number) + self.bounds)
        ) ** 2

        self.guess_count += 1
        done = self.guess_count >= self.guess_max

        results = (self.observation, reward[0], done, self._get_info())
        try:
            from gym.utils.step_api_compatibility import step_api_compatibility
            return step_api_compatibility(results, True)
        except:
            return results

    def _get_info(self):
        return {"number": self.number, "guesses": self.guess_count}

    def reset(self, *, seed=None, return_info=True, options=None):
        super().reset(seed=seed)
        self.number = self.np_random.uniform(-self.range, self.range)
        self.guess_count = 0
        self.observation = 0
        if return_info:
            return self.observation, self._get_info()
        else:
            return self.observation
