import json
import yaml
from gendiff import parser


def generate_diff(*file_paths):
    parsed_content = []
    for file_path in file_paths:
        match file_path.endswith('json'):
            case True:
                parsed_content.append(parser.parse(file_path, json))
            case _:
                match file_path.endswith(('yml', 'yaml')):
                    case True:
                        parsed_content.append(parser.parse(
                            file_path, yaml, yaml.Loader
                        ))
                    case _:
                        print(f'Unsupported file type. See: "{file_path}"')
                        return
    diff = diff_parsed(*parsed_content)
    print(diff)
    return diff


def diff_parsed(parsed_content_1, parsed_content_2):

    def unite_keys(keys_1, keys_2):
        return list(set(keys_1).union(set(keys_2)))

    def inner(key, value_1, value_2, parsed_content_1, parsed_content_2):
        if key in parsed_content_1:
            value_1 = parsed_content_1[key]
        if key in parsed_content_2:
            value_2 = parsed_content_2[key]
        if value_1 == 'null':
            return {key: (value_2, '+')}
        if value_2 == 'null':
            return {key: (value_1, '-')}
        if not isinstance(value_1, dict) or not isinstance(value_2, dict):
            if value_1 == value_2:
                return {key: (value_1, '=')}
            return {key: (value_1, value_2, '±')}
        return {key: diff_parsed(value_1, value_2)}

    keys_1, keys_2 = parsed_content_1.keys(), parsed_content_2.keys()
    united_keys = unite_keys(keys_1, keys_2)
    united_keys.sort()
    value_1, value_2 = 'null', 'null'
    return list(map(lambda key: inner(key, value_1, value_2,
                                      parsed_content_1, parsed_content_2),
                    united_keys))
