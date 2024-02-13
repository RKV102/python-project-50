from gendiff.parser import parse
from gendiff.formatters.diff_formatter import format_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    parsed_file1 = parse(file_path1)
    parsed_file2 = parse(file_path2)
    diff = diff_parsed(parsed_file1, parsed_file2)
    return format_diff(formatter, diff)


def diff_parsed(parsed1, parsed2):
    view = {}
    keys1 = set(parsed1.keys())
    keys2 = set(parsed2.keys())
    removed_keys = keys1.difference(keys2)
    added_keys = keys2.difference(keys1)
    united_keys = list(keys1.union(keys2))
    united_keys.sort()
    for key in united_keys:
        if key in removed_keys:
            view[key] = (parsed1[key], 'removed')
        elif key in added_keys:
            view[key] = (parsed2[key], 'added')
        elif parsed1[key] == parsed2[key]:
            view[key] = (parsed1[key], 'same')
        elif isinstance(parsed1[key], dict) and isinstance(parsed2[key], dict):
            view[key] = (diff_parsed(parsed1[key], parsed2[key]), 'nested')
        else:
            view[key] = ((parsed1[key], parsed2[key]), 'updated')
    return view
