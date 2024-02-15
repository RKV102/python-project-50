MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'


def format(diff):
    return format_inner(diff)[:-1]


def format_inner(diff, input_dir=''):
    lines = []
    for key, (value, status) in diff.items():
        dir = '.'.join((input_dir, key)) if input_dir else key
        dir_with_quotes = transform(dir)
        match status:
            case 'removed':
                lines.append(MESSAGE_START + dir_with_quotes
                             + ' was removed\n')
            case 'added':
                lines.append(MESSAGE_START + dir_with_quotes
                             + ' was added with value: '
                             + (COMPLEX_VALUE if isinstance(value, dict)
                                else transform(value))
                             + '\n')
            case 'nested':
                lines.append(format_inner(value, dir))
            case 'updated':
                lines.append(MESSAGE_START + dir_with_quotes
                             + ' was updated. From '
                             + ' to '.join(
                               [COMPLEX_VALUE
                                if isinstance(sub_value, dict)
                                else transform(sub_value)
                                for sub_value in value]
                             )
                             + '\n')
    return ''.join(lines)


def transform(value):
    match str(type(value))[8:-2]:
        case 'bool':
            return str(value).lower()
        case 'NoneType':
            return 'null'
        case 'str':
            return f"'{value}'"
        case _:
            return str(value)
