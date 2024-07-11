import numpy as np

from autora.theorist.rnn_sindy_rl import RNNSindy
from autora.theorist.rnn_sindy_rl.resources.bandits import AgentQ, EnvironmentBanditsDrift, create_dataset

rnnsindy = RNNSindy(n_actions=2)

synthetic_experiment = True

# setup of synthetic experiment
if synthetic_experiment:
    agent = AgentQ(
        alpha=0.25,
        beta=3,
        n_actions=2,
        forget_rate=0.,
        perseveration_bias=0.,
        correlated_reward=False,
    )
    env = EnvironmentBanditsDrift(
        sigma=0.25,
        n_actions=2,
    )
    n_trials_per_session, n_sessions = 100, 5
    training_data, experiment_list = create_dataset(agent, env, n_trials_per_session, n_sessions)
    conditions = np.expand_dims(np.stack([exp.rewards for exp in experiment_list]), -1)  # rewards with shape (session, trial, 1)
    observations = np.eye(2)[np.stack([exp.choices for exp in experiment_list])]  # one-hot encoding of actions with shape (session, trial, actions)
else:
    conditions = np.random.randint(0, 2, (1, 100, 1))  # rewards with shape (session, trial, 1)
    observations = np.eye(2)[np.random.randint(0, 2, (1, 100))]  # one-hot encoding of actions with shape (session, trial, actions)

rnnsindy = rnnsindy.fit(conditions, observations)
