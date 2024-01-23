import pytest
from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff
from gendiff.formatters.stylish import format
JSON_SAMPLE_PATH = './tests/fixtures/stylish_json.txt'
YAML_SAMPLE_PATH = './tests/fixtures/stylish_yaml.txt'
with open(JSON_SAMPLE_PATH) as json_sample:
    json_sample_content = json_sample.read()
with open(YAML_SAMPLE_PATH) as yaml_sample:
    yaml_sample_content = yaml_sample.read()


@pytest.mark.parametrize('input, expected', [
    (json_diff, json_sample_content),
    (yaml_diff, yaml_sample_content)
])
def test_format(input, expected):
    assert format(input) == expected
