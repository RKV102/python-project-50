from gendiff.gendiff import diff_parsed
from gendiff.parsers import json_parser, yaml_parser


def test_diff_parsed():

    # JSON-тестирование
    file_path_1 = './tests/fixtures/first_file.json'
    first_parsed = json_parser.parse(file_path_1)
    file_path_2 = './tests/fixtures/second_file.json'
    second_parsed = json_parser.parse(file_path_2)
    file_path_3 = './tests/fixtures/json_sample.txt'
    with open(file_path_3) as sample:
        sample_content = sample.read()
    assert diff_parsed(first_parsed, second_parsed) == sample_content

    # YML/YAML-тестирование
    file_path_1 = './tests/fixtures/first_file.yaml'
    first_parsed = yaml_parser.parse(file_path_1)
    file_path_2 = './tests/fixtures/second_file.yaml'
    second_parsed = yaml_parser.parse(file_path_2)
    file_path_3 = './tests/fixtures/yaml_sample.txt'
    with open(file_path_3) as sample:
        sample_content = sample.read()
    assert diff_parsed(first_parsed, second_parsed) == sample_content
