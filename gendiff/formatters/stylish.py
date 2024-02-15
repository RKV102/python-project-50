INDENT_LEN = 4
INDENT_SYMBOL = ' '


def format(diff):
    return '{\n' + format_inner(diff) + '}'


def format_inner(diff, level=1, was_status=False):
    indent = INDENT_SYMBOL * INDENT_LEN * level
    indent_before_the_sign = f'{indent[:-2]}'
    messages = []
    for key, value_and_status in diff.items():
        (value, status) = (value_and_status[0], value_and_status[1]) \
            if not was_status else (value_and_status, None)
        match status:
            case 'removed':
                messages.append(f'{indent_before_the_sign}- {key}: '
                                + transform(value, level, indent, status))
            case 'added':
                messages.append(f'{indent_before_the_sign}+ {key}: '
                                + transform(value, level, indent, status))
            case 'updated':
                appended = []
                for value_, sign in ((value[0], '-'), (value[1], '+')):
                    appended.append(f'{indent_before_the_sign}{sign} {key}: '
                                    + transform(value_, level, indent, status))
                messages.append(''.join(appended))
            case _:
                messages.append(f'{indent}{key}: '
                                + transform(value, level, indent, status))
    return ''.join(messages)


def transform(value, level, indent, status):
    match str(type(value))[8:-2]:
        case 'bool':
            transformed = str(value).lower()
        case 'NoneType':
            transformed = 'null'
        case 'str':
            transformed = value
        case 'dict':
            was_status = False if status == 'nested' else True
            transformed = ('{\n' + format_inner(value, level + 1, was_status)
                           + indent + '}')
        case _:
            transformed = str(value)
    return transformed + '\n'
