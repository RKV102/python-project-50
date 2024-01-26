import pytest
from gendiff.diff_generator import diff_views, is_right_formatter
from gendiff.diff_generator import create_view, parse_file
from gendiff.files_loader import load_files


files = load_files(
    'view1.json',
    'view2.json',
    'view1.yml',
    'view2.yml',
    'file.json',
    'file.yml'
)


@pytest.mark.parametrize('input, expected', [
    ((files['view1.json'], files['view2.json']), files['diff.json']),
    ((files['view1.yml'], files['view2.yml']), files['diff.yml'])
])
def test_diff_views(input, expected):
    assert diff_views(*input) == expected


@pytest.mark.parametrize('input, expected', [
    ('stylish', True),
    ('plain', True),
    ('json', True),
    ('unknown', False)
])
def test_is_right_formatter(input, expected):
    assert is_right_formatter(input) == expected


def test_parse_file():
    assert parse_file('unknown.png') is None


@pytest.mark.parametrize('input, expected', [
    (files['file.json'], files['view1.json']),
    (files['file.yml'], files['view1.yml'])
])
def test_create_view(input, expected):
    assert create_view(input) == expected
