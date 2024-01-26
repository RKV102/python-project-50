import pytest
from gendiff.formatters.plain import format
from gendiff.files_loader import load_files


files = load_files('plain_json.txt', 'plain_yml.txt')


@pytest.mark.parametrize('input, expected', [
    (files['diff.json'], files['plain_json.txt']),
    (files['diff.yml'], files['plain_yml.txt'])
])
def test_format(input, expected):
    assert format(input) == expected
