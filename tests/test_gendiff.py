from gendiff import generate_diff


def test_generate_diff():
    path_1 = './gendiff/compared/first_file.json'
    path_2 = './gendiff/compared/second_file.json'
    str_ = '{\n  - follow: False\n'\
           + '    host: hexlet.io\n'\
           + '  - proxy: 123.234.53.22\n'\
           + '  - timeout: 50\n'\
           + '  + timeout: 20\n'\
           + '  + verbose: True\n}'
    assert generate_diff(path_1, path_2) == str_
