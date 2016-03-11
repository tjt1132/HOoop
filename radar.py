"""file: radar.py"""

class Radar(object):
    """Radar object. Pings medium and detects targets."""

    def __init__(self, generator, detector):
        """Radar constructor."""

        self.generator = generator
        self.detector = detector
        self.targets_found = []

    def step(self, medium, time):
        """Step in time."""

        signal = self.generator.emit(time)

        self.targets_found = medium.ping(signal, time)

    def get_hits(self):
        """Get the coordinates of the found targets."""

        return self.targets_found
