MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'


def format(diff):
    return format_inner(diff)[:-1]


def format_inner(diff, input_dir=()):
    lines = []
    for key, (value, status) in diff.items():
        dir = (*input_dir, key)
        dir_with_quotes = make_quotes('.'.join(dir))
        match status:
            case 'removed':
                lines.append(MESSAGE_START + dir_with_quotes
                             + ' was removed\n')
            case 'added':
                lines.append(MESSAGE_START + dir_with_quotes
                             + ' was added with value: '
                             + (COMPLEX_VALUE if isinstance(value, dict)
                                else make_quotes(value))
                             + '\n')
            case 'nested':
                lines.append(format_inner(value, dir))
            case 'updated':
                lines.append(MESSAGE_START + dir_with_quotes
                             + ' was updated. From '
                             + ' to '.join(
                               [COMPLEX_VALUE
                                if isinstance(sub_value, dict)
                                else make_quotes(sub_value)
                                for sub_value in value]
                             )
                             + '\n')
    return ''.join(lines)


def make_quotes(value):
    transformed_value = transform(value)
    return f"'{transformed_value}'" if isinstance(value, str) \
        else transformed_value


def transform(value):
    match str(type(value))[8:-2]:
        case 'bool':
            return str(value).lower()
        case 'NoneType':
            return 'null'
        case 'str':
            return value
        case _:
            return str(value)
