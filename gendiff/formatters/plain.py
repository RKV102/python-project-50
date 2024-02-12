from gendiff.formatters.stylish import transform


MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'


def format(diff):
    return format_inner(diff)[:-1]


def format_inner(diff, input_dir=()):
    messages = []
    for key, (value, status) in diff.items():
        dir = (*input_dir, key)
        transformed_dir = transform('.'.join(dir), True)
        match status:
            case 'removed':
                messages.append(MESSAGE_START + transformed_dir
                                + ' was removed\n')
            case 'added':
                messages.append(MESSAGE_START + transformed_dir
                                + ' was added with value: '
                                + (COMPLEX_VALUE if isinstance(value, dict)
                                   else transform(value, True))
                                + '\n')
            case 'nested':
                messages.append(format_inner(value, dir))
            case 'updated':
                messages.append(MESSAGE_START + transformed_dir
                                + ' was updated. From '
                                + ' to '.join(
                                  [COMPLEX_VALUE
                                   if isinstance(sub_value, dict)
                                   else transform(sub_value, True)
                                   for sub_value in value]
                                )
                                + '\n')
    return ''.join(messages)
