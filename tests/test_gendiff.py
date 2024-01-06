from gendiff.gendiff import diff_content
from gendiff.parsers.json_parser import parse


def test_diff_content():
    first_file = './tests/fixtures/first_file.json'
    with open(first_file) as f1:
        first_content = f1.read()
        first_parsed = parse(first_content)
    second_file = './tests/fixtures/second_file.json'
    with open(second_file) as f2:
        second_content = f2.read()
        second_parsed = parse(second_content)
    sample_file = './tests/fixtures/json_verification.txt'
    with open(sample_file) as sample:
        sample_content = sample.read()
    assert diff_content(first_content, second_content) == sample_content
