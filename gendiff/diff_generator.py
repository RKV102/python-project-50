from gendiff.file_parser_via_formatter import parse_file
from gendiff.formatters.diff_formatter import format_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    parsed_file1 = parse_file(file_path1)
    parsed_file2 = parse_file(file_path2)
    diff = diff_parsed(parsed_file1, parsed_file2)
    return format_diff(formatter, diff)


def diff_parsed(parsed1, parsed2={}, was_action=False):
    if not isinstance(parsed1, dict):
        return parsed1
    view = {}
    keys1 = set(parsed1.keys())
    keys2 = set(parsed2.keys())
    removed_keys = keys1.difference(keys2)
    added_keys = keys2.difference(keys1)
    united_keys = list(keys1.union(keys2))
    united_keys.sort()
    for key in united_keys:
        if key_in_added_or_removed_keys(key, removed_keys, added_keys,
                                        was_action=was_action, view=view,
                                        parsed1=parsed1, parsed2=parsed2):
            continue
        elif parsed1[key] == parsed2[key]:
            view[key] = {'nested': diff_parsed(parsed1[key], parsed2[key],
                                               was_action=True)}
            check_action(was_action, 'same', view[key])
        elif (not isinstance(parsed1[key], dict)
              or not isinstance(parsed2[key], dict)):
            view[key] = {'nested': [diff_parsed(parsed1[key], was_action=True),
                                    diff_parsed(parsed2[key], was_action=True)]}
            check_action(was_action, 'updated', view[key])
        else:
            view[key] = {'nested': diff_parsed(parsed1[key], parsed2[key])}

    return view


def check_action(was_action, action, key_of_view):
    if not was_action:
        key_of_view['action'] = action


def key_in_added_or_removed_keys(key, removed_keys, added_keys, **kwargs):
    action = None
    parsed = None
    if key in removed_keys:
        parsed = kwargs['parsed1']
        action = 'removed'
    elif key in added_keys:
        parsed = kwargs['parsed2']
        action = 'added'
    if action:
        kwargs['view'][key] = {'nested': diff_parsed(parsed[key],
                                                     was_action=True)}
        check_action(kwargs['was_action'], action, kwargs['view'][key])
        return True
    return False
