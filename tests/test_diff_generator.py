import pytest
from gendiff.diff_generator import generate_diff
from gendiff.file_handler import get_file_path, load_file


@pytest.mark.parametrize('input1, input2, formatter, expected', [
    (get_file_path('first.json'), get_file_path('second.json'), 'stylish',
     load_file('stylish_json.txt')),
    (get_file_path('first.yml'), get_file_path('second.yml'), 'stylish',
     load_file('stylish_yml.txt')),
    (get_file_path('first.json'), get_file_path('second.json'), 'plain',
     load_file('plain_json.txt')),
    (get_file_path('first.yml'), get_file_path('second.yml'), 'plain',
     load_file('plain_yml.txt'))
])
def test_generate_diff(input1, input2, formatter, expected):
    assert generate_diff(input1, input2, formatter) == expected
