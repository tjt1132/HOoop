"""file: generator.py"""
import math

class Generator(object):
    """Generator object. Generates a signal."""

    def __init__(self,
                 signal_amplitude,
                 signal_phase,
                 signal_frecuency,
                 signal_noise):
        """Generator constructor."""

        self.signal_amplitude = signal_amplitude
        self.signal_phase = signal_phase
        self.signal_frecuency = signal_frecuency
        self.signal_noise = signal_noise

        self.sampling_frequency = signal_frecuency * 100

        self.__corrective_value = 0

    def emit(self, time):
        """Emit signal."""
        corrective_phase = math.asin(self.__corrective_value)

        total_samples = int(time * self.sampling_frequency) + 1

        samples = range(total_samples)

        signal = [self.signal_amplitude *
                  math.sin((math.pi / (2 * 25)) *
                  self.signal_frecuency * sample +
                  self.signal_phase +
                  corrective_phase)
                  for sample in samples]

        self.__corrective_value = signal[len(signal) - 1]

        return signal
