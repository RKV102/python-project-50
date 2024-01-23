import pytest
from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff
from gendiff.formatters.stylish import format
FILE_PATH_START = './tests/fixtures/'
FILE_EXTENSIONS = '.txt'
samples = {}
for i in ('json', 'yaml'):
    with open(f'{FILE_PATH_START}stylish_{i}{FILE_EXTENSIONS}') \
            as sample:
        samples[i] = sample.read()


@pytest.mark.parametrize('input, expected', [
    (json_diff, samples['json']),
    (yaml_diff, samples['yaml'])
])
def test_format(input, expected):
    assert format(input) == expected
