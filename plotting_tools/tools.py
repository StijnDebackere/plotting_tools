import numpy as np


def bin_centers(bins, log=False):
    """Return the center position of bins, with bins along axis -1."""
    if log:
        centers = (
            (bins[..., 1:] - bins[..., :-1])
            / (np.log(bins[..., 1:]) - np.log(bins[..., :-1]))
        )
    else:
        centers = 0.5 * (bins[..., :-1] + bins[..., 1:])

    return centers
