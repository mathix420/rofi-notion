from datetime import datetime
from functools import partial
from typing import Any
from rofi import Rofi
from sys import exit


def required(transcoder: (...), *args):
    result = transcoder(*args)
    if not result:
        exit('This field is required.')
    return result


def text(r: Rofi, name: str, config: dict, store: Any) -> dict:
    res = r.text_entry(name)
    if res == None:
        return {}
    return {
        name: {
            config.get('type'): [
                {
                    "type": "text",
                    "text": {"content": res}
                },
            ]
        }
    }


def number(r: Rofi, name: str, config: dict, store: Any) -> dict:
    res = r.decimal_entry(name)
    if res == None:
        return {}
    return {
        name: {'number': res}
    }


def select(r: Rofi, name: str, config: dict, store: Any) -> dict:
    prop_type = config.get('type')
    choices = list(map(lambda x: x['name'], config[prop_type]['options']))

    index, _key = r.select(name, choices)
    if index == -1:
        return {}

    return {
        name: {
            prop_type: {'name': choices[index]}
        }
    }


def multi_select(r: Rofi, name: str, config: dict, store: Any) -> dict:
    choices = list(map(lambda x: x['name'], config['multi_select']['options']))

    all_res = []
    index = 0
    while index != -1:
        index, _key = r.select(name, choices)
        if index != -1:
            all_res.append({'name': choices[index]})
            choices.remove(choices[index])

    if not all_res:
        return {}

    return {
        name: {
            'multi_select': all_res
        }
    }


def date(r: Rofi, name: str, config: dict, store: Any) -> dict:
    res = r.date_entry(name)
    if not res:
        return {}
    if type(res) != str:
        res = str(res)
    date = datetime.strptime(res, '%Y-%m-%d')  # type: ignore
    return {
        name: {
            'date': {
                'start': date.isoformat()
            }
        }
    }


def people(r: Rofi, name: str, config: dict, store: Any) -> dict:
    return {}


def checkbox(r: Rofi, name: str, config: dict, store: Any) -> dict:
    index, key = r.select(name, ['Yes', 'No'], )
    return {
        name: {
            'checkbox': index == 0
        }
    }


def url(r: Rofi, name: str, config: dict, store: Any) -> dict:
    res = r.text_entry(name)
    if res == None:
        return {}
    return {
        name: {
            'url': res
        }
    }


def email(r: Rofi, name: str, config: dict, store: Any) -> dict:
    res = r.text_entry(name)
    if res == None:
        return {}
    return {
        name: {
            'email': res
        }
    }


def phone_number(r: Rofi, name: str, config: dict, store: Any) -> dict:
    res = r.text_entry(name)
    if res == None:
        return {}
    return {
        name: {
            'phone_number': res
        }
    }


def relation(r: Rofi, name: str, config: dict, choices: dict) -> dict:
    config = config['relation']
    relations = []

    if not choices:
        return {}

    index = 0
    while index != -1:
        index, _key = r.select(name, choices)
        if index != -1:
            key = list(choices.keys())[index]
            relations.append({'id': choices[key]})
            del choices[key]

    if not relations:
        return {}

    return {
        name: {
            'relation': relations
        }
    }


transcoders = {
    'title': partial(required, text),
    'relation': relation,
    'rich_text': text,
    'number': number,
    'select': select,
    'status': select,
    'multi_select': multi_select,
    'date': date,
    'people': people,
    'checkbox': checkbox,
    'url': url,
    'email': email,
    'phone_number': phone_number,
}
