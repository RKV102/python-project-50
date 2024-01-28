from gendiff.formatters.stylish import transform


MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'


def format(diff):

    def inner(diff, input_dir=[]):
        message = ''
        for item in diff.items():
            key = item[0]
            value = item[1]['nested']
            action = item[1].get('action')
            dir = [*input_dir, key]
            transformed_dir = transform('.'.join(dir), True)
            match action:
                case 'removed':
                    message += (MESSAGE_START + transformed_dir
                                + ' was removed\n')
                case 'added':
                    message += (MESSAGE_START + transformed_dir
                                + ' was added with value: '
                                + (COMPLEX_VALUE if isinstance(value, dict)
                                   else transform(value, True))
                                + '\n')
                case 'updated':
                    message += (MESSAGE_START + transformed_dir
                                + ' was updated. From '
                                + ' to '.join(
                                    [COMPLEX_VALUE
                                     if isinstance(sub_value, dict)
                                     else transform(sub_value, True)
                                     for sub_value in value]
                                )
                                + '\n')
                case 'same':
                    pass
                case _:
                    message += inner(value, dir)
        return message

    return inner(diff)[:-1]
