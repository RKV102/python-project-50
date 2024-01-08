import json


def parse_json(file_path):
    with open(file_path) as file_content:
        parsed_content = json.load(file_content)
    return parsed_content
