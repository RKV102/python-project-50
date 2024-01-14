from gendiff.gendiff import generate_diff


def test_diff_parsed():

    # JSON-тестирование
    file_path_1 = './tests/fixtures/first_file.json'
    file_path_2 = './tests/fixtures/second_file.json'
    file_path_3 = './tests/fixtures/json_sample.txt'
    with open(file_path_3) as sample:
        sample_content = sample.read()
    assert str(generate_diff(file_path_1, file_path_2)) == sample_content

    # YML/YAML-тестирование
    file_path_1 = './tests/fixtures/first_file.yaml'
    file_path_2 = './tests/fixtures/second_file.yaml'
    file_path_3 = './tests/fixtures/yaml_sample.txt'
    with open(file_path_3) as sample:
        sample_content = sample.read()
    assert str(generate_diff(file_path_1, file_path_2)) == sample_content

    # YAML- и TXT-тестирование
    assert generate_diff(file_path_1, file_path_3) is None
