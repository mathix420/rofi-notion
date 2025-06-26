from concurrent.futures import ThreadPoolExecutor
from .config import get_config, get_creds
from notion_client import AsyncClient
from .transcoders import transcoders
from rofi import Rofi
import webbrowser
import asyncio


executor = ThreadPoolExecutor(max_workers=10)
r = Rofi()


def filter_prop(property_tupple):
    property = property_tupple[1]
    return property.get('type', '') in transcoders


def fmt_choices(title_prop):
    def func(page):
        text = page['properties'][title_prop]['title'][0]['plain_text']
        icon = page.get('icon')
        if icon and icon.get('type') == 'emoji':
            emoji = icon['emoji']
            return (f'{emoji} {text}', page['id'])
        return (text, page['id'])
    return func


async def run(notion, db_id):
    store = dict()

    async def load_relation(name, config):
        db = await notion.databases.query(config['relation']['database_id'])
        pages = db['results']

        if not pages:
            return None

        page_props = pages[0].get('properties', {}).items()
        title_prop = list(filter(lambda x: x[1]['type'] == 'title', page_props))[0][0]
        fmt_fct = fmt_choices(title_prop)
        choices = dict(map(fmt_fct, pages))  # type: ignore
        store[name] = choices

    db = await notion.databases.retrieve(db_id)
    properties = db['properties']  # type: ignore

    mod_props = list(filter(filter_prop, properties.items()))
    mod_props = list(sorted(mod_props, key=lambda x: x[1]['type'] != 'title'))

    co_routines = dict()
    for name, config in mod_props:
        if config.get('type') == 'relation':
            co_routines[name] = asyncio.create_task(
                load_relation(name, config), name=name)

    loop = asyncio.get_running_loop()

    properties = dict()
    for name, config in mod_props:
        prop_type = config.get('type')

        if name in co_routines:
            await co_routines[name]

        result = await loop.run_in_executor(
            executor,
            # Fct to run
            transcoders[prop_type],
            # Args
            r, name, config, store.get(name)
        )
        properties = {**properties, **result}

    if not properties:
        return

    # Create the page
    res = await notion.pages.create(
        parent={'database_id': db_id},
        properties=properties
    )

    webbrowser.open(res['url'])


def main(opts):
    # Get config and creds from config files
    config = get_config(opts.database_name)
    creds = get_creds(opts.database_name)

    if not config:
        raise Exception(f'No config for {opts.database_name}')

    if not creds:
        creds = get_creds('DEFAULT')

    # Start notion client
    notion = AsyncClient(auth=creds)

    # Run command
    asyncio.run(run(notion, config['id']))
