from tinytuya import BulbDevice
from sys import argv
from enum import Enum
from typing import List
from typing import Dict
from dotenv import dotenv_values
from pathlib import Path


DEFAULT_API_VERSION = 3.3


class Turn(Enum):
    OFF = 1
    ON = 2


def _exit_because(reason: str, code: int = 0) -> None:
    print(reason)
    exit(code)


def is_command_valid(args):
    return len(args) > 1 and args[1] in ('ON', 'OFF')


def get_switch_value(args) -> Turn:
    if is_command_valid(args):
        switch_value = args[1]
        if switch_value == 'ON':
            return Turn.ON
        if switch_value == 'OFF':
            return Turn.OFF
    _exit_because('Missing action or action is invalid\nUsage: ngs-switch ON|OFF')


def configure(lights: List[BulbDevice], config: Dict = None) -> None:
    api_version = DEFAULT_API_VERSION
    if config and config.get('API_VERSION'):
        api_version = config.get('API_VERSION')
    for light in lights:
        light.set_version(api_version)


def turn_on(lights: List[BulbDevice]) -> None:
    for light in lights:
        light.turn_on()
        light.set_brightness_percentage(20)


def turn_off(lights: List[BulbDevice]) -> None:
    for light in lights:
        light.turn_off()


def load_configuration(file: str = '.env') -> Dict:
    config = dotenv_values(file)
    all_variables_are_present = (
            config.get('L_DEVICE_ID') and config.get('L_IP_ADDR') and config.get('L_LOCAL_KEY') and
            config.get('R_DEVICE_ID') and config.get('R_IP_ADDR') and config.get('R_LOCAL_KEY')
    )
    if all_variables_are_present:
        return config
    else:
        _exit_because('Missing configuration ! Check the .env file')


def main():
    action = get_switch_value(argv)
    config_path = Path(__file__).parent.resolve() / '.env'
    config = load_configuration(str(config_path))
    light_left_side = BulbDevice(config['L_DEVICE_ID'], config['L_IP_ADDR'], config['L_LOCAL_KEY'])
    light_right_side = BulbDevice(config['R_DEVICE_ID'], config['R_IP_ADDR'], config['R_LOCAL_KEY'])

    lights = [light_left_side, light_right_side]
    configure(lights, config)

    if action is Turn.ON:
        turn_on(lights)
    if action is Turn.OFF:
        turn_off(lights)


if __name__ == '__main__':
    main()
