from gendiff.parsers_runner import run_parser


def test_run_parser():
    assert run_parser('./tests/fixtures/unknown.png', '_') is None
