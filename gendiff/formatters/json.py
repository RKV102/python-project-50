import json
from gendiff.formatters import INDENT_LEN


def format(diff):
    return json.dumps(diff, indent=INDENT_LEN)
