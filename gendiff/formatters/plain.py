from gendiff.formatters.stylish import transform


MESSAGE_START = 'Property '
COMPLEX_VALUE = '[complex value]'
ACTIONS = {
    'added': lambda dir, value: MESSAGE_START + dir + ' was added with value: '
    + (COMPLEX_VALUE if isinstance(value, dict) else transform(
        value, True
    )) + '\n',
    'removed': lambda dir, _: MESSAGE_START + dir + ' was removed\n',
    'updated': lambda dir, values: MESSAGE_START + dir + ' was updated. From '
    + (COMPLEX_VALUE if isinstance(values[0], dict) else transform(
        values[0], True
    ))
    + ' to '
    + (COMPLEX_VALUE if isinstance(values[1], dict) else transform(
        values[1], True
    ))
    + '\n',
    'same': lambda *_: ''
}


def format(diff):

    def inner(diff, input_dir=[]):
        message = ''
        for item in diff.items():
            key = item[0]
            value = item[1]['nested']
            action = item[1].get('action')
            dir = [*input_dir, key]
            message += ACTIONS[action](transform('.'.join(dir), True), value) \
                if action \
                else inner(value, dir)
        return message

    return inner(diff)[:-1]
