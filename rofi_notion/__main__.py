from .settings import DEFAULT_CONFIG_DIR
from argparse import ArgumentParser
from . import main as main_handler
from . import manage

parser = ArgumentParser('rofi-notion')

parser.add_argument('--config-dir', metavar='PATH', type=str, help="Config directory", default=DEFAULT_CONFIG_DIR)

# SUBPARSER CONFIG
subparser = parser.add_subparsers(dest='command', title='commands', required=True)

# SET CREDS
set_creds = subparser.add_parser('set-creds', help='set notion bot api secret')
set_creds.set_defaults(handler=manage.set_default_creds)

# LINK
link_db = subparser.add_parser('link', help='link a new database')
link_db.set_defaults(handler=manage.link_db)

# UNLINK
unlink_db = subparser.add_parser('unlink', help='unlink a database')
unlink_db.add_argument('database_name', metavar='DB_NAME', type=str, nargs='?', help='database name')
unlink_db.set_defaults(handler=manage.unlink_db)

# LIST
list_db = subparser.add_parser('list', help='list linked databases')
list_db.set_defaults(handler=manage.list_db)

# RUN
run = subparser.add_parser('run', help='start new row creation flow')
run.add_argument('database_name', metavar='DB_NAME', type=str, help='database name')
run.add_argument('-s', '--skip-browser', action='store_true', help='skip opening the browser after creating entry')
run.add_argument('-q', '--quick-add', action='store_true', help='only fill the first field (fast inbox mode)')
run.set_defaults(handler=main_handler.main)


def main():
    options = parser.parse_args()

    if options.handler:
        options.handler(options)
