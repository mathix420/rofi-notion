from prompt_toolkit.validation import Validator, ValidationError
from .config import rm_db, set_config, config, set_creds
from InquirerPy.resolver import prompt
from prompt_toolkit import document
import re


NO_SPACES = re.compile(r'^[\w-]+$')
DB_ID = re.compile(r'^[a-f0-9]{32}$', re.IGNORECASE)
API_KEY_REGEX = re.compile(r'^secret_\w{43}$')


class NameValidator(Validator):
    def __init__(self, *args, **kwargs) -> None:
        pass

    def validate(self, document: document.Document) -> None:
        if 'DEFAULT' == document.text:
            raise ValidationError(message = 'Cannot be `DEFAULT`', cursor_position = len(document.text))
        if not NO_SPACES.match(document.text):
            raise ValidationError(message = 'Must match ^[\\w-]+$', cursor_position = len(document.text))


class DbIdValidator(Validator):
    def __init__(self, *args, **kwargs) -> None:
        pass

    def validate(self, document: document.Document) -> None:
        if not DB_ID.match(document.text):
            raise ValidationError(message = 'Must match ^[a-f0-9]{32}$', cursor_position = len(document.text))


class ApiKeyValidator(Validator):
    def __init__(self, *args, **kwargs) -> None:
        pass

    def validate(self, document: document.Document) -> None:
        if not API_KEY_REGEX.match(document.text):
            raise ValidationError(message = 'Must match ^secret_\\w{43}$', cursor_position = len(document.text))


def link_db(opts):
    res = prompt([
        {
            'type': 'input',
            'name': 'name',
            'message': 'Database name',
            'validate': NameValidator,
        },
        {
            'type': 'input',
            'name': 'id',
            'message': 'Database id',
            'validate': DbIdValidator,
        },
        {
            'type': 'confirm',
            'name': 'custom-secret',
            'message': 'Do you want to setup a custom API key for this database'
        }
    ])

    key = res['name']

    if res['custom-secret']:
        new_res = prompt([{
            'type': 'input',
            'name': 'api_key',
            'message': 'Api secret',
            'validate': ApiKeyValidator,
        }])
        set_creds(key, new_res['api_key'])

    set_config(key, {
        'id': res['id'],
    })

    print(f'DB {key} linked!')


def unlink_db(opts):
    key = opts.database_name
    if not key:
        res = prompt([{
            'type': 'input',
            'name': 'name',
            'message': 'Database name',
            'validate': NameValidator,
        }])
        key = res['name']
    rm_db(key)

    print(f'DB {key} un-linked!')


def list_db(opts):
    if not config.keys():
        print('No db linked.')

    for name in config.keys():
        print(f'• {name}')


def set_default_creds(opts):
    res = prompt([{
        'type': 'input',
        'name': 'api_key',
        'message': 'Api secret',
        'validate': ApiKeyValidator,
    }])
    set_creds('DEFAULT', res['api_key'])

    print('Done!')
