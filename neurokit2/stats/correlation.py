# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import scipy.stats

import matplotlib.pyplot as plt


def cor(x, y, method="pearson", show=False):
    """
    Density estimation

    Computes kernel density estimates.

    Parameters
    -----------
    x,y : list, array or Series
        Vectors of values.
    method : str
        Correlation method. Can be one of 'pearson', 'spearman', 'kendall'.
    show : bool
        Draw a scatterplot with a regression line.

    Returns
    -------
    r
        The correlation coefficient.

    Examples
    --------
    >>> import neurokit2 as nk
    >>>
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [3, 1, 5, 6, 6]
    >>> nk.cor(x, y, method="pearson", show=True)
    """
    r, p = _cor_methods(x, y, method)

    if show is True:
        _cor_plot(x, y)

    return r


# =============================================================================
# Internals
# =============================================================================
def _cor_methods(x, y, method="pearson"):
    method = method.lower()
    if method in ["pearson", "pears", "p", "r"]:
        r, p = scipy.stats.pearsonr(x, y)
    elif method in ["spearman", "spear", "s", "rho"]:
        r, p = scipy.stats.spearmanr(x, y)
    elif method in ["kendall", "kend", "k", "tau"]:
        r, p = scipy.stats.spearmanr(x, y)
    else:
        raise ValueError("NeuroKit error: cor(): 'method' not recognized.")

    return r, p



def _cor_plot(x, y):

    # Create scatter
    plt.plot(x, y, 'o')

    # Add regresion line
    m, b = np.polyfit(x, y, 1)
    plt.plot(np.array(x), m*np.array(x) + b)