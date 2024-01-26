import pytest
from gendiff.formatters.stylish import format
from gendiff.files_loader import load_files


files = load_files('stylish_json.txt', 'stylish_yml.txt')


@pytest.mark.parametrize('input, expected', [
    (files['diff.json'], files['stylish_json.txt']),
    (files['diff.yml'], files['stylish_yml.txt'])
])
def test_format(input, expected):
    assert format(input) == expected
