from gendiff.formatters import stylish, plain, json


def format_diff(formatter, diff):
    match formatter:
        case 'stylish':
            return stylish.format(diff)
        case 'plain':
            return plain.format(diff)
        case 'json':
            return json.format(diff)
        case _:
            raise ValueError('Unsupported format')
