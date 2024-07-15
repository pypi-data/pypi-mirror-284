# gym_toytext

This repository contains the text environments previously present in OpenAI Gym <0.20. These environments had been in the master branch of [openai/gym](https://github.com/openai/gym/) but later excluded in [this pull](https://github.com/openai/gym/pull/2384/).


### List of environments

| environment | commit history | first committer |
| --- | --- | --- |
| `GuessingGame-v0` | [`guessing_game.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/guessing_game.py) | @JKCooper2 |
| `HotterColder-v0` | [`hotter_colder.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/hotter_colder.py) | @JKCooper2 |
| `KellyCoinflip-v0` and `KellyCoinflipGeneralized-v0` | [`kellycoinflip.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/kellycoinflip.py) | @gwern |
| `NChain-v0` | [`nchain.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/nchain.py) | @machinaut |
| `Roulette-v0` | [`roulette.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/roulette.py) | @gdb |

We also provide alternative versions of `GuessingGame`:

- `GuessingGame-v1` and `GuessingGameRange-v1` use different default parameters.
- `GuessingGameRange-v0`  and `GuessingGameRange-v1` show observations in the format of `(low, high)`.


### Compatibility

- `gym>=0.26`: Please use `gym_toytext>=0.26`.
- `gym>=0.19, gym<0.26`: Please use `gym_toytext==0.25`.


### Install

```
pip install gym-toytext
```


### Usage

```python
import gym
import gym_toytext

env = gym.make("GuessingGame-v0")
observation, info = env.reset()
low, high = env.action_space.low, env.action_space.high
while True:
    action = (low + high) / 2.
    observation, reward, termination, truncation, info = env.step(action)
    if termination or truncation:
        break
    if observation == 1:
        low = action
    elif observation == 3:
        high = action
env.close()
```
