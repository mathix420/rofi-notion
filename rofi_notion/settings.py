from os.path import join
from os import getenv

HOME = getenv('HOME', '~')
_CONFIG_DIR = getenv('XDG_CONFIG_HOME', join(HOME, '.config'))
DEFAULT_CONFIG_DIR = join(_CONFIG_DIR, 'rofi-notion')