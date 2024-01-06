import json


def parse(first_file, second_file):
    with open(first_file) as f1:
        with open(second_file) as f2:
            f1_content = json.load(f1)
            f2_content = json.load(f2)
    return [f1_content, f2_content]
