import json
import gendiff.formatters as formatters


def format_diff(formatter, diff):
    match formatter:
        case 'stylish':
            return formatters.stylish.format(diff)
        case 'plain':
            return formatters.plain.format(diff)
        case 'json':
            return json.dumps(
                diff,
                indent=formatters.stylish.INDENT_LEN
            )
        case _:
            raise ValueError('Unsupported format')
