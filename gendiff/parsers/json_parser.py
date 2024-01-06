import json


def generate_diff(first_file, second_file):
    f1_content, f2_content = read_content(first_file, second_file)
    diff = diff_content(f1_content, f2_content)
    return diff


def read_content(first_file, second_file):
    with open(first_file) as f1:
        with open(second_file) as f2:
            f1_content = json.load(f1)
            f2_content = json.load(f2)
    return f1_content, f2_content
