from gendiff.gendiff import gendiff


def test_generate_diff():
    path_1 = './gendiff/compared/first_file.json'
    path_2 = './gendiff/compared/second_file.json'
    with open('./tests/fixtures/json_verification.txt') as f:
        json_string = f.read()
    assert gendiff(path_1, path_2) == json_string
