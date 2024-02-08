INDENT_LEN = 4
INDENT_SYMBOL = ' '
PAIRS_OF_VALUES = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def format(diff, level=1):
    indent = INDENT_SYMBOL * INDENT_LEN * level
    message = []
    for item in diff.items():
        key = item[0]
        value = item[1]['nested']
        value_type = str(type(value))[8:-2]
        action = item[1].get('action')
        message_start = f'{indent[:-2]}'
        match value_type:
            case 'dict':
                message_end = create_message_end(key, value,
                                                 indent=indent,
                                                 level=level,
                                                 format=format)
                message.append(create_message(message_start, message_end,
                                              action=action, indent=indent))
            case 'list':
                for i in ((value[0], '-'), (value[1], '+')):
                    if isinstance(i[0], dict):
                        message_end = create_message_end(key, i[0],
                                                         indent=indent,
                                                         level=level,
                                                         format=format)
                    else:
                        message_end = create_message_end(key, i[0])
                    message.append(create_message(message_start, message_end,
                                                  sign=i[1]))
            case _:
                message_end = create_message_end(key, value)
                message.append(create_message(message_start, message_end,
                                              action=action, indent=indent))
    message_str = ''.join(message)
    return '{\n' + message_str + '}' if level == 1 else message_str


def create_message_end(key, value, **kwargs):
    if not kwargs.get('indent'):
        return f'{key}: {transform(value)}\n'
    return (f'{key}:' + ' {\n' + kwargs['format'](value, kwargs['level'] + 1)
            + kwargs['indent'] + '}\n')


def create_message(message_start, message_end, **kwargs):
    if not kwargs.get('indent'):
        return message_start + kwargs['sign'] + f' {message_end}'
    match kwargs['action']:
        case 'removed':
            return f'{message_start}- {message_end}'
        case 'added':
            return f'{message_start}+ {message_end}'
        case _:
            return kwargs['indent'] + message_end


def transform(value, plain_mode=False):
    if plain_mode and isinstance(value, str):
        return f"'{value}'"
    value_str = str(value)
    if PAIRS_OF_VALUES.get(value_str):
        return PAIRS_OF_VALUES[value_str]
    return str(value)
