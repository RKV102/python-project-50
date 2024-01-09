from gendiff.parsers import json_parser, yaml_parser


def gendiff(*file_paths):
    parsed_content = []
    for file_path in file_paths:
        match file_path.endswith('json'):
            case True:
                parsed_content.append(json_parser.parse(file_path))
            case _:
                match file_path.endswith(('yml', 'yaml')):
                    case True:
                        parsed_content.append(yaml_parser.parse(file_path))
                    case _:
                        print(f'Unsupported file type. See: "{file_path}"')
                        return
    diff = diff_parsed(*parsed_content)
    print(diff)
    return diff


def diff_parsed(parsed_content_1, parsed_content_2):
    keys_1 = parsed_content_1.keys()
    keys_2 = parsed_content_2.keys()
    united_keys = unite_keys(keys_1, keys_2)
    united_keys.sort()
    diff = '{\n'
    for key in united_keys:
        match key in keys_1:
            case True:
                value_1 = parsed_content_1[key]
                match key in keys_2:
                    case True:
                        value_2 = parsed_content_2[key]
                        match value_1 == value_2:
                            case True:
                                diff = f'{diff}    {key}: {value_1}\n'
                            case _:
                                diff = f'{diff}  - {key}: {value_1}\n'
                                diff = f'{diff}  + {key}: {value_2}\n'
                    case _:
                        diff = f'{diff}  - {key}: {value_1}\n'
            case _:
                value_2 = parsed_content_2[key]
                diff = f'{diff}  + {key}: {value_2}\n'
    diff += '}'
    return diff


def unite_keys(keys_1, keys_2):
    set_1 = set(keys_1)
    set_2 = set(keys_2)
    union_set = set_1.union(set_2)
    united_keys = list(union_set)
    return united_keys
