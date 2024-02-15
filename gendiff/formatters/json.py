import json
from gendiff.formatters.__init__ import INDENT_LEN


def format(diff):
    return json.dumps(diff, indent=INDENT_LEN)
