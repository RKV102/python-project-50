from gendiff.diff_generator import diff_parsed
from tests.fixtures.first_parsed_json import parsed as json_1
from tests.fixtures.second_parsed_json import parsed as json_2
from tests.fixtures.first_parsed_yaml import parsed as yaml_1
from tests.fixtures.second_parsed_yaml import parsed as yaml_2
from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff


def test_diff_parsed():

    # JSON-тестирование
    assert diff_parsed(json_1, json_2) == json_diff

    # YAML-тестирование
    assert diff_parsed(yaml_1, yaml_2) == yaml_diff
