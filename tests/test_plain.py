from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff
from gendiff.formatters.plain import format
JSON_SAMPLE_PATH = './tests/fixtures/plain_json.txt'
YAML_SAMPLE_PATH = './tests/fixtures/plain_yaml.txt'


def test_format():

    # JSON-тестирование
    with open(JSON_SAMPLE_PATH) as json_sample:
        json_sample_content = json_sample.read()
    assert format(json_diff) == json_sample_content

    # YAML-тестирование
    with open(YAML_SAMPLE_PATH) as yaml_sample:
        yaml_sample_content = yaml_sample.read()
    assert format(yaml_diff) == yaml_sample_content
