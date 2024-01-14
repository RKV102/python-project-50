import json
import yaml
from gendiff.parser_runner import run_parser


def generate_diff(*file_paths):
    parsed_content = []
    for file_path in file_paths:
        match file_path.endswith('json'):
            case True:
                parsed_content.append(run_parser(file_path, json))
            case _:
                match file_path.endswith(('yml', 'yaml')):
                    case True:
                        parsed_content.append(run_parser(
                            file_path, yaml, yaml.Loader
                        ))
                    case _:
                        print(f'Unsupported file type. See: "{file_path}"')
                        return
    diff = diff_parsed(*parsed_content)
    return diff


def diff_parsed(parsed_content_1, parsed_content_2):

    def inner(key, parsed_content_1, parsed_content_2):
        value_1, value_2 = 'null', 'null'
        for num, parsed_content in enumerate((parsed_content_1,
                                              parsed_content_2), start=1):
            if key in parsed_content:
                if num == 1:
                    value_1 = parsed_content[key]
                else:
                    value_2 = parsed_content[key]
        for num, value in enumerate((value_1, value_2), start=1):
            if value == 'null':
                if num == 1:
                    return {key: (value_2, '+')}
                return {key: (value_1, '-')}
        if value_1 == value_2:
            return {key: (value_1, '=')}
        if not isinstance(value_1, dict) or not isinstance(value_2, dict):
            return {key: (value_1, value_2, '±')}
        return {key: diff_parsed(value_1, value_2)}

    keys_1, keys_2 = parsed_content_1.keys(), parsed_content_2.keys()
    united_keys = list(set(keys_1).union(set(keys_2)))
    united_keys.sort()
    return list(map(lambda key: inner(key, parsed_content_1, parsed_content_2),
                    united_keys))
