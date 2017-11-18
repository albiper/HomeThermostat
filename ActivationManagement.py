"""Module to check when activate relay"""
import datetime

from TemperatureCapture import TemperatureCapture

class ActivationManagement:
    """Class to check when activate relay"""

    @classmethod
    def Check(cls, db, sensor_id):
        schedule = db.get_current_schedule()

        if schedule is None:
            return False

        currentTemperature = TemperatureCapture.get_value(sensor_id)

        if currentTemperature < schedule[0]:
            return True
        else:
            return False
