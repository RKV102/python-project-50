import argparse


def parse():
    parser = argparse.ArgumentParser(description='Compares two '
                                                 + 'configuration files and '
                                                 + 'shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', dest='format',
                        help='set format of output.')
    return (
        parser.parse_args().first_file,
        parser.parse_args().second_file,
        parser.parse_args().format
    )
