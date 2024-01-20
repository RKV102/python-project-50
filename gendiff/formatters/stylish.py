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
    'True': 'true',
    'False': 'false',
    'None': 'null'
}


def format(diff, level=1):
    indent = INDENT_SYMBOL * INDENT_LEN * level
    formatted_diff = reduce(
        lambda x, y: x + y,
        map(
            lambda key_and_value: ACTIONS_FOR_VALUE_TYPES[
                type(key_and_value[1])
            ](key_and_value[0], key_and_value[1], indent, level)
            if ACTIONS_FOR_VALUE_TYPES.get(type(key_and_value[1]))
            else f'{indent}{key_and_value[0]}: '
                 + f'{transform(key_and_value[1])}\n',
            diff.items()
        )
    )
    return '{\n' + formatted_diff + '}' if level == 1 else formatted_diff


def transform(value):
    value_str = str(value)
    return PAIRS_OF_VALUES[value_str] \
        if PAIRS_OF_VALUES.get(value_str) \
        else value
