import pytest
from tests.fixtures.json_diff import diff as json_diff
from tests.fixtures.yaml_diff import diff as yaml_diff
from tests.test_stylish import FILE_PATH_START, FILE_EXTENSIONS
from gendiff.formatters.plain import format
samples = {}
for i in ('json', 'yaml'):
    with open(f'{FILE_PATH_START}plain_{i}{FILE_EXTENSIONS}') \
            as sample:
        samples[i] = sample.read()


@pytest.mark.parametrize('input, expected', [
    (json_diff, samples['json']),
    (yaml_diff, samples['yaml'])
])
def test_format(input, expected):
    assert format(input) == expected
