import pytest
import json
import yaml
from gendiff.diff_generator import diff_parsed
from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff
with open('./tests/fixtures/first.json') as first_json:
    first_parsed_json = json.load(first_json)
with open('./tests/fixtures/second.json') as second_json:
    second_parsed_json = json.load(second_json)
with open('./tests/fixtures/first.yml') as first_yml:
    first_parsed_yml = yaml.load(first_yml, Loader=yaml.Loader)
with open('./tests/fixtures/second.yml') as second_yml:
    second_parsed_yml = yaml.load(second_yml, Loader=yaml.Loader)


@pytest.mark.parametrize('input, expected', [
    ((first_parsed_json, second_parsed_json), json_diff),
    ((first_parsed_yml, second_parsed_yml), yaml_diff)
])
def test_diff_parsed(input, expected):
    assert diff_parsed(*input) == expected
