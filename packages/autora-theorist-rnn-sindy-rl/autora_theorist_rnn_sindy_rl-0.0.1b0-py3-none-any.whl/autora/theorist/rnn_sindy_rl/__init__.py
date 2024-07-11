"""
RNN-SINDy Theorist
"""
from typing import Union

import numpy as np
import pandas as pd
import torch
from sklearn.base import BaseEstimator
import pysindy as ps

from autora.theorist.rnn_sindy_rl.rnn_main import main as rnn_main
from autora.theorist.rnn_sindy_rl.sindy_main import main as sindy_main
from autora.theorist.rnn_sindy_rl.resources.rnn_training import ensemble_types
from autora.theorist.rnn_sindy_rl.resources.rnn import RLRNN, EnsembleRNN
from autora.theorist.rnn_sindy_rl.resources.rnn_training import ensemble_types
from autora.theorist.rnn_sindy_rl.resources.sindy_utils import check_library_setup
from autora.theorist.rnn_sindy_rl.resources.bandits import AgentSindy


class RNNSindy(BaseEstimator):
    """
    Include inline mathematics in docstring \\(x < 1\\) or $c = 3$
    or block mathematics:

    \\[
        x + 1 = 3
    \\]


    $$
    y + 1 = 4
    $$

    """

    def __init__(self, n_actions):
        # possible arguments for init
        # environment parameters
        self.n_actions = n_actions

        # rnn parameters
        hidden_size = 4
        dropout = 0.25
        checkpoint = None

        # ensemble parameters
        self.evolution_interval = 5
        self.sampling_replacement = False
        self.n_submodels = 1
        self.ensemble = ensemble_types.NONE
        self.voting_type = EnsembleRNN.MEDIAN

        # sindy parameters
        self.threshold = 0.03
        self.polynomial_degree = 1
        self.regularization = 1e-1
        self.sindy_ensemble = False
        self.library_ensemble = False
        self.library = ps.PolynomialLibrary(degree=self.polynomial_degree)

        # actual code begins here
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        x_train_list = ['xQf', 'xQr', 'xQc', 'xH']
        control_list = ['ca', 'ca[k-1]', 'cr', 'cQr']
        self.sindy_feature_list = x_train_list + control_list

        self.parsing_dict = {
            ' 1 ': '',
            'cr': 'Reward',
            '[k+1]': '_{t+1}',
        }

        # TODO: glossary, get model equation, q-value visualization

        # library setup aka which terms are allowed as control inputs in each SINDy model
        # key is the SINDy submodel name, value is a list of allowed control inputs
        self.library_setup = {
            'xQf': [],
            'xQc': ['cQr'],
            'xQr': ['cr'],
            'xH': []
        }

        # data-filter setup aka which samples are allowed as training samples in each SINDy model corresponding to the given filter condition
        # key is the SINDy submodel name, value is a list with the first element being the feature name to be used as a filter and the second element being the filter condition
        # Example:
        # 'xQf': ['ca', 0] means that only samples where the feature 'ca' is 0 are used for training the SINDy model 'xQf'
        self.datafilter_setup = {
            'xQf': ['ca', 0],
            'xQc': ['ca', 0],
            'xQr': ['ca', 1],
            'xH': ['ca[k-1]', 1]
        }

        if not check_library_setup(self.library_setup, self.sindy_feature_list, verbose=False):
            raise ValueError('Library setup does not match feature list.')

        if self.ensemble > -1 and self.n_submodels == 1:
            Warning('Ensemble is actived but n_submodels is set to 1. Deactivating ensemble...')
            ensemble = ensemble_types.NONE

        # define model
        self.rnn = RLRNN(
            n_actions=n_actions,
            hidden_size=hidden_size,
            init_value=0.5,
            device=device,
            list_sindy_signals=self.sindy_feature_list,
            dropout=dropout,
        ).to(device)
        self.rnn.set_device(device)

        self.sindy = AgentSindy(n_actions)

    def fit(self,
            conditions: Union[pd.DataFrame, np.ndarray],  # rewards
            observations: Union[pd.DataFrame, np.ndarray],  # actions
            ):
        """
        Examples:
            >>> _conditions = [np.array([[0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [1, 0]])]
            >>> _observations =[np.array([[0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [1, 0]])]
            >>> model = RNNSindy(2)
            >>> model.fit(_conditions, _observations)
        """

        # inputs shapes of conditions and observations:
        # conditions: (trials, reward_per_arm)
        # observations: (trials, action_onehot)

        # shape after conversion:
        # shape of conditions: (n_sessions, n_trials, n_features) with features = (action[t], reward[t], (only for visualization:)*reward_probs)
        # shape of observations: (n_sessions, n_trials, n_features) with features = (action[t+1])

        if isinstance(conditions, pd.Series):
            conditions = conditions.tolist()
        if isinstance(observations, pd.Series):
            observations = observations.tolist()

        conditions = np.array(conditions)
        observations = np.array(observations)

        # add actions[t] and rewards[t] to conditions and actions[t+1] to observations
        conditions, observations = _reformat_experiment_data(conditions, observations)

        self.rnn = rnn_main(
            conditions,
            observations,
            self.rnn,
        )

        self.sindy = sindy_main(
            conditions,
            observations,
            self.rnn,
            self.sindy,
            self.library_setup,
            self.datafilter_setup,
            self.library,
            self.threshold,
            self.polynomial_degree,
            self.regularization,
            self.sindy_ensemble,
            self.library_ensemble,
        )

        return self

    def predict(self,
                conditions: Union[pd.DataFrame, np.ndarray],
                deterministic: bool = True,
                reset_agent: bool = True,
                ) -> Union[pd.DataFrame, np.ndarray]:

        # shape of conditions: (n_trials, n_features)
        # with features = (action, reward)

        if reset_agent:
            self.sindy.new_sess()

        predictions = np.zeros((len(conditions), self.n_actions))
        # value_updates_collected = {}
        for trial in range(len(conditions)):
            # predictions[trial] = self.sindy.get_choice(deterministic)
            predictions[trial] = self.sindy.get_choice_probs(deterministic)

            value_updates = self.sindy.update(int(conditions[trial, 0]),
                                              float(conditions[trial, 1]))

            actions, rewards = int(conditions[trial, :-1]), float(conditions[trial, -1])
            value_updates = self.sindy.update(actions, rewards)

        return predictions


def _reformat_experiment_data(conditions, observations):
    """
    Examples:
        >>> _conditions = [np.array([[0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [1, 0]])]
        >>> _observations =[np.array([[0, 1], [0, 1], [1, 0], [1, 0], [1, 0], [1, 0]])]
        >>> c, o = _reformat_experiment_data(_conditions, _observations)
        >>> c

    """
    conditions = np.array(conditions)
    observations = np.array(observations)

    # Create the masked conditions by extracting elements where observations are 1
    masked_conditions = np.where(observations == 1, conditions, np.nan)

    # Flattening and removing NaNs
    flattened_masked_conditions = masked_conditions[~np.isnan(masked_conditions)].reshape(
        masked_conditions.shape[0], masked_conditions.shape[1], -1)

    # Concatenate the observations with the masked conditions along the feature axis
    combined_conditions = np.concatenate([observations, flattened_masked_conditions], axis=2)

    # Removing the last trial from conditions and the first trial from observations
    conditions = combined_conditions[:, :-1]
    observations = observations[:, 1:]

    return conditions, observations
