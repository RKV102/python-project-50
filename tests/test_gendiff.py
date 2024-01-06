from gendiff.gendiff import diff_parsed
from gendiff.parsers.json_parser import parse


def test_diff_parsed():
    file_path_1 = './tests/fixtures/first_file.json'
    with open(file_path_1) as f1:
        first_parsed = parse(file_path_1)
    file_path_2 = './tests/fixtures/second_file.json'
    with open(file_path_2) as f2:
        second_parsed = parse(file_path_2)
    file_path_3 = './tests/fixtures/json_verification.txt'
    with open(file_path_3) as sample:
        sample_content = sample.read()
    assert diff_parsed(first_parsed, second_parsed) == sample_content
