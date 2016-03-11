import matplotlib.pyplot as pp
import matplotlib.animation as animation

#import numpy as np

class Renderizer(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, scr):

        self.screen = scr
        self.stream = self.data_stream()

        # Setup the figure and axes...
        self.fig, self.ax = pp.subplots()
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=250,
                                           init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""

        #x, y = next(self.stream)
        #data = self.data_stream()
        #data = next(self.stream)

        self.scat = self.ax.scatter([], [], animated=True)
        self.ax.axis([0, 100, 0, 100])

        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def data_stream(self):
        """Generate a random walk (brownian motion). Data is scaled to produce
        a soft "flickering" effect."""

#        self.screen.step(0)
#        return self.screen.coordinate_data()
        while True:
            self.screen.step(0)
            data = self.screen.coordinate_data()
            yield data

    def update(self, i):
        """Update the scatter plot."""
        data = next(self.stream)
        #data = self.data_stream()

        # Set x and y data...
        self.scat.set_offsets(data[1])
        # Set sizes...
        self.scat._sizes = data[0]
        # Set colors..
        #self.scat.set_array(data[3])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def show(self):
        pp.show()
