from os import path, makedirs
from yaml import safe_load, safe_dump
from .settings import DEFAULT_CONFIG_DIR


config_dir = DEFAULT_CONFIG_DIR
config_path = path.join(config_dir, 'config.yaml')
creds_path = path.join(config_dir, 'creds.yaml')

if not path.exists(config_dir):
    makedirs(config_dir, exist_ok=True)
    with open(path.join(config_dir, '.gitignore'), 'w+') as fp:
        fp.write('creds.yaml\n')

try:
    config = safe_load(open(config_path, 'r')) or {}
except:
    config = {}
try:
    creds = safe_load(open(creds_path, 'r')) or {}
except:
    creds = {}


def get_config(key):
    return config.get(key)


def set_config(key, value):
    config[key] = value
    safe_dump(config, open(config_path, 'w+'))


def rm_db(key):
    try:
        del config[key]
    except:
        print(f'Config not found for {key}')
    try:
        del creds[key]
    except:
        print(f'Creds not found for {key}')
    safe_dump(config, open(config_path, 'w+'))
    safe_dump(creds, open(creds_path, 'w+'))


def get_creds(key):
    return creds.get(key)


def set_creds(key, value):
    creds[key] = value
    safe_dump(creds, open(creds_path, 'w+'))
