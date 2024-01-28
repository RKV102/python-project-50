import pytest
from gendiff.diff_generator import generate_diff
from gendiff.file_handler import get_file_path, load_file


first_json = get_file_path('first.json')
second_json = get_file_path('second.json')
first_yml = get_file_path('first.yml')
second_yml = get_file_path('second.yml')
stylish_json = load_file('stylish_json.txt')
stylish_yml = load_file('stylish_yml.txt')
plain_json = load_file('plain_json.txt')
plain_yml = load_file('plain_yml.txt')


@pytest.mark.parametrize('input1, input2, formatter, expected', [
    (first_json, second_json, 'stylish', stylish_json),
    (first_yml, second_yml, 'stylish', stylish_yml),
    (first_json, second_json, 'plain', plain_json),
    (first_yml, second_yml, 'plain', plain_yml)
])
def test_generate_diff(input1, input2, formatter, expected):
    assert generate_diff(input1, input2, formatter) == expected
