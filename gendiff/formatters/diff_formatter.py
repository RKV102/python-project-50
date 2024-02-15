import json
from gendiff.formatters import stylish, plain
from gendiff.formatters.__init__ import INDENT_LEN


def format_diff(formatter, diff):
    match formatter:
        case 'stylish':
            return stylish.format(diff)
        case 'plain':
            return plain.format(diff)
        case 'json':
            return json.dumps(
                diff,
                indent=INDENT_LEN
            )
        case _:
            raise ValueError('Unsupported format')
