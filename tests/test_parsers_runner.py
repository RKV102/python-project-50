from gendiff.parsers_runner import run_parser


def test_run_parser():
    assert run_parser(f'./tests/fixtures/unknown.png', '_') is None
