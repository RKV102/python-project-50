import json
import yaml
from os.path import splitext
from gendiff.parsers_runner import run_parser


def parse_file(file_path):
    _, file_extension = splitext(file_path)
    match file_extension:
        case '.json':
            return run_parser(file_path, json)
        case '.yaml' | '.yml':
            return run_parser(file_path, yaml, yaml.Loader)
        case _:
            raise ValueError(f'Unsupported file type. See: {file_path}')
