from tests.fixtures.diff import diff
from gendiff.formatters import stylish


def test_format():
    stylish_diff_path = './tests/fixtures/json_stylish_diff.txt'
    with open(stylish_diff_path) as stylish_diff:
        stylish_diff_content = stylish_diff.read()
    assert stylish.format(diff) == stylish_diff_content
