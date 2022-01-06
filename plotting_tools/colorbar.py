import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import plotting_tools.tools as tools


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


def get_partial_cmap_mappable(
        cmap, norm=mpl.colors.Normalize, a=0.25, b=1, **norm_kwargs
):
    """Return cmap mapping values between vmin and vmax."""
    partial_cmap = get_partial_cmap(cmap=cmap, a=a, b=b)
    sm = plt.cm.ScalarMappable(norm=norm(**norm_kwargs), cmap=partial_cmap)
    cmap = sm.to_rgba

    return cmap


def add_colorbar_indexed(
        cmap_indexed,
        items,
        fig=None,
        ax_cb=None,
        tick_positions='centers',
        ticks=None,
        **cbar_kwargs,
):
    """Put the colorbar with cmap_indexed over items in ax_cb.

    Parameters
    ----------
    cmap_indexed : matplotlib.colors.Colormap
        color map
    items : array-like
        range of values in cmap_indexed
    fig : matplotlib.Figure
        figure for plotting
    ax_cb : matplotlib.axes.Axes
        axes to draw colorbar in
    tick_positions : Optional[str] 'centers', 'edges' or None
        put items as discrete ticks at centers or edges of colors
    ticks : Optional[array-like]
        ticks to draw, ignored if tick_options is set
    cbar_kwargs : dict
        kwargs for Colorbar

    Returns
    -------
    matplotlib.Colorbar : colorbar instance
    """
    ticks_options = ['centers', 'edges', None]
    if tick_positions not in ticks_options:
        raise ValueError(f'tick_positions should be one of {ticks_options}')

    ticks = None
    bounds = None
    ticklabels = None
    norm = None

    # plot items as discrete colors with tick centred in colors
    if tick_positions == 'centers':
        if cmap_indexed.N != len(items):
            raise ValueError(f"{cmap_indexed.N=} should match {len(items)=}")

        # use item index as colormap index
        vmin, vmax = 0, len(items) - 1
        norm = mpl.colors.NoNorm(vmin=vmin, vmax=vmax)

        # put tick in middle of range for each item
        ticks = np.arange(vmin + 0.5, vmax + 1.5, 1)
        bounds = np.arange(0, vmax + 2, 1)
        ticklabels = items

    # see https://matplotlib.org/stable/tutorials/colors/colorbar_only.html
    # plot items as edges of colors in colorbar
    elif tick_positions == 'edges':
        if cmap_indexed.N != len(items) - 1:
            raise ValueError(f"{cmap_indexed.N=} should match {len(items) - 1=}")

        # map data value to colormap index => color between items
        bounds = items
        ticks = items
        norm = mpl.colors.BoundaryNorm(bounds, len(items) - 1)

    # decide colorbar automatically
    elif tick_positions is None:
        norm = mpl.colors.Normalize(min(items), max(items))

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

    if ticklabels is not None:
        # still need to ensure that the actual ticklabels match
        cb.set_ticklabels(np.round(ticklabels, 2))
        cb.minorticks_off()

    return cb
