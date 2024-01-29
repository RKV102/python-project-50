import pytest
from gendiff.diff_generator import generate_diff
from tests.fixture_handler import get_fixture_path, load_fixture_content


@pytest.mark.parametrize('input1, input2, formatter, expected', [
    (get_fixture_path('first.json'), get_fixture_path('second.json'), 'stylish',
     load_fixture_content('stylish_json.txt')),
    (get_fixture_path('first.yml'), get_fixture_path('second.yml'), 'stylish',
     load_fixture_content('stylish_yml.txt')),
    (get_fixture_path('first.json'), get_fixture_path('second.json'), 'plain',
     load_fixture_content('plain_json.txt')),
    (get_fixture_path('first.yml'), get_fixture_path('second.yml'), 'plain',
     load_fixture_content('plain_yml.txt'))
])
def test_generate_diff(input1, input2, formatter, expected):
    assert generate_diff(input1, input2, formatter) == expected
