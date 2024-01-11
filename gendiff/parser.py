def parse(file_path, parser, loader=None):
    with open(file_path) as file_content:
        parsed_content = parser.load(file_content) if not loader\
            else parser.load(file_content, Loader=loader)
    return parsed_content
