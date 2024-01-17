from functools import reduce


INDENT_LEN = 4
INDENT_SYMBOL = ' '


def format(diff):

    def inner(diff, level=1):
        formatted_diff = ''
        indent = INDENT_SYMBOL * INDENT_LEN * level
        for key_and_value in diff.items():
            key = key_and_value[0]
            value = key_and_value[1]
            if isinstance(value, tuple):
                action = value[-1]
                formatted_diff += f'{indent}{key}: {transform(value[0])}\n'\
                    if action == '='\
                    else reduce(lambda x, y: x + y,
                                map(lambda i: f'{indent[:-2]}'
                                    + f'{action[-i-1]} {key}: '
                                    + '{\n' + inner(value[i], level + 1)
                                    + indent + '}\n'
                                    if isinstance(value[i], dict)
                                    else f'{indent[:-2]}'
                                    + f'{action[-i-1]} {key}: '
                                    + f'{transform(value[i])}\n',
                                    range(len(action))))
            elif isinstance(value, dict):
                formatted_diff += f'{indent}{key}:' + ' {\n'\
                    + inner(value, level + 1) + indent + '}\n'
            else:
                formatted_diff += f'{indent}{key}: {transform(value)}\n'
        return formatted_diff

    return '{\n' + inner(diff) + '}'


def transform(value):
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return value
