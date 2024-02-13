import json
import yaml
from os.path import splitext


def parse_file(file_path):
    _, file_extension = splitext(file_path)
    with open(file_path) as file_content:
        return load_to_parser(file_content, file_extension, file_path)


def load_to_parser(file_content, file_extension, file_path):
    match file_extension[1:]:
        case 'json':
            return json.load(file_content)
        case 'yaml' | 'yml':
            return yaml.load(file_content, Loader=yaml.Loader)
        case _:
            raise ValueError(f'Unsupported file type. See: {file_path}')
