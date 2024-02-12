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
                                + ('{\n' + format_inner(value, level + 1, True)
                                   + indent + '}' if isinstance(value, dict)
                                   else transform(value)) + '\n')
            case 'added':
                messages.append(f'{indent_before_the_sign}+ {key}: '
                                + ('{\n' + format_inner(value, level + 1, True)
                                   + indent + '}' if isinstance(value, dict)
                                   else transform(value)) + '\n')
            case 'updated':
                appended = []
                for value_, sign in ((value[0], '-'), (value[1], '+')):
                    appended.append(f'{indent_before_the_sign}{sign} {key}: '
                                    + ('{\n' + format_inner(value_, level + 1,
                                                            True)
                                       + indent + '}'
                                       if isinstance(value_, dict)
                                       else transform(value_)) + '\n')
                messages.append(''.join(appended))
            case 'nested':
                messages.append(f'{indent}{key}: ' + '{\n'
                                + format_inner(value, level + 1) + indent + '}'
                                + '\n')
            case _:
                messages.append(f'{indent}{key}: '
                                + ('{\n' + format_inner(value, level + 1, True)
                                   + indent + '}' if isinstance(value, dict)
                                   else transform(value)) + '\n')
    return ''.join(messages)


def transform(value, plain_mode=False):
    if plain_mode and isinstance(value, str):
        return f"'{value}'"
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return str(value)
