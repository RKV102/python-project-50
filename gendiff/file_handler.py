FILE_PATH_START = './tests/fixtures/'


def get_file_path(file_name):
    return f'{FILE_PATH_START}{file_name}'


def load_file(file_name):
    file_path = get_file_path(file_name)
    with open(file_path) as opened_file:
        return opened_file.read()
