import json
import gendiff.formatters as formatters


def generate_diff(file_path1, file_path2, formatter='stylish'):
    parsed_file1 = formatters.file_parser.parse_file(file_path1)
    parsed_file2 = formatters.file_parser.parse_file(file_path2)
    view1 = create_view(parsed_file1)
    view2 = create_view(parsed_file2)
    diff = diff_views(view1, view2)
    match formatter:
        case 'stylish':
            formatted_diff = formatters.stylish.format(diff)
        case 'plain':
            formatted_diff = formatters.plain.format(diff)
        case 'json':
            formatted_diff = json.dumps(
                diff,
                indent=formatters.stylish.INDENT_LEN
            )
        case _:
            raise ValueError('Unsupported format')
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
