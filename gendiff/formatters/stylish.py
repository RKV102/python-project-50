INDENT_LEN = 4
INDENT_SYMBOL = ' '
PAIRS_OF_VALUES = {
    'True': 'true',
    'False': 'false',
    'None': 'null'
}
ACTIONS_FOR_DICTS = {
    'removed': lambda indent, key, value, level, inner: f'{indent[:-2]}- {key}:'
    + ' {\n' + inner(value, level + 1) + indent + '}\n',
    'added': lambda indent, key, value, level, inner: f'{indent[:-2]}+ {key}:'
    + ' {\n' + inner(value, level + 1) + indent + '}\n'
}
ACTIONS_FOR_PRIMITIVES = {
    'removed': lambda indent, key, value: f'{indent[:-2]}- {key}: '
    + f'{transform(value)}\n',
    'added': lambda indent, key, value: f'{indent[:-2]}+ {key}: '
    + f'{transform(value)}\n'
}
ACTIONS_FOR_NON_PRIMITIVES = {
    dict: lambda indent, key, value, level, inner, action:
    ACTIONS_FOR_DICTS[action](indent, key, value, level + 1, inner)
    if ACTIONS_FOR_DICTS.get(action)
    else f'{indent}{key}:' + ' {\n' + inner(value, level + 1)
         + indent + '}\n',
    list: lambda indent, key, value, level, inner, _:
    (f'{indent[:-2]}- {key}: ' + '{\n' + inner(value[0], level + 1) + indent
     + '}\n'
     if isinstance(value[0], dict)
     else f'{indent[:-2]}- {key}: ' + f'{transform(value[0])}\n')
    + (f'{indent[:-2]}+ {key}: ' + '{\n' + inner(value[1], level + 1) + indent
       + '}\n'
       if isinstance(value[1], dict)
       else f'{indent[:-2]}+ {key}: ' + f'{transform(value[1])}\n')
}


def format(diff):

    def inner(diff, level=1):
        indent = INDENT_SYMBOL * INDENT_LEN * level
        message = ''
        for item in diff.items():
            key = item[0]
            value = item[1]['nested']
            value_type = type(value)
            action = item[1].get('action')
            if ACTIONS_FOR_NON_PRIMITIVES.get(value_type):
                message += ACTIONS_FOR_NON_PRIMITIVES[value_type](
                    indent, key, value, level, inner, action
                )
            elif ACTIONS_FOR_PRIMITIVES.get(action):
                message += ACTIONS_FOR_PRIMITIVES[action](indent, key, value)
            else:
                message += f'{indent}{key}: {transform(value)}\n'
        return message

    return '{\n' + inner(diff) + '}'


def transform(value, plain_mode=False):
    if plain_mode and isinstance(value, str):
        return f"'{value}'"
    value_str = str(value)
    return PAIRS_OF_VALUES[value_str] \
        if PAIRS_OF_VALUES.get(value_str) \
        else value
