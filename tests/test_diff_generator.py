import pytest
from gendiff.diff_generator import generate_diff
from tests import get_fixture_path, load_fixture_content


@pytest.mark.parametrize('input1, input2, formatter, output', [
    ('first.json', 'second.json', 'stylish', 'stylish_json.txt'),
    ('first.yml', 'second.yml', 'stylish', 'stylish_yml.txt'),
    ('first.json', 'second.json', 'plain', 'plain_json.txt'),
    ('first.yml', 'second.yml', 'plain', 'plain_yml.txt')
])
def test_generate_diff(input1, input2, formatter, output):
    assert generate_diff(
        get_fixture_path(input1),
        get_fixture_path(input2),
        formatter
    ) == load_fixture_content(get_fixture_path(output))
