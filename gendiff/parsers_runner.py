def run_parser(file_path, parser, loader=None):
    try:
        with open(file_path) as file_content:
            parsed_content = parser.load(file_content) if not loader\
                else parser.load(file_content, Loader=loader)
        return parsed_content
    except FileNotFoundError:
        raise FileNotFoundError(f'No such file or directory. See: {file_path}')
