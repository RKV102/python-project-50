from gendiff.formatters.__init__ import INDENT_LEN, INDENT_SYMBOL


def format(diff):
    return '{\n' + format_inner(diff) + '}'


def format_inner(diff, level=1, was_status=False):
    indent = INDENT_SYMBOL * INDENT_LEN * level
    indent_before_the_sign = f'{indent[:-2]}'
    lines = []
    for key, value_and_status in diff.items():
        (value, status) = (value_and_status[0], value_and_status[1]) \
            if not was_status else (value_and_status, None)
        match status:
            case 'removed':
                lines.append(f'{indent_before_the_sign}- {key}: '
                             + construct(value, level, indent, True))
            case 'added':
                lines.append(f'{indent_before_the_sign}+ {key}: '
                             + construct(value, level, indent, True))
            case 'updated':
                appended = []
                for value_, sign in ((value[0], '-'), (value[1], '+')):
                    appended.append(f'{indent_before_the_sign}{sign} {key}: '
                                    + construct(value_, level, indent, True))
                lines.append(''.join(appended))
            case 'nested':
                lines.append(f'{indent}{key}: '
                             + construct(value, level, indent, False))
            case _:
                lines.append(f'{indent}{key}: '
                             + construct(value, level, indent, True))
    return ''.join(lines)


def construct(value, level, indent, was_status=None):
    match str(type(value))[8:-2]:
        case 'bool':
            constructed = str(value).lower()
        case 'NoneType':
            constructed = 'null'
        case 'str':
            constructed = value
        case 'dict':
            constructed = ('{\n' + format_inner(value, level + 1, was_status)
                           + indent + '}')
        case _:
            constructed = str(value)
    return constructed + '\n'
