from gendiff.formatters.stylish import PAIRS_OF_VALUES
from functools import reduce


MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'
ACTIONS_FOR_SIGNS = {
    '+-': lambda current_dir, value: f"{MESSAGE_START}'{current_dir}'"
    + ' was updated. From '
    + f'{COMPLEX_VALUE if isinstance(value[0], dict) else transform(value[0])}'
    + ' to '
    + f'{COMPLEX_VALUE if isinstance(value[1], dict) else transform(value[1])}'
    + '\n',
    '-': lambda current_dir, _: f"{MESSAGE_START}'{current_dir}'"
    + ' was removed\n',
    '+': lambda current_dir, value: MESSAGE_START
    + f"'{current_dir}' was added with value: "
    + f'{COMPLEX_VALUE if isinstance(value[0], dict) else transform(value[0])}'
    + '\n',
    '=': lambda *_: ''
}


def format(diff):

    def inner(diff, input_dir=[]):
        return reduce(
            lambda x, y: x + y,
            map(
                lambda key_and_value:
                ACTIONS_FOR_SIGNS[key_and_value[1][-1]]
                ('.'.join([*input_dir, key_and_value[0]]), key_and_value[1])
                if isinstance(key_and_value[1], tuple)
                else inner(
                    key_and_value[1],
                    [*input_dir, key_and_value[0]]
                ), diff.items()
            )
        )

    return inner(diff)[:-1]


def transform(value):
    if isinstance(value, str):
        return f"'{value}'"
    value_str = str(value)
    return PAIRS_OF_VALUES[value_str] \
        if PAIRS_OF_VALUES.get(value_str) \
        else value
