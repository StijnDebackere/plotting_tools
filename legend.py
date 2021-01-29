from matplotlib.legend_handler import HandlerTuple


class HandlerTupleVertical(HandlerTuple):
    """Return a legend handler that stacks the lines of the tuple
    vertically.

    """
    def __init__(self, **kwargs):
        HandlerTuple.__init__(self, **kwargs)

    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # How many lines are there.
        numlines = len(orig_handle)
        handler_map = legend.get_legend_handler_map()

        # divide the vertical space where the lines will go
        # into equal parts based on the number of lines
        height_y = (height / numlines)

        leglines = []
        for i, handle in enumerate(orig_handle):
            handler = legend.get_legend_handler(handler_map, handle)

            legline = handler.create_artists(
                legend, handle,
                xdescent, (2 * i + 1)*height_y,
                width, 2 * height,
                fontsize, trans
            )

            leglines.extend(legline)

        return leglines
