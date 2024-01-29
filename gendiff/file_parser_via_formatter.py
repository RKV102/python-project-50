import json
import yaml
from os.path import splitext


def parse_file(file_path):
    _, file_extension = splitext(file_path)
    match file_extension:
        case '.json':
            return run_parser(file_path, json)
        case '.yaml' | '.yml':
            return run_parser(file_path, yaml, yaml.Loader)
        case _:
            raise ValueError(f'Unsupported file type. See: {file_path}')


def run_parser(file_path, parser, parser_loader=None):
    try:
        with open(file_path) as opened_file:
            return (parser.load(opened_file) if not parser_loader
                    else parser.load(opened_file, Loader=parser_loader))
    except FileNotFoundError:
        raise FileNotFoundError(f'No such file or directory. See: {file_path}')
