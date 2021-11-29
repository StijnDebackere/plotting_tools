def set_spines_labels(
        ax, left=True, right=True, top=True, bottom=True,
        labels=False):
    """Remove the spines of the given axes instance and modify the labels."""
    ax.spines["left"].set_visible(left)
    ax.spines["right"].set_visible(right)
    ax.spines["top"].set_visible(top)
    ax.spines["bottom"].set_visible(bottom)

    ax.axes.xaxis.set_visible(bottom & labels)
    ax.axes.yaxis.set_visible(left & labels)

    ax.tick_params(
        left=left & labels, right=right & labels,
        top=top & labels, bottom=bottom & labels,
        which="both"
    )
    ax.patch.set_alpha(0)
    return ax
