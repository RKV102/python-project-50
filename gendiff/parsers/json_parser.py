import json


def parse(file_path):
    with open(file_path) as file_content:
        parsed_content = json.load(file_content)
    return parsed_content
