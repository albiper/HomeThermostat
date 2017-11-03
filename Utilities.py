"""Utilities module"""
import os
#import RPi.GPIO as GPIO


def get_gpio_pin_status(pin):
    """Gets the status of a GPIO pin"""
    #return GPIO.input(pin)


def set_gpio_pin_status(pin, value):
    """Sets the status of a GPIO pin"""
    #GPIO.output(pin, value)


def file_exists(filename):
    """Checks if specified file exists"""
    return os.path.exists(filename)


def gpio_cleanup():
    """Cleanup GPIO status"""
    #GPIO.cleanup()


def set_gpio_mode(bcm):
    """Sets GPIO mode"""
    #if bcm:
        #GPIO.setmode(GPIO.BCM)
    #else:
        #GPIO.setmode(GPIO.BOARD)


def set_gpio_pin_mode(logger, pin, is_in, is_pull_up=None):
    """Sets GPIO pin mode"""
    pud = ""
    if is_in:
        message = "IN"
        if is_pull_up is not None:
            if is_pull_up:
                pud = "PULL UP"
            else:
                pud = "PULL DOWN"
        else:
            pud = "PULL UP DOWN NOT SPECIFIED"
    else:
        message = "OUT"

    logger.debug("Setting mode for pin %s to %s (%s)" % (pin, message, pud))

    # if is_pull_up is not None:
    #     if is_in:
    #         if is_pull_up:
    #             GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #         else:
    #             GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #     else:
    #         GPIO.setup(pin, GPIO.OUT)
    # else:
    #     if is_in:
    #         GPIO.setup(pin, GPIO.IN)
    #     else:
    #         GPIO.setup(pin, GPIO.OUT)
