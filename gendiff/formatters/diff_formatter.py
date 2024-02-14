import json
from gendiff.formatters import stylish, plain


def format_diff(formatter, diff):
    match formatter:
        case 'stylish':
            return stylish.format(diff)
        case 'plain':
            return plain.format(diff)
        case 'json':
            return json.dumps(
                diff,
                indent=stylish.INDENT_LEN
            )
        case _:
            raise ValueError('Unsupported format')
