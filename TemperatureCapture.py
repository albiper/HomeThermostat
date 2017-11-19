"""Module to read ds18b20 sensor value"""
import logging

class TemperatureCapture:
    """Class to check when activate relay"""

    @classmethod
    def get_value(cls, sensor_id, logger=None):
        logger = logger or logging.getLogger(__name__)

        try:
            location = "/sys/bus/w1/devices/%s/w1_slave" % sensor_id
            with open(location) as sensor_file:
                text = sensor_file.read()

            secondline = text.split("\n")[1]
            temperaturedata = secondline.split(" ")[9]
            temperature = float(temperaturedata[2:])
            temperature = float(temperature) / 1000

            logger.info("Current temperature %s" % temperature)

            return temperature
        except Exception as exc:
            return 100
