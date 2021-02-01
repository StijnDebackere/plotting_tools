from functools import wraps

import matplotlib.pyplot as plt


def light_or_dark(light=True):
    def wrapper(func):
        @wraps(func)
        def plot(*args, **kwargs):
            paper_style(light=light)
            func(*args, **kwargs)

        return plot
    return wrapper


def paper_style(light=True):
    joint_params = {
        #### Text
        "font.family" : "serif",
        "font.weight" : "normal",
        "font.size"   : 30.0,
        "font.serif"  : "Times New Roman",

        #### LaTeX customizations. See http://wiki.scipy.org/Cookbook/Matplotlib/UsingTex
        "text.usetex" : False,
        "mathtext.rm"  : "Times New Roman",
        "mathtext.tt"  : "t1xtt",
        "mathtext.it"  : "Times New Roman:italic",
        "mathtext.bf"  : "Times New Roman:bold",
        "mathtext.fontset" : "custom",
        "mathtext.fallback" : "cm",

        #### Axes
        "axes.titlesize"   : 30,
        "axes.labelsize"   : 30,
        "axes.labelpad"    : 10,
        "axes.labelweight" : "normal",

        #### Ticks
        "xtick.top" : True,
        "xtick.bottom" : True,
        "xtick.labeltop" : False,
        "xtick.labelbottom" : True,
        "xtick.major.size" : 6,
        "xtick.minor.size" : 4,
        "xtick.major.pad" : 10,
        "xtick.minor.pad" : 3.4,
        "xtick.labelsize" : 30,
        "xtick.direction" : "in",
        "xtick.minor.visible" : True,
        "xtick.major.top" : True,
        "xtick.major.bottom" : True,
        "xtick.minor.top" : True,
        "xtick.minor.bottom" : True,
        "xtick.alignment" : "center",

        "ytick.left" : True,
        "ytick.right" : True,
        "ytick.labelleft" : True,
        "ytick.labelright" : False,
        "ytick.major.size" : 6,
        "ytick.minor.size" : 4,
        "ytick.major.pad" : 3.5,
        "ytick.minor.pad" : 3.4,
        "ytick.labelsize" : 30,
        "ytick.direction" : "in",
        "ytick.minor.visible" : True,
        "ytick.major.left" : True,
        "ytick.major.right" : True,
        "ytick.minor.left" : True,
        "ytick.minor.right" : True,
        "ytick.alignment" : "center_baseline",

        #### Legend
        "legend.loc"            : "best",
        "legend.frameon"        : False,
        "legend.numpoints"      : 1,
        "legend.scatterpoints"  : 1,
        "legend.fontsize"       : 30,
        "legend.title_fontsize" : None,

        #### Figure
        "figure.titlesize" : 34,
        "figure.figsize"   : (10, 9),

        #### Images
        "image.aspect" : "equal",
        "image.interpolation"  : "none",
        "image.cmap"   : "magma",
        "image.origin" : "lower",

        #### Errorbar plots
        "errorbar.capsize" : 0,

        #### Saving figures
        "savefig.transparent" : True
    }
    if light:
        color_params = {
            ### Ticks
            "xtick.color" : "black",
            "ytick.color" : "black",

            ### Axes
            "axes.labelcolor": "black",
            "axes.edgecolor" : "black",
            "grid.color" : "black",

            ### Boxplots
            "boxplot.boxprops.color" : "black",
            "boxplot.capprops.color" : "black",
            "boxplot.flierprops.color" : "black",
            "boxplot.flierprops.markeredgecolor" : "black",
        }

    else:
        color_params = {
            ### Ticks
            "xtick.color" : "white",
            "ytick.color" : "white",

            ### Axes
            "axes.labelcolor": "white",
            "axes.edgecolor" : "white",
            "grid.color" : "white",

            ### Boxplots
            "boxplot.boxprops.color" : "white",
            "boxplot.capprops.color" : "white",
            "boxplot.flierprops.color" : "white",
            "boxplot.flierprops.markeredgecolor" : "white",
        }

    plt.style.use({**joint_params, **color_params})
