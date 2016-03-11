"""file: screen.py"""

class Screen(object):
    """Screen object."""

    def __init__(self, radar, medium, start_time=0):
        """Class constructor."""

        self.radar = radar
        self.medium = medium
        self.current_time = start_time
        self.data = []

    def step(self, time):
        """Step forward in time."""

        self.radar.step(self.medium, time)

    def coordinate_data(self):
        """Send coordinate data."""

        return self.radar.get_hits()
