import gym
from gym import spaces
from gym.utils import seeding


class RouletteEnv(gym.Env):
    """Simple roulette environment

    The roulette wheel has s spots. If the bet is 0 and a 0 comes up, you win a reward of s-2.
    If any other number comes up you get a reward of -1.

    For non-zero bets, if the parity of your bet matches the parity of the spin, you win 1.
    Otherwise you receive a reward of -1.

    The last action (s+1) stops the rollout for a return of 0 (walking away)"""

    def __init__(self, spots=37):
        self.n = spots + 1
        self.action_space = spaces.Discrete(self.n)
        self.observation_space = spaces.Discrete(1)

    def step(self, action):
        assert self.action_space.contains(action)
        if action == self.n - 1:
            reward = 0.0
            done = True
        else:
            # N.B. np.random.randint draws from [A, B) while random.randint draws from [A,B]
            val = self.np_random.randint(0, self.n - 1)
            if val == action == 0:
                reward = self.n - 2.0
            elif val != 0 and action != 0 and val % 2 == action % 2:
                reward = 1.0
            else:
                reward = -1.0
            done = False
        results = (0, reward, done, {})
        try:
            from gym.utils.step_api_compatibility import step_api_compatibility
            return step_api_compatibility(results, True)
        except:
            return results

    def reset(self, *, seed=None, return_info=True, options=None):
        super().reset(seed=seed)
        if return_info:
            return 0, {}
        else:
            return 0
