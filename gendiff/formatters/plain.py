from gendiff.formatters.stylish import transform


MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'


def format(diff):
    return format_inner(diff)[:-1]


def format_inner(diff, input_dir=[]):
    message = []
    for item in diff.items():
        key = item[0]
        value = item[1]['value']
        status = item[1].get('status')
        dir = [*input_dir, key]
        transformed_dir = transform('.'.join(dir), True)
        match status:
            case 'removed':
                message.append(MESSAGE_START + transformed_dir
                               + ' was removed\n')
            case 'added':
                message.append(MESSAGE_START + transformed_dir
                               + ' was added with value: '
                               + (COMPLEX_VALUE if isinstance(value, dict)
                                  else transform(value, True))
                               + '\n')
            case 'updated':
                message.append(MESSAGE_START + transformed_dir
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
                message.append(format_inner(value, dir))
    return ''.join(message)
