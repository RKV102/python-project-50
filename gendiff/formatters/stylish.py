from gendiff.formatters import INDENT_LEN, INDENT_SYMBOL


def format(diff, level=1):
    indent_part = INDENT_SYMBOL * INDENT_LEN
    indent_before_the_brace = indent_part * (level - 1)
    indent = indent_part * level
    indent_before_the_sign = f'{indent[:-2]}'
    lines = ['{']
    for key, (value, status) in diff.items():
        match status:
            case 'removed':
                appended = (f'{indent_before_the_sign}- {key}: '
                            + to_str(value, level + 1))
            case 'added':
                appended = (f'{indent_before_the_sign}+ {key}: '
                            + to_str(value, level + 1))
            case 'updated':
                appended = '\n'.join([f'{indent_before_the_sign}{sign} {key}: '
                                      + to_str(sub_value, level + 1)
                                      for sub_value, sign
                                      in ((value[0], '-'), (value[1], '+'))])
            case 'nested':
                appended = f'{indent}{key}: ' + format(value, level + 1)
            case 'same':
                appended = f'{indent}{key}: ' + to_str(value, level + 1)
        lines.append(appended)
    lines.append(indent_before_the_brace + '}')
    return '\n'.join(lines)


def to_str(inner, level):
    if isinstance(inner, bool):
        return str(inner).lower()
    elif inner is None:
        return 'null'
    elif isinstance(inner, str):
        return inner
    elif isinstance(inner, dict):
        indent_part = INDENT_SYMBOL * INDENT_LEN
        indent_before_the_brace = indent_part * (level - 1)
        indent = indent_part * level
        lines = ['{']
        for key, value in inner.items():
            appended = f'{indent}{key}: ' + to_str(value, level + 1)
            lines.append(appended)
        lines.append(indent_before_the_brace + '}')
        return '\n'.join(lines)
    else:
        return str(inner)
