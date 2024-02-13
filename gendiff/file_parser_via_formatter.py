import json
import yaml
from os.path import splitext


def parse_file(file_path):
    _, file_extension = splitext(file_path)
    with open(file_path) as opened_file:
        return load_to_parser(opened_file, file_extension, file_path)


def load_to_parser(opened_file, file_extension, file_path):
    match file_extension:
        case '.json':
            return json.load(opened_file)
        case '.yaml' | '.yml':
            return yaml.load(opened_file, Loader=yaml.Loader)
        case _:
            raise ValueError(f'Unsupported file type. See: {file_path}')
