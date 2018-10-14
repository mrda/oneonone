#!/usr/bin/env python
#
# main.py - main entry point for OneOnOne
#

import appdirs
import os
import pathlib
import sys

from onexone import command
from onexone import datastore
from onexone import debugging
from onexone import meeting
from onexone import person
from onexone import utils


debug = False

APP_NAME = 'onexone'
SAVE_FILE = 'onexone-data.json'
USER = os.environ.get('USER')
CONFIG_DIR = appdirs.user_config_dir(APP_NAME, USER)
DATA_FILENAME = os.path.join(CONFIG_DIR, SAVE_FILE)

utils.register_name(APP_NAME)
utils.register_years("2018")


@debugging.trace
def configure_datastore():
    # Initialise the location for stored data
    try:
        pathlib.Path(CONFIG_DIR).mkdir(parents=True)
    except OSError as e:
        # Allow directory already exists to be squashed.
        # Otherwise allow it to bubble up
        if e.errorcode != os.errno.EEXIST:
            raise
    ds = datastore.choose_location(DATA_FILENAME)


def main():

    c = command.CommandOptions(debug=debug)
    c.add_command('help', c.usage, "")
    c.add_command('version', utils.display_program_header, "")
    p = person.Person()
    c.add_command('person', p.parse, "<subcommand>")
    m = meeting.Meeting()
    c.add_command('meeting', m.parse, "<subcommand>")

    configure_datastore()

    if len(sys.argv) == 1:
        c.usage()
        sys.exit(0)

    c.jump(sys.argv[1:])


if __name__ == '__main__':
    main()
