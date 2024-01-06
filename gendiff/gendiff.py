import argparse
from gendiff.parsers import json_parser


def gendiff():
    args = parse_arg()
    first_file = get_item(args)
    second_file = get_item(args)
    parsed_content = json_parser.parse(first_file, second_file)
    first_content = get_item(parsed_content)
    second_content = get_item(parsed_content)
    diff = diff_content(first_content, second_content)
    print(diff)


def parse_arg():
    parser = argparse.ArgumentParser(description='Compares two '
                                     + 'configuration files and '
                                     + 'shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    return [args.first_file, args.second_file]


def diff_content(f1_content, f2_content):
    f1_keys = get_keys(f1_content)
    f2_keys = get_keys(f2_content)
    united_keys = unite_keys(f1_keys, f2_keys)
    united_sorted_keys = sort_keys(united_keys)
    diff = '{\n'
    for key in united_sorted_keys:
        if key in f1_keys:
            f1_value = get_value(key, f1_content)
            if key in f2_keys:
                f2_value = get_value(key, f2_content)
                if f1_value == f2_value:
                    diff = f'{diff}    {key}: {f1_value}\n'
                else:
                    diff = f'{diff}  - {key}: {f1_value}\n'
                    diff = f'{diff}  + {key}: {f2_value}\n'
            else:
                diff = f'{diff}  - {key}: {f1_value}\n'
        else:
            f2_value = get_value(key, f2_content)
            diff = f'{diff}  + {key}: {f2_value}\n'
    diff += '}'
    return diff


def unite_keys(f1_keys, f2_keys):
    f1_set = set(f1_keys)
    f2_set = set(f2_keys)
    union_set = f1_set.union(f2_set)
    united_keys = list(union_set)
    return united_keys


def sort_keys(f_keys):
    f_keys.sort()
    return f_keys


def get_keys(f_content):
    return list(f_content.keys())


def get_value(key, f_content):
    return f_content[key]


def get_item(iterable):
    return iterable.pop(0)
