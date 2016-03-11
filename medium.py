"""file: medium.py"""

class Medium(object):
    """Medium object. Transmits signal in map. Contains targets."""

    def __init__(self, targets):
        """Medium constructor."""

        self.targets = targets

    def ping(self, signal, time):
        """Ping medium with signal."""

        detected_coordinates = []
        detected_size = []

        for target_number in range(len(self.targets)):
            if self.targets[target_number].check(signal, time):
                detected_coordinates.append(self.targets[target_number].get_coordinates())
                detected_size.append(self.targets[target_number].size)

        return (detected_size, detected_coordinates)
