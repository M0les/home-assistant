"""
Support for controlling GPIO pins of a Orange Pi.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/opi_gpio/
"""
# pylint: disable=import-error
import logging

from homeassistant.const import (
    EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP)

REQUIREMENTS = [
    ('https://github.com/duxingkei33/orangepi_PC_gpio_pyH3/archive/'
     '8d2095e3cef1b8f8435956a2e4ed17be9fb4c29c.zip')
    ]
DOMAIN = "opi_gpio"
_LOGGER = logging.getLogger(__name__)


# pylint: disable=no-member
def setup(hass, config):
    """Setup the Orange PI GPIO component."""
    from pyA20.gpio import gpio

    hass.bus.listen_once(EVENT_HOMEASSISTANT_START, prepare_gpio)
    gpio.init()
    return True


def setup_output(port):
    """Setup a GPIO as output."""
    from pyA20.gpio import gpio
    gpio.setcfg(port, gpio.OUTPUT)


def setup_input(port, pull_mode):
    """Setup a GPIO as input."""
    from pyA20.gpio import gpio
    gpio.setcfg(port, gpio.INPUT)
    gpio.pullup(port, gpio.PULLDOWN if pull_mode == 'DOWN' else gpio.PULLUP)


def write_output(port, value):
    """Write a value to a GPIO."""
    from pyA20.gpio import gpio
    gpio.output(port, value)


def read_input(port):
    """Read a value from a GPIO."""
    from pyA20.gpio import gpio
    return gpio.input(port)
