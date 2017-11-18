#!/usr/bin/env python
"""This module handle cart start/stop and camera shooting """

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import time
#import datetime
import json
import logging
import logging.config
import logging.handlers
import ConfigParser
import sys

#from Queue import Queue

from Utilities import gpio_cleanup
from Utilities import set_gpio_mode
from Utilities import set_gpio_pin_mode
from Utilities import file_exists
from Utilities import set_gpio_pin_status
from DatabaseInteraction import DatabaseInteraction
from ActivationManagement import ActivationManagement
from RelayControl import RelayControl

__author__ = "Alberto Perona aka albirex"

# Defaults
CONFIGFILENAME = 'thermostat.conf'


def main():
    """Main method of the class"""
    exit_loop = False

    # Configuration read
    config = ConfigParser.RawConfigParser()
    if not file_exists(CONFIGFILENAME):
        sys.exit()

    config.read(CONFIGFILENAME)

    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()

    with open("logging.json", 'r') as log_config_file:
        logging.config.dictConfig(json.load(log_config_file))

    pin_mode = config.get('Pin', 'Mode')
    relay_pin = config.getint('Pin', 'Relay')
    database_name = config.get('Database', 'Filename')
    sensor_id = config.get('Sensors', 'TemperatureSensor')
    db = DatabaseInteraction(database_name)
    relay = RelayControl(relay_pin)

    try:
        # initialize GPIO
        gpio_cleanup()

        set_gpio_mode(pin_mode.lower() == 'bcm')
        set_gpio_pin_mode(logger, relay_pin, False)
        set_gpio_pin_status(relay_pin, 0)

        current_status = False

        while not exit_loop:

            logging.info("Checking schedules")

            activation = ActivationManagement.Check(db, sensor_id)

            if activation != current_status:
                print("Change status")
                relay.set_status(activation)
                current_status = activation

            time.sleep(60)

    except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
        # if start.isAlive():
        #     start.join()
        print('DAEMON - exit')
        logger.debug("Exit with CTRL + C")
    except Exception as exc:
        print('DAEMON - exception %s' % (exc))
        logger.error(exc)
    finally:
        gpio_cleanup()  # cleanup all GPIO


if __name__ == "__main__":
    main()
