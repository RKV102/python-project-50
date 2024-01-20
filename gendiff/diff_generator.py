import json
import yaml
from gendiff.parsers_runner import run_parser
import gendiff.formatters as formatters


ACTIONS_FOR_FORMATTERS = {
    'stylish': lambda diff: formatters.stylish.format(diff),
    'plain': lambda diff: formatters.plain.format(diff)
}
ACTIONS_FOR_FILE_EXTENSIONS = {
    'json': lambda file_path: run_parser(file_path, json),
    'yaml': lambda file_path: run_parser(file_path, yaml, yaml.Loader),
    'yml': lambda file_path: run_parser(file_path, yaml, yaml.Loader)
}


def generate_diff(formatter, *file_paths):
    parsed_content = []
    for file_path in file_paths:
        file_extension = get_file_extension(file_path)
        if ACTIONS_FOR_FILE_EXTENSIONS.get(file_extension):
            parsed_content.append(
                ACTIONS_FOR_FILE_EXTENSIONS[file_extension](file_path)
            )
        else:
            print(f'Unsupported file type. See: {file_path}')
            return
    diff = diff_parsed(*parsed_content)
    print(ACTIONS_FOR_FORMATTERS[formatter](diff)) \
        if ACTIONS_FOR_FORMATTERS.get(formatter) \
        else print('Unsupported format')


def diff_parsed(parsed_content_1, parsed_content_2):
    keys_1, keys_2 = set(parsed_content_1.keys()), set(parsed_content_2.keys())
    removed_keys = keys_1.difference(keys_2)
    added_keys = keys_2.difference(keys_1)
    united_keys = list(keys_1.union(keys_2))
    united_keys.sort()
    diff = {}
    for key in united_keys:
        if key in removed_keys:
            diff[key] = (parsed_content_1[key], '-')
        elif key in added_keys:
            diff[key] = (parsed_content_2[key], '+')
        elif parsed_content_1[key] == parsed_content_2[key]:
            diff[key] = (parsed_content_1[key], '=')
        elif not isinstance(parsed_content_1[key], dict) or \
                not isinstance(parsed_content_2[key], dict):
            diff[key] = (parsed_content_1[key], parsed_content_2[key], '+-')
        else:
            diff[key] = diff_parsed(parsed_content_1[key],
                                    parsed_content_2[key])
    return diff


def get_file_extension(file_path):
    extension_name_start = file_path.rfind('.') + 1
    return file_path[extension_name_start:] if extension_name_start else None
