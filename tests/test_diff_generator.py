import pytest
from gendiff.diff_generator import diff_views
from gendiff.files_loader import load_files


files = load_files('view1.json', 'view2.json', 'view1.yml', 'view2.yml')


@pytest.mark.parametrize('input, expected', [
    ((files['view1.json'], files['view2.json']), files['diff.json']),
    ((files['view1.yml'], files['view2.yml']), files['diff.yml'])
])
def test_diff_views(input, expected):
    assert diff_views(*input) == expected
