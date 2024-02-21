LINE_START = 'Property '


def format(diff, input_dir=''):
    lines = []
    for key, (value, status) in diff.items():
        dir = '.'.join((input_dir, key)) if input_dir else key
        dir_with_quotes = f"'{dir}'"
        match status:
            case 'removed':
                line = LINE_START + dir_with_quotes + ' was removed'
            case 'added':
                line = (LINE_START + dir_with_quotes + ' was added with value: '
                        + to_str(value))
            case 'updated':
                line = (LINE_START + dir_with_quotes + ' was updated. From '
                        + ' to '.join(
                            [to_str(sub_value) for sub_value in value]
                        ))
            case 'nested':
                line = format(value, dir)
            case 'same':
                line = None
        lines.append(line) if line else None
    return '\n'.join(lines)


def to_str(inner):
    if isinstance(inner, bool):
        return str(inner).lower()
    elif inner is None:
        return 'null'
    elif isinstance(inner, str):
        return f"'{inner}'"
    elif isinstance(inner, dict):
        return '[complex value]'
    else:
        return str(inner)
