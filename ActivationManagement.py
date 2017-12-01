"""Module to check when activate relay"""
import logging

from TemperatureCapture import TemperatureCapture

class ActivationManagement:
    """Class to check when activate relay"""

    @classmethod
    def Check(cls, db, sensor_id, logger=None):
        logger = logger or logging.getLogger(__name__)
        schedule = db.get_current_schedule()

        if schedule is None:
            return False

        current_temperature = TemperatureCapture.get_value(sensor_id)
        logger.info("Current temperature %s" % current_temperature)
        logger.info("Schedule temperature %s until %s" % (schedule[0], schedule[1]))

        if current_temperature < schedule[0] - float(0.5):
            return True
        elseif current_temperature < schedule[0] + float(0.5):
            return False
        else:
            retun None
