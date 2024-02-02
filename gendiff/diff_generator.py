from gendiff.file_parser_via_formatter import parse_file
from gendiff.formatters.diff_formatter import format_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    parsed_file1 = parse_file(file_path1)
    parsed_file2 = parse_file(file_path2)
    diff = diff_parsed(parsed_file1, parsed_file2)
    return format_diff(formatter, diff)


def diff_parsed(parsed1, parsed2={}, was_action=False):
    if not isinstance(parsed1, dict) and not parsed2:
        return parsed1
    view = {}
    keys1 = set(parsed1.keys())
    keys2 = set(parsed2.keys())
    removed_keys = keys1.difference(keys2)
    added_keys = keys2.difference(keys1)
    united_keys = list(keys1.union(keys2))
    united_keys.sort()
    for key in united_keys:
        if key in removed_keys:
            add_to_view(view, key, parsed1, 'removed', was_action)
        elif key in added_keys:
            add_to_view(view, key, parsed2, 'added', was_action)
        elif parsed1[key] == parsed2[key]:
            add_to_view(view, key, parsed1, 'same', was_action)
        elif isinstance(parsed1[key], dict) and isinstance(parsed2[key], dict):
            view[key] = {'nested': diff_parsed(parsed1[key], parsed2[key])}
        else:
            view[key] = {'nested': [diff_parsed(parsed1[key], was_action=True),
                                    diff_parsed(parsed2[key], was_action=True)],
                         'action': 'updated'}
    return view


def add_to_view(view, key, source, action, was_action):
    view[key] = {'nested': diff_parsed(source[key], was_action=True),
                 'action': action} \
        if not was_action \
        else {'nested': diff_parsed(source[key], was_action=True)}
