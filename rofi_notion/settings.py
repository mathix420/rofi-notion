from os.path import join
from os import getenv

HOME = getenv('HOME', '.config')
DEFAULT_CONFIG_DIR = join(HOME, '.config', 'rofi-notion')
