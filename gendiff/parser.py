import json
import yaml
from os.path import splitext


def run_to_parse(file_path):
    _, file_extension = splitext(file_path)
    with open(file_path) as file_content:
        return parse(file_content, file_extension)


def parse(file_content, file_extension):
    match file_extension[1:]:
        case 'json':
            return json.load(file_content)
        case 'yaml' | 'yml':
            return yaml.load(file_content, Loader=yaml.Loader)
        case _:
            raise ValueError(f'Unsupported file type.')
