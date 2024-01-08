import yaml


def parse_yaml(file_path):
    with open(file_path) as file_content:
        parsed_content = yaml.load(file_content, Loader=yaml.Loader)
    return parsed_content
