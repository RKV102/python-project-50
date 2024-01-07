from gendiff.parsers import json_parser


def gendiff(file_path_1, file_path_2):
    parsed_content_1 = json_parser.parse(file_path_1)
    parsed_content_2 = json_parser.parse(file_path_2)
    diff = diff_parsed(parsed_content_1, parsed_content_2)
    print(diff)


def diff_parsed(parsed_content_1, parsed_content_2):
    first_keys = get_keys(parsed_content_1)
    second_keys = get_keys(parsed_content_2)
    united_keys = unite_keys(first_keys, second_keys)
    united_keys.sort()
    diff = '{\n'
    for key in united_keys:
        match key in first_keys:
            case True:
                first_value = get_value(key, parsed_content_1)
                match key in second_keys:
                    case True:
                        second_value = get_value(key, parsed_content_2)
                        match first_value == second_value:
                            case True:
                                diff = f'{diff}    {key}: {first_value}\n'
                            case _:
                                diff = f'{diff}  - {key}: {first_value}\n'
                                diff = f'{diff}  + {key}: {second_value}\n'
                    case _:
                        diff = f'{diff}  - {key}: {first_value}\n'
            case _:
                second_value = get_value(key, parsed_content_2)
                diff = f'{diff}  + {key}: {second_value}\n'
    diff += '}'
    return diff


def unite_keys(first_keys, second_keys):
    first_set = set(first_keys)
    second_set = set(second_keys)
    union_set = first_set.union(second_set)
    united_keys = list(union_set)
    return united_keys


def get_keys(parsed_content):
    return list(parsed_content.keys())


def get_value(key, parsed_content):
    return parsed_content[key]
