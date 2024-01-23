import pytest
import json
import yaml
from gendiff.diff_generator import diff_parsed
from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff
with open('./tests/fixtures/first_input.json') as first_input_json:
    first_input_json_content = json.load(first_input_json)
with open('./tests/fixtures/second_input.json') as second_input_json:
    second_input_json_content = json.load(second_input_json)
with open('./tests/fixtures/first_input.yml') as first_input_yml:
    first_input_yml_content = yaml.load(first_input_yml, Loader=yaml.Loader)
with open('./tests/fixtures/second_input.yml') as second_input_yml:
    second_input_yml_content = yaml.load(second_input_yml, Loader=yaml.Loader)


@pytest.mark.parametrize('input, expected', [
    ((first_input_json_content, second_input_json_content), json_diff),
    ((first_input_yml_content, second_input_yml_content), yaml_diff)
])
def test_diff_parsed(input, expected):
    assert diff_parsed(*input) == expected
