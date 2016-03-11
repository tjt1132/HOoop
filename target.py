"""file: target.py"""
import random

class Target(object):
    """Target object. Targets are potentially detected by radars."""

    def __init__(self, size, personality, speed, stealth, area):
        """Target constructor."""

        self.size = size
        self.personality = personality
        self.speed = speed
        self.stealth = stealth

        self.__coordinates = [((area[1][0] - area[0][0]) *
                              random.random()) +
                              area[0][0],
                              ((area[0][1] - area[1][1]) *
                              random.random()) +
                              area[1][1]]
        self.__area_limit = area
        self.__is_detected = False

    def __reflect(self, signal, time):
        """Reflect signal with modified amplitude."""
        pass

    def __update(self, signal, time):
        """Update coordinate informacion and stealth state of target."""

        if random.random() < self.personality:
            if random.random() < 0.25:
                if self.__coordinates[0] < self.__area_limit[1][0]:
                    self.__coordinates[0] = self.__coordinates[0] + self.speed
            elif random.random() < 0.5:
                if self.__coordinates[0] > self.__area_limit[0][0]:
                    self.__coordinates[0] = self.__coordinates[0] - self.speed
            elif random.random() < 0.75:
                if self.__coordinates[1] < self.__area_limit[0][1]:
                    self.__coordinates[1] = self.__coordinates[1] + self.speed
            else:
                if self.__coordinates[1] > self.__area_limit[1][1]:
                    self.__coordinates[1] = self.__coordinates[1] - self.speed

        if random.random() > self.stealth:
            self.__is_detected = True
        else:
            self.__is_detected = False

        self.__reflect(signal, time)

    def check(self, signal, time):
        """Ceck if target is detected."""

        self.__update(signal, time)

        return self.__is_detected

    def get_coordinates(self):
        """Get target coordinates"""

        return self.__coordinates
