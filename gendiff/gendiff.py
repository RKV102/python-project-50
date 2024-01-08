from gendiff import parsers


def gendiff(file_path_1, file_path_2, format_):
    match format_:
        case 'json':
            parsed_content_1 = parsers.json_parser.parse_json(file_path_1)
            parsed_content_2 = parsers.json_parser.parse_json(file_path_2)
        case 'yaml':
            parsed_content_1 = parsers.json_parser.parse_yaml(file_path_1)
            parsed_content_2 = parsers.json_parser.parse_yaml(file_path_2)
    diff = diff_parsed(parsed_content_1, parsed_content_2)
    print(diff)


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
