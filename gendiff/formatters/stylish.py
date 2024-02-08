INDENT_LEN = 4
INDENT_SYMBOL = ' '


def format(diff, level=1):
    indent = INDENT_SYMBOL * INDENT_LEN * level
    message = []
    for item in diff.items():
        key = item[0]
        value = item[1]['value']
        value_type = str(type(value))[8:-2]
        status = item[1].get('status')
        message_start = f'{indent[:-2]}'
        match value_type:
            case 'dict':
                message_end = create_message_end(key, value,
                                                 indent=indent,
                                                 level=level)
                message.append(create_message(message_start, message_end,
                                              status=status, indent=indent))
            case 'list':
                for i in ((value[0], '-'), (value[1], '+')):
                    if isinstance(i[0], dict):
                        message_end = create_message_end(key, i[0],
                                                         indent=indent,
                                                         level=level)
                    else:
                        message_end = create_message_end(key, i[0])
                    message.append(create_message(message_start, message_end,
                                                  sign=i[1]))
            case _:
                message_end = create_message_end(key, value)
                message.append(create_message(message_start, message_end,
                                              status=status, indent=indent))
    message_str = ''.join(message)
    return '{\n' + message_str + '}' if level == 1 else message_str


def create_message_end(key, value, **kwargs):
    indent = kwargs.get('indent')
    if not indent:
        return f'{key}: {transform(value)}\n'
    level = kwargs['level']
    return f'{key}:' + ' {\n' + format(value, level + 1) + indent + '}\n'


def create_message(message_start, message_end, **kwargs):
    indent = kwargs.get('indent')
    if not indent:
        sign = kwargs['sign']
        return message_start + sign + f' {message_end}'
    status = kwargs['status']
    match status:
        case 'removed':
            return f'{message_start}- {message_end}'
        case 'added':
            return f'{message_start}+ {message_end}'
        case _:
            return indent + message_end


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
