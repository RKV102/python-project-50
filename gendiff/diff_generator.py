import json
import yaml
from os.path import splitext
from gendiff.parsers_runner import run_parser
import gendiff.formatters as formatters


ACTIONS_FOR_FORMATTERS = {
    'stylish': lambda diff: formatters.stylish.format(diff),
    'plain': lambda diff: formatters.plain.format(diff),
    'json': lambda diff: json.dumps(
        diff,
        indent=formatters.stylish.INDENT_LEN
    )
}
ACTIONS_FOR_FILE_EXTENSIONS = {
    '.json': lambda file_path: run_parser(file_path, json),
    '.yaml': lambda file_path: run_parser(file_path, yaml, yaml.Loader),
    '.yml': lambda file_path: run_parser(file_path, yaml, yaml.Loader)
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    parsed_file1 = parse_file(file_path1)
    parsed_file2 = parse_file(file_path2)
    if not is_right_formatter(formatter) \
            or not parsed_file1 \
            or not parsed_file2:
        return
    view1 = create_view(parsed_file1)
    view2 = create_view(parsed_file2)
    diff = diff_views(view1, view2)
    formatted_diff = ACTIONS_FOR_FORMATTERS[formatter](diff)
    print(formatted_diff)
    return formatted_diff


def diff_views(view1, view2):
    keys1 = set(view1.keys())
    keys2 = set(view2.keys())
    removed_keys = keys1.difference(keys2)
    added_keys = keys2.difference(keys1)
    united_keys = list(keys1.union(keys2))
    united_keys.sort()
    diff = {}
    for key in united_keys:
        if key in removed_keys:
            diff[key] = {
                'nested': view1[key]['nested'],
                'action': 'removed'
            }
        elif key in added_keys:
            diff[key] = {
                'nested': view2[key]['nested'],
                'action': 'added'
            }
        elif view1[key] == view2[key]:
            diff[key] = {
                'nested': view1[key]['nested'],
                'action': 'same'
            }
        elif not isinstance(view1[key]['nested'], dict) or \
                not isinstance(view2[key]['nested'], dict):
            diff[key] = {
                'nested': [view1[key]['nested'], view2[key]['nested']],
                'action': 'updated'
            }
        else:
            diff[key] = {
                'nested': diff_views(
                    view1[key]['nested'],
                    view2[key]['nested']
                )
            }
    return diff


def parse_file(file_path):
    _, file_extension = splitext(file_path)
    try:
        return ACTIONS_FOR_FILE_EXTENSIONS[file_extension](file_path)
    except KeyError:
        print(f'Unsupported file type. See: {file_path}')


def create_view(parsed_content):
    view = {}
    for item in parsed_content.items():
        key = item[0]
        value = item[1]
        if not isinstance(value, dict):
            view[key] = {'nested': value}
        else:
            view[key] = {'nested': create_view(value)}
    return view


def is_right_formatter(formatter):
    try:
        ACTIONS_FOR_FORMATTERS[formatter]
        return True
    except KeyError:
        print('Unsupported format')
        return False
