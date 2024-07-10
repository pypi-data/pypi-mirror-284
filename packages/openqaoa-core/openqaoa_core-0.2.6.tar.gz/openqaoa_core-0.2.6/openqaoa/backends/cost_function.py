# Cost function to be used for QAOA training
from typing import Dict
import numpy as np

from ..qaoa_components import Hamiltonian
from ..utilities import bitstring_energy


def expectation_value_classical(counts: Dict, hamiltonian: Hamiltonian):
    """
    Evaluate the cost function, i.e. expectation value ``$$\langle|H \rangle$$``
    w.r.t to the measurements results ``counts``.

    Parameters
    ----------
    counts: dict
                The counts of the measurements.
    hamiltonian: Hamiltonian
                The Cost Hamiltonian defined for the optimization problem
    """
    shots = sum(counts.values())
    cost = 0
    for basis_state, count in counts.items():
        cost += count * (bitstring_energy(hamiltonian, basis_state) / shots)
    return cost


def cvar_expectation_value_classical(
    counts: Dict, hamiltonian: Hamiltonian, alpha: float
):
    """
    CVaR computation of cost function. For the definition of the cost function, refer
    to https://arxiv.org/abs/1907.04769.

    Parameters
    ----------
    counts: `dict`
            The counts of the measurements.
    hamiltonian: `Hamiltonian`
            The Cost Hamiltonian defined for the optimization problem
    alpha: `float`
            The CVaR parameter.
    """
    assert alpha > 0 and alpha < 1, "Please specify a valid alpha value between 0 and 1"
    shots = sum(counts.values())

    cost_list = []

    # eigen-energy computation of each basis state in counts
    for basis_state, count in counts.items():
        cost_list.append(count * (bitstring_energy(hamiltonian, basis_state) / shots))

    # sort costs in ascending order
    sorted_cost_list = np.sort(np.array(cost_list))

    K = max([int(len(cost_list) * alpha), 1])
    cost = sum(sorted_cost_list[:K])

    return cost


def cost_function(counts: Dict, hamiltonian: Hamiltonian, alpha: float = 1):
    """
    The cost function to be used for QAOA training.

    Parameters
    ----------
    counts: `dict`
            The counts of the measurements.
    hamiltonian: `Hamiltonian`
            The Cost Hamiltonian defined for the optimization problem
    alpha: `float`
            The CVaR parameter.
    """
    if alpha == 1:
        return expectation_value_classical(counts, hamiltonian)
    else:
        return cvar_expectation_value_classical(counts, hamiltonian, alpha)
