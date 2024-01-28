INDENT_LEN = 4
INDENT_SYMBOL = ' '
PAIRS_OF_VALUES = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def format(diff):

    def inner(diff, level=1):
        indent = INDENT_SYMBOL * INDENT_LEN * level
        message = ''
        for item in diff.items():
            key = item[0]
            value = item[1]['nested']
            value_type = str(type(value))[8:-2]
            action = item[1].get('action')
            message_start = f'{indent[:-2]}'
            match value_type:
                case 'dict':
                    message_end = create_message_end(key, value, indent, level,
                                                     inner)
                    message += create_message(message_start, message_end,
                                              action, indent)
                case 'list':
                    for i in ((value[0], '-'), (value[1], '+')):
                        if isinstance(i[0], dict):
                            message_end = create_message_end(key, i[0], indent,
                                                             level, inner)
                        else:
                            message_end = create_message_end(key, i[0])
                        message += create_message(message_start, message_end,
                                                  sign=i[1])
                case _:
                    message_end = create_message_end(key, value)
                    message += create_message(message_start, message_end,
                                              action, indent)
        return message

    return '{\n' + inner(diff) + '}'


def create_message_end(key, value, indent=None, level=None, inner=None):
    if not indent:
        return f'{key}: {transform(value)}\n'
    return f'{key}:' + ' {\n' + inner(value, level + 1) + indent + '}\n'


def create_message(message_start, message_end, action=None, indent=None,
                   sign=None):
    if not indent:
        return f'{message_start}{sign} {message_end}'
    match action:
        case 'removed':
            return f'{message_start}- {message_end}'
        case 'added':
            return f'{message_start}+ {message_end}'
        case _:
            return f'{indent}{message_end}'


def transform(value, plain_mode=False):
    if plain_mode and isinstance(value, str):
        return f"'{value}'"
    value_str = str(value)
    if PAIRS_OF_VALUES.get(value_str):
        return PAIRS_OF_VALUES[value_str]
    return str(value)
