"""
This submodule contains classes to represent Mutual Hazard Networks
"""
# author(s): Y. Linda Hu, Stefan Vocht

from __future__ import annotations

import json
import warnings
from math import factorial
from typing import Iterator, Optional, Union

import matplotlib
import matplotlib.axes
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.core.multiarray import array as array
from scipy.linalg.blas import daxpy, dcopy, dscal

from . import utilities
from .training import likelihood_cmhn


def bits_fixed_n(n: int, k: int) -> Iterator[int]:
    """
    Generator over integers whose binary representation has a fixed number of 1s, in lexicographical order.

    From https://graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation

    :param n: How many 1s there should be
    :param k: How many bits the integer should have
    """

    v = int("1" * n, 2)
    stop_no = v << (k - n)
    w = -1
    while w != stop_no:
        t = (v | (v - 1)) + 1
        w = t | ((((t & -t)) // (v & (-v)) >> 1) - 1)
        v, w = w, v
        yield w


class cMHN:
    """
    This class represents a classical Mutual Hazard Network.
    """

    def __init__(self, log_theta: np.array,
                 events: list[str] = None, meta: dict = None):
        """
        :param log_theta: logarithmic values of the theta matrix representing the cMHN
        :param events: (optional) list of strings containing the names of the events considered by the cMHN
        :param meta: (optional) dictionary containing metadata for the cMHN, e.g. parameters used to train the model
        """
        n = log_theta.shape[1]
        self.log_theta = log_theta
        if events is not None and len(events) != n:
            raise ValueError(
                f"the number of events ({len(events)}) does not align with the shape of log_theta ({n}x{n})")
        self.events = events
        self.meta = meta

    def sample_artificial_data(
            self, sample_num: int, as_dataframe: bool = False) -> np.ndarray | pd.DataFrame:
        """
        Returns artificial data sampled from this cMHN. Random values are generated with numpy, use np.random.seed()
        to make results reproducible.

        :param sample_num: number of samples in the generated data
        :param as_dataframe: if True, the data is returned as a pandas DataFrame, else as a numpy matrix

        :returns: array or DataFrame with samples as rows and events as columns
        """
        art_data = utilities.sample_artificial_data(
            self.log_theta, sample_num)
        if as_dataframe:
            df = pd.DataFrame(art_data)
            if self.events is not None:
                df.columns = self.events
            return df
        else:
            return art_data

    def sample_trajectories(self, trajectory_num: int, initial_state: np.ndarray | list[str],
                            output_event_names: bool = False) -> tuple[list[list[int | str]], np.ndarray]:
        """
        Simulates event accumulation using the Gillespie algorithm. Random values are generated with numpy, use np.random.seed()
        to make results reproducible.

        :param trajectory_num: Number of trajectories sampled by the Gillespie algorithm
        :param initial_state: Initial state from which the trajectories start. Can be either a numpy array containing 0s and 1s, where each entry represents an event being present (1) or not (0),
        or a list of strings, where each string is the name of an event. The later can only be used if events were specified during creation of the cMHN object.
        :param output_event_names: If True, the trajectories are returned as lists containing the event names, else they contain the event indices

        :return: A tuple: first element as a list of trajectories, the second element contains the observation times of each trajectory
        """
        if type(initial_state) is np.ndarray:
            initial_state = initial_state.astype(np.int32)
            if initial_state.size != self.log_theta.shape[1]:
                raise ValueError(
                    f"The initial state must be of size {self.log_theta.shape[1]}")
            if not set(initial_state.flatten()).issubset({0, 1}):
                raise ValueError(
                    "The initial state array must only contain 0s and 1s")
        else:
            init_state_copy = list(initial_state)
            initial_state = np.zeros(self.log_theta.shape[1], dtype=np.int32)
            if len(init_state_copy) != 0 and self.events is None:
                raise RuntimeError(
                    "You can only use event names for the initial state, if event was set during initialization of the cMHN object"
                )

            for event in init_state_copy:
                index = self.events.index(event)
                initial_state[index] = 1

        trajectory_list, observation_times = utilities.gillespie(
            self.log_theta, initial_state, trajectory_num)

        if output_event_names:
            if self.events is None:
                raise ValueError(
                    "output_event_names can only be set to True, if events was set for the cMHN object")
            trajectory_list = list(map(
                lambda trajectory: list(map(
                    lambda event: self.events[event],
                    trajectory
                )),
                trajectory_list
            ))

        return trajectory_list, observation_times

    def compute_marginal_likelihood(self, state: np.ndarray) -> float:
        """
        Computes the likelihood of observing a given state, where we consider the observation time to be an
        exponential random variable with mean 1.

        :param state: a 1d numpy array (dtype=np.int32) containing 0s and 1s, where each entry represents an event being present (1) or not (0)

        :returns: the likelihood of observing the given state according to this cMHN
        """
        if not set(state.flatten()).issubset({0, 1}):
            raise ValueError("The state array must only contain 0s and 1s")
        mutation_num = np.sum(state)
        nx = 1 << mutation_num
        p0 = np.zeros(nx)
        p0[0] = 1
        p_th = likelihood_cmhn.compute_restricted_inverse(
            self.log_theta, state, p0, False)
        return p_th[-1]

    def compute_next_event_probs(self, state: np.ndarray, as_dataframe: bool = False,
                                 allow_observation: bool = False) -> np.ndarray | pd.DataFrame:
        """
        Compute the probability for each event that it will be the next one to occur given the current state.

        :param state: a 1d numpy array (dtype=np.int32) containing 0s and 1s, where each entry represents an event being present (1) or not (0)
        :param as_dataframe: if True, the result is returned as a pandas DataFrame, else as a numpy array
        :param allow_observation: if True, the observation event can happen before any other event -> observation probability included in the output

        :returns: array or DataFrame that contains the probability for each event that it will be the next one to occur

        :raise ValueError: if the number of events in state does not align with the number of events modeled by this cMHN object
        """
        n = self.log_theta.shape[1]
        if n != state.shape[0]:
            raise ValueError(
                f"This cMHN object models {n} events, but state contains {state.shape[0]}")
        if allow_observation:
            observation_rate = self._get_observation_rate(state)
        else:
            observation_rate = 0
        result = utilities.compute_next_event_probs(
            self.log_theta, state, observation_rate)
        if allow_observation:
            result = np.concatenate((result, [1 - result.sum()]))
        if not as_dataframe:
            return result
        df = pd.DataFrame(result)
        df.columns = ["PROBS"]
        if self.events is not None:
            df.index = self.events + \
                (["Observation"] if allow_observation else [])
        return df

    def _get_observation_rate(self, state: np.ndarray) -> float:
        return 1.

    def order_likelihood(self, sigma: tuple[int]) -> float:
        """Marginal likelihood of an order of events.

        Args:
            sigma (tuple[int]): Tuple of integers where the integers represent the events.

        Returns:
            float: Marginal likelihood of observing sigma.
        """
        events = np.zeros(self.log_theta.shape[0], dtype=np.int32)
        sigma = np.array(sigma)
        events[sigma] = 1
        pos = np.argsort(np.argsort(sigma))
        restr_diag = self.get_restr_diag(state=events)
        return np.exp(sum((self.log_theta[x_i, sigma[:n_i]].sum() + self.log_theta[x_i, x_i]) for n_i, x_i in enumerate(sigma))) \
            / np.prod([1 - restr_diag[(1 << pos)[:i].sum()] for i in range(len(sigma) + 1)])

    def likeliest_order(self, state: np.array,
                        normalize: bool = False) -> tuple[float, np.array]:
        """Returns the likeliest order in which a given state accumulated according to the MHN.

        Args:
            state (np.array):  State (binary, dtype int32), shape (n,) with n the number of total
            events.
            normalize (bool, optional): Whether to normalize among all possible accumulation orders.
            Defaults to False.

        Returns:
            tuple[float, np.array]: Likelihood of the likeliest accumulation order and the order itself.
        """
        restr_diag = self.get_restr_diag(state=state)
        log_theta = self.log_theta[state.astype(bool)][:, state.astype(bool)]

        k = state.sum()
        # {state: highest path probability to this state}
        A = {0: 1 / (1 - restr_diag[0])}
        # {state: path with highest probability to this state}
        B = {0: []}
        for i in range(1, k + 1):         # i is the number of events
            A_new = dict()
            B_new = dict()
            for st in bits_fixed_n(n=i, k=k):
                A_new[st] = -1
                state_events = np.array(
                    [i for i in range(k) if (1 << i) | st == st])  # events in state
                for e in state_events:
                    # numerator in Gotovos formula
                    num = np.exp(log_theta[e, state_events].sum())
                    pre_st = st - (1 << e)
                    if A[pre_st] * num > A_new[st]:
                        A_new[st] = A[pre_st] * num
                        B_new[st] = B[pre_st].copy()
                        B_new[st].append(e)
                A_new[st] /= (1 - restr_diag[st])
            A = A_new
            B = B_new
        i = (1 << k) - 1
        if normalize:
            A[i] /= self.compute_marginal_likelihood(state=state)
        return (A[i], np.arange(self.log_theta.shape[0])
                [state.astype(bool)][B[i]])

    def m_likeliest_orders(self, state: np.array, m: int,
                           normalize: bool = False) -> tuple[np.array, np.array]:
        """Returns the m likeliest orders in which a given state accumulated according to the MHN.

        Args:
            state (np.array):  State (binary, dtype int32), shape (n,) with n the number of total
            events.
            m (int): Number of likeliest orders to compute.
            normalize (bool, optional): Whether to normalize among all possible accumulation orders.
            Defaults to False.

        Returns:
            tuple[np.array, np.array]: Array of likelihoods of the likeliest accumulation order and
            array of the order itself.
        """
        restr_diag = self.get_restr_diag(state=state)
        log_theta = self.log_theta[state.astype(bool)][:, state.astype(bool)]

        k = state.sum()
        # {state: highest path probability to this state}
        A = {0: np.array(1 / (1 - restr_diag[0]))}
        # {state: path with highest probability to this state}
        B = {0: np.empty(0, dtype=int)}
        for i in range(
                1, k + 1):                     # i is the number of events
            _m = min(factorial(i - 1), m)
            A_new = dict()
            B_new = dict()
            for st in bits_fixed_n(n=i, k=k):
                A_new[st] = np.zeros(i * _m)
                B_new[st] = np.zeros((i * _m, i), dtype=int)
                state_events = np.array(
                    [i for i in range(k) if 1 << i | st == st])  # events in state
                for j, e in enumerate(state_events):
                    # numerator in Gotovos formula
                    num = np.exp(log_theta[e, state_events].sum())
                    pre_st = st - (1 << e)
                    A_new[st][j * _m: (j + 1) * _m] = num * A[pre_st]
                    B_new[st][j * _m: (j + 1) * _m, :-1] = B[pre_st]
                    B_new[st][j * _m: (j + 1) * _m, -1] = e
                sorting = A_new[st].argsort()[::-1][:m]
                A_new[st] = A_new[st][sorting]
                B_new[st] = B_new[st][sorting]
                A_new[st] /= (1 - restr_diag[st])
            A = A_new
            B = B_new
        i = (1 << k) - 1
        if normalize:
            A[i] /= self.compute_marginal_likelihood(state=state)
        return (A[i], (np.arange(self.log_theta.shape[0])[
                state.astype(bool)])[B[i].flatten()].reshape(-1, k))

    def save(self, filename: str):
        """
        Save the cMHN in a CSV file. If metadata is given, it will be stored in a separate JSON file.

        :param filename: name of the CSV file, JSON will be named accordingly
        """
        pd.DataFrame(self.log_theta, columns=self.events,
                     index=self.events).to_csv(f"{filename}")
        if self.meta is not None:
            json_serializable_meta = {}
            # check if objects in self.meta are JSON serializable, if not,
            # convert them to a string
            for meta_key, meta_value in self.meta.items():
                try:
                    json.dumps(meta_value)
                    json_serializable_meta[meta_key] = meta_value
                except TypeError:
                    json_serializable_meta[meta_key] = str(meta_value)
            with open(f"{filename[:-4]}_meta.json", "w") as file:
                json.dump(json_serializable_meta, file, indent=4)

    @classmethod
    def load(cls, filename: str, events: list[str] = None) -> cMHN:
        """
        Load an cMHN object from a CSV file.

        :param filename: name of the CSV file
        :param events: list of strings containing the names of the events considered by the cMHN

        :returns: cMHN object
        """
        df = pd.read_csv(f"{filename}", index_col=0)
        if events is None and (df.columns != pd.Index(
                [str(x) for x in range(len(df.columns))])).any():
            events = df.columns.to_list()
        try:
            with open(f"{filename[:-4]}_meta.json", "r") as file:
                meta = json.load(file)
        except FileNotFoundError:
            meta = None
        return cls(np.array(df), events=events, meta=meta)

    def get_restr_diag(self, state: np.array) -> np.array:
        """Get the diagonal of the state-space-restricted Q_Theta matrix.

        Args:
            state (np.array): State (binary, dtype int32) which should be considered for the
            state space restriction. Shape (n,) with n the number of total events.

        Returns:
            np.array: Diagonal of the state-space-restricted Q_Theta matrix. Shape (2^k,) with
            k the number of 1s in state
        """
        k = state.sum()
        nx = 1 << k
        n = self.log_theta.shape[0]
        diag = np.zeros(nx)
        subdiag = np.zeros(nx)

        for i in range(n):

            current_length = 1
            subdiag[0] = 1
            # compute the ith subdiagonal of Q
            for j in range(n):
                if state[j]:
                    exp_theta = np.exp(self.log_theta[i, j])
                    if i == j:
                        exp_theta *= -1
                        dscal(n=current_length, a=exp_theta, x=subdiag, incx=1)
                        dscal(n=current_length, a=0,
                              x=subdiag[current_length:], incx=1)
                    else:
                        dcopy(n=current_length, x=subdiag, incx=1,
                              y=subdiag[current_length:], incy=1)
                        dscal(n=current_length, a=exp_theta,
                              x=subdiag[current_length:], incx=1)

                    current_length *= 2

                elif i == j:
                    exp_theta = - np.exp(self.log_theta[i, j])
                    dscal(n=current_length, a=exp_theta, x=subdiag, incx=1)

            # add the subdiagonal to dg
            daxpy(n=nx, a=1, x=subdiag, incx=1, y=diag, incy=1)
        return diag

    def __str__(self):
        if isinstance(self.meta, dict):
            meta_data_string = '\n'.join(
                [f'{key}:\n{value}\n' for key, value in self.meta.items()])
        else:
            meta_data_string = "None"
        return f"EVENTS: \n{self.events}\n\n" \
               f"THETA IN LOG FORMAT: \n {self.log_theta}\n\n" \
               f"ADDITIONAL METADATA: \n\n{meta_data_string}"

    def plot(
            self,
            cmap_thetas: Union[str, matplotlib.colors.Colormap] = "RdBu_r",
            cmap_brs: Union[str, matplotlib.colors.Colormap] = "Greens",
            colorbar: bool = True,
            annot: Union[float, bool] = 0.1,
            ax: Optional[np.arraymatplotlib.axes.Axes] = None,
            logarithmic: bool = True
    ) -> tuple[matplotlib.image.AxesImage, matplotlib.image.AxesImage, matplotlib.colorbar.Colorbar, matplotlib.colorbar.Colorbar] | tuple[matplotlib.image.AxesImage, matplotlib.image.AxesImage]:
        """
        Plots the theta matrix.

        Args:
            cmap_thetas (Union[str, matplotlib.colors.Colormap], optional):
                Colormap to use for thetas. Defaults to "RdBu_r".
            cmap_brs (Union[str, matplotlib.colors.Colormap], optional):
                Colormap to use for the base rates. Defaults to "Greens".
            colorbar (bool, optional):
                Whether to display the colorbars. Defaults to True.
            annot (Union[float, bool], optional):
                If boolean, either all or no annotations are displayed. If numerical, displays
                annotations for all effects greater than this threshold in the logarithmic theta matrix.
                Defaults to 0.1.
            ax (Optional[matplotlib.axes.Axes], optional):
                Matplotlib axes to plot on. Defaults to None.
            logarithmic (bool, optional):
                If set to True, plots the logarithmic theta matrix, else plots the exponential theta matrix.
                Defaults to True.

        Returns:
            tuple[matplotlib.image.AxesImage, matplotlib.image.AxesImage, matplotlib.colorbar.Colorbar, matplotlib.colorbar.Colorbar] | tuple[matplotlib.image.AxesImage, matplotlib.image.AxesImage]:
                If colorbar is True, returns the two heatmaps and the two colorbars. Else, returns only the two axes images.
        """

        # raise warning that the threshold is applied to the logarithmic values
        if isinstance(annot, float) and not logarithmic:
            warnings.warn(
                f"The annotation threshold of {annot} is applied to the logarithmic theta, not the exponential values. " +
                f"thetas with |exp(theta)| < {annot} are hidden.")

        # configure basic plot setup
        n_col = 3 if colorbar else 2
        dim_theta_0 = self.log_theta.shape[0]
        dim_theta_1 = self.log_theta.shape[1]
        figsize = (
            dim_theta_1 * 0.35 +
            (3.2 if colorbar else 1.8),
            dim_theta_0 * 0.35 + 1)
        width_ratios = [4, dim_theta_1 + 6,
                        3] if colorbar else [4, dim_theta_1 + 3]

        # create axes object if not provided
        if ax is None:
            _, ax = plt.subplots(
                1, n_col,
                figsize=figsize,
                width_ratios=width_ratios,
                sharey=True,
                layout="tight")
        else:
            # check if ax is n_col dimensional
            if not isinstance(ax, np.ndarray) or ax.shape != (n_col,):
                # warn and create new axes object
                warnings.warn(
                    f"Provided axes object is not {n_col}-dimensional, creating new axes object")
                _, ax = plt.subplots(
                    1, n_col,
                    figsize=figsize,
                    width_ratios=width_ratios,
                    sharey=True,
                    layout="tight")

        # name axes
        ax_brs, ax_theta = ax[:2]

        # get base rates
        base_rates = np.diag(self.log_theta).reshape(-1, 1)
        if not logarithmic:
            base_rates = np.exp(base_rates)

        # plot thetas
        if logarithmic:
            _max_th = np.abs(self.log_theta).max()
            theta = self.log_theta.copy()
            np.fill_diagonal(theta, 0)
            im_brs = ax_brs.imshow(
                base_rates,
                cmap=cmap_brs)
            im_thetas = ax_theta.imshow(
                theta,
                cmap=cmap_thetas,
                vmin=-_max_th, vmax=_max_th)
        else:
            _max_th = np.exp(
                np.abs(self.log_theta - np.diag(self.log_theta)).max())
            _max_br = np.exp(np.abs(np.diag(self.log_theta)).max())
            theta = np.exp(self.log_theta)
            np.fill_diagonal(theta, 1)
            im_brs = ax_brs.imshow(
                base_rates,
                norm=colors.LogNorm(vmin=1 / _max_br, vmax=_max_br),
                cmap=cmap_brs)
            im_thetas = ax_theta.imshow(
                theta,
                norm=colors.LogNorm(vmin=1 / _max_th, vmax=_max_th),
                cmap=cmap_thetas)

        # style the plot ticks
        ax_brs.tick_params(length=0)
        ax_brs.set_yticks(
            np.arange(0, dim_theta_0, 1),
            (self.events or list(range(dim_theta_1))) +
            (["Observation"] if
             dim_theta_0 == dim_theta_1 + 1
             else []))
        ax_brs.set_xticks([0], ["Base Rate"])
        ax_brs.tick_params(axis="x", rotation=90)

        ax_theta.tick_params(length=0)
        ax_theta.set_yticks(
            np.arange(0, dim_theta_0, 1),
            (self.events or list(range(dim_theta_1))) +
            (["Observation"] if
             dim_theta_0 == dim_theta_1 + 1
             else []))
        ax_theta.set_xticks(
            np.arange(0, dim_theta_1, 1),
            self.events)
        ax_theta.tick_params(axis="x", rotation=90)

        ax_theta.set_ylim((dim_theta_0 - 0.5, -0.5))

        # add annotations
        if annot:
            for i in range(dim_theta_1):
                _ = ax_brs.text(
                    0, i, np.around(base_rates[i, 0], decimals=2),
                    ha="center", va="center", fontsize=8)
            for i in range(dim_theta_0):
                for j in range(dim_theta_1):
                    if not i == j and \
                            (annot is True
                             or np.abs(self.log_theta[i, j]) >= annot):
                        _ = ax_theta.text(
                            j, i, np.around(theta[i, j], decimals=2),
                            ha="center", va="center", fontsize=8)

        # add colorbars
        if colorbar:
            ax_cbar = ax[2]
            ax_cbar.axis("off")
            cbar_brs = plt.colorbar(
                im_brs, ax=ax_cbar, orientation="horizontal", aspect=3)
            cbar_thetas = plt.colorbar(
                im_thetas, ax=ax_cbar, orientation="horizontal", aspect=3)

        if colorbar:
            return im_brs, im_thetas, cbar_thetas, cbar_brs
        else:
            return im_brs, im_thetas


class oMHN(cMHN):
    """
    This class represents an oMHN.
    """

    def sample_artificial_data(
            self, sample_num: int, as_dataframe: bool = False) -> np.ndarray | pd.DataFrame:
        """
        Returns artificial data sampled from this oMHN. Random values are generated with numpy, use np.random.seed()
        to make results reproducible.

        :param sample_num: number of samples in the generated data
        :param as_dataframe: if True, the data is returned as a pandas DataFrame, else numpy matrix

        :returns: array or DataFrame with samples as rows and events as columns
        """
        return self.get_equivalent_classical_mhn(
        ).sample_artificial_data(sample_num, as_dataframe)

    def compute_marginal_likelihood(self, state: np.ndarray) -> float:
        """
        Computes the likelihood of observing a given state, where we consider the observation time to be an
        exponential random variable with mean 1.

        :param state: a 1d numpy array (dtype=np.int32) containing 0s and 1s, where each entry represents an event being present (1) or not (0)

        :returns: the likelihood of observing the given state according to this oMHN
        """
        return self.get_equivalent_classical_mhn().compute_marginal_likelihood(state)

    def get_equivalent_classical_mhn(self) -> cMHN:
        """
        This method returns a classical cMHN object that represents the same distribution as this oMHN object.

        :returns: classical cMHN object representing the same distribution as this oMHN object
        """
        n = self.log_theta.shape[1]
        # subtract observation rates from each element in each column
        equivalent_classical_mhn = self.log_theta[:-1] - self.log_theta[-1]
        # undo changes to the diagonal
        equivalent_classical_mhn[range(n), range(n)] += self.log_theta[-1]
        return cMHN(equivalent_classical_mhn, self.events, self.meta)

    def _get_observation_rate(self, state: np.ndarray) -> float:
        return np.exp(np.sum(self.log_theta[-1, state != 0]))

    def save(self, filename: str):
        """
        Save the oMHN in a CSV file. If metadata is given, it will be stored in a separate JSON file.

        :param filename: name of the CSV file, JSON will be named accordingly
        """
        if self.events is None:
            events_and_observation_labels = None
        else:
            events_and_observation_labels = self.events + ["Observation"]
        pd.DataFrame(self.log_theta, columns=self.events,
                     index=events_and_observation_labels).to_csv(f"{filename}")
        if self.meta is not None:
            json_serializable_meta = {}
            # check if objects in self.meta are JSON serializable, if not,
            # convert them to a string
            for meta_key, meta_value in self.meta.items():
                try:
                    json.dumps(meta_value)
                    json_serializable_meta[meta_key] = meta_value
                except TypeError:
                    json_serializable_meta[meta_key] = str(meta_value)
            with open(f"{filename[:-4]}_meta.json", "w") as file:
                json.dump(json_serializable_meta, file, indent=4)

    def order_likelihood(self, sigma: tuple[int]) -> float:
        """Marginal likelihood of an order of events.

        Args:
            sigma (tuple[int]): Tuple of integers where the integers represent the events.

        Returns:
            float: Marginal likelihood of observing sigma.
        """
        return self.get_equivalent_classical_mhn().order_likelihood(sigma)

    def likeliest_order(self, state: np.array,
                        normalize: bool = False) -> tuple[float, np.array]:
        """Returns the likeliest order in which a given state accumulated according to the MHN.

        Args:
            state (np.array):  State (binary, dtype int32), shape (n,) with n the number of total
            events.
            normalize (bool, optional): Whether to normalize among all possible accumulation orders.
            Defaults to False.

        Returns:
            tuple[float, Any]: Likelihood of the likeliest accumulation order and the order itself.
        """
        return self.get_equivalent_classical_mhn().likeliest_order(state, normalize)

    def m_likeliest_orders(self, state: np.array, m: int,
                           normalize: bool = False) -> tuple[np.array, np.array]:
        """Returns the m likeliest orders in which a given state accumulated according to the MHN.

        Args:
            state (np.array):  State (binary, dtype int32), shape (n,) with n the number of total
            events.
            m (int): Number of likeliest orders to compute.
            normalize (bool, optional): Whether to normalize among all possible accumulation orders.
            Defaults to False.

        Returns:
            tuple[np.array, np.array]: Array of likelihoods of the likeliest accumulation order and
            array of the order itself.
        """
        return self.get_equivalent_classical_mhn().m_likeliest_orders(state, m, normalize)
