from functools import reduce


INDENT_LEN = 4
INDENT_SYMBOL = ' '
ACTIONS_FOR_VALUE_TYPES = {
    tuple: lambda key, value, indent, level: f'{indent}{key}: '
    + f'{transform(value[0])}\n' if value[-1] == '='
    else reduce(lambda x, y: x + y, map(lambda i: f'{indent[:-2]}'
                                        + f'{value[-1][-i-1]} {key}: '
                                        + '{\n' + format(value[i],
                                                         level + 1)
                                        + indent + '}\n'
                                        if isinstance(value[i], dict)
                                        else f'{indent[:-2]}'
                                        + f'{value[-1][-i - 1]} {key}: '
                                        + f'{transform(value[i])}\n',
                                        range(len(value[-1])))),
    dict: lambda key, value, indent, level: f'{indent}{key}:'
    + ' {\n' + format(value, level + 1) + indent + '}\n'
}
PAIRS_OF_VALUES = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def format(diff, level=1):
    formatted_diff = ''
    indent = INDENT_SYMBOL * INDENT_LEN * level
    for key_and_value in diff.items():
        key = key_and_value[0]
        value = key_and_value[1]
        value_type = type(value)
        formatted_diff += ACTIONS_FOR_VALUE_TYPES[value_type](key, value,
                                                              indent, level) \
            if ACTIONS_FOR_VALUE_TYPES.get(value_type) \
            else f'{indent}{key}: {transform(value)}\n'
    return '{\n' + formatted_diff + '}' if level == 1 else formatted_diff


def transform(value):
    return PAIRS_OF_VALUES[value] if PAIRS_OF_VALUES.get(value) else value
