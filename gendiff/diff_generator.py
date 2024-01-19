import json
import yaml
from gendiff.parsers_runner import run_parser
import gendiff.formatters as formatters


ACTIONS_FOR_FORMATS = {
    'stylish': lambda diff: formatters.stylish.format(diff),
    'plain': lambda diff: formatters.plain.format(diff)
}


def generate_diff(format, *file_paths):
    parsed_content = []
    for file_path in file_paths:
        if file_path.endswith('json'):
            parsed_content.append(run_parser(file_path, json))
        elif file_path.endswith(('yml', 'yaml')):
            parsed_content.append(run_parser(file_path, yaml, yaml.Loader))
        else:
            print(f'Unsupported file type. See: "{file_path}"')
            return
    diff = diff_parsed(*parsed_content)
    print(ACTIONS_FOR_FORMATS[format](diff)) \
        if ACTIONS_FOR_FORMATS.get(format) \
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
        elif not isinstance(parsed_content_1[key], dict) or\
                not isinstance(parsed_content_2[key], dict):
            diff[key] = (parsed_content_1[key], parsed_content_2[key], '+-')
        else:
            diff[key] = diff_parsed(parsed_content_1[key],
                                    parsed_content_2[key])
    return diff
