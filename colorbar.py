import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def get_partial_cmap(cmap, a=0.25, b=1):
    """Return cmap but sampled from a to b."""
    partial_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        f'trunc({cmap.name},{a:.2f},{b:.2f})',
        cmap(np.linspace(a, b, 256))
    )
    return partial_cmap


def get_partial_cmap_indexed(cmap, N, a=0.25, b=1):
    """Return cmap but sampled from a to b and indexed to N colors."""
    partial_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        f'trunc({cmap.name},{a:.2f},{b:.2f})',
        cmap(np.linspace(a, b, 256))
    )._resample(N)
    return partial_cmap


def add_colorbar_indexed(
        cmap_indexed, items, fig=None, ax_cb=None,
        ticks='center',
        **cbar_kwargs):
    """Put the colorbar with cmap_indexed over items in ax_cb. If ticks_at_values,
    ticks are centered on values.

    """
    ticks_options = ['center', 'bins', None]
    if ticks not in ticks_options:
        raise ValueError(f'ticks should be one of {ticks_options}')

    if ticks == 'center':
        # increment between ticks
        delta = (items[-1] - items[0]) / len(items)
        # data boundaries for the colormap
        bounds = items[0] + np.array([i * delta for i in range(len(items) + 1)])
        # map data value to colormap index
        norm = mpl.colors.BoundaryNorm(bounds, len(items))

        # center ticks within bounds and get corresponding cmap values
        ticks = tools.bin_centers(bounds)

    elif ticks == 'bins':
        # increment between ticks
        delta = (items[-1] - items[0]) / len(items)
        # data boundaries for the colormap
        bounds = items[0] + np.array([i * delta for i in range(len(items))])
        # map data value to colormap index
        norm = mpl.colors.BoundaryNorm(bounds, len(items) - 1)
        ticks = bounds

    elif ticks is None:
        norm = mpl.colors.Normalize(min(items), max(items))
        bounds = None
        ticks = None

    # get fake ScalarMappable for colorbar
    # this will convert data values to the given colormap
    sm = plt.cm.ScalarMappable(cmap=cmap_indexed, norm=norm)

    if fig is None or ax_cb is None:
        cb = plt.colorbar(
            sm, ticks=ticks, boundaries=bounds,
            **cbar_kwargs
        )

    else:
        cb = fig.colorbar(
            sm, cax=ax_cb, ticks=ticks, boundaries=bounds,
            **cbar_kwargs
        )

    if ticks is not None:
        # still need to ensure that the actual ticklabels match
        cb.set_ticklabels(np.round(items, 2))
        cb.minorticks_off()

    return cb
