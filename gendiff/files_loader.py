from os.path import splitext
import json
import yaml


ACTIONS_FOR_FILE_EXTENSIONS = {
    '.txt': lambda file_content: file_content.read(),
    '.json': lambda file_content: json.load(file_content),
    '.yml': lambda file_content: yaml.load(file_content, Loader=yaml.Loader),
    '.yaml': lambda file_content: yaml.load(file_content, Loader=yaml.Loader)
}


def load_files(*file_names):
    files = {}
    for file_name in ('diff.json', 'diff.yml', *file_names):
        _, file_extension = splitext(file_name)
        file_path = f'./tests/fixtures/{file_name}'
        with open(file_path) as file_content:
            files[file_name] = ACTIONS_FOR_FILE_EXTENSIONS[file_extension](
                file_content
            )
    return files
