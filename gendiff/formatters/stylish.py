INDENT_LEN = 4
INDENT_SYMBOL = ' '


def format(diff):
    return '{\n' + format_inner(diff) + '}'


def format_inner(diff, level=1):
    indent = INDENT_SYMBOL * INDENT_LEN * level
    message = []
    for item in diff.items():
        key = item[0]
        value = item[1]['value']
        status = item[1].get('status')
        indent_before_the_sign = f'{indent[:-2]}'
        match status:
            case 'removed':
                appended = (f'{indent_before_the_sign}- {key}: '
                            + ('{\n' + format_inner(value, level + 1) + indent
                               + '}' if isinstance(value, dict)
                               else transform(value)) + '\n')
            case 'added':
                appended = (f'{indent_before_the_sign}+ {key}: '
                            + ('{\n' + format_inner(value, level + 1) + indent
                               + '}' if isinstance(value, dict)
                               else transform(value)) + '\n')
            case 'updated':
                appended = []
                for value, sign in ((value[0], '-'), (value[1], '+')):
                    appended.append(f'{indent_before_the_sign}{sign} {key}: '
                                    + ('{\n' + format_inner(value, level + 1)
                                       + indent + '}' if isinstance(value, dict)
                                       else transform(value)) + '\n')
                appended = ''.join(appended)
            case _:
                appended = (f'{indent}{key}: '
                            + ('{\n' + format_inner(value, level + 1) + indent
                               + '}' if isinstance(value, dict)
                               else transform(value)) + '\n')
        message.append(appended)
    return ''.join(message)


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
