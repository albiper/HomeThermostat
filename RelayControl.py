"""Module to control relay"""
import logging

from Utilities import set_gpio_pin_status
from Utilities import get_gpio_pin_status


class RelayControl:
    """Class to control relay"""

    def __init__(self, out_pin=18, logger=None):
        #super(RelayControl, self).__init__()
        self.out_pin = out_pin
        self.logger = logger or logging.getLogger(__name__)

    def change_status(self):
        """Changes the status of the relay"""
        set_gpio_pin_status(self.out_pin, not get_gpio_pin_status(self.out_pin))

    def set_status_high(self):
        set_gpio_pin_status(self.out_pin, 1)

    def set_status_low(self):
        set_gpio_pin_status(self.out_pin, 0)

    def set_status(self, desired_value):
        set_gpio_pin_status(self.out_pin, int(desired_value))
