from gendiff.parsers import json_parser


def gendiff(file_path_1, file_path_2):
    parsed_content_1 = json_parser.parse(file_path_1)
    parsed_content_2 = json_parser.parse(file_path_2)
    diff = diff_content(parsed_content_1, parsed_content_2)
    print(diff)


def diff_content(parsed_content_1, parsed_content_2):
    first_keys = get_keys(parsed_content_1)
    second_keys = get_keys(parsed_content_2)
    united_keys = unite_keys(first_keys, second_keys)
    united_sorted_keys = sort_keys(united_keys)
    diff = '{\n'
    for key in united_sorted_keys:
        if key in first_keys:
            first_value = get_value(key, parsed_content_1)
            if key in second_keys:
                second_value = get_value(key, parsed_content_2)
                if first_value == second_value:
                    diff = f'{diff}    {key}: {first_value}\n'
                else:
                    diff = f'{diff}  - {key}: {first_value}\n'
                    diff = f'{diff}  + {key}: {second_value}\n'
            else:
                diff = f'{diff}  - {key}: {first_value}\n'
        else:
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


def sort_keys(keys):
    keys.sort()
    return keys


def get_keys(parsed_content):
    return list(parsed_content.keys())


def get_value(key, parsed_content):
    return parsed_content[key]


def get_item(iterable):
    return iterable.pop(0)
