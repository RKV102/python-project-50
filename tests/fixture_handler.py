from os.path import join


FIXTURE_PATH_START = join('.', 'tests', 'fixtures')


def get_fixture_path(fixture_name):
    return join(FIXTURE_PATH_START, fixture_name)


def load_fixture_content(fixture_name):
    fixture_path = get_fixture_path(fixture_name)
    with open(fixture_path) as opened_fixture:
        return opened_fixture.read()
