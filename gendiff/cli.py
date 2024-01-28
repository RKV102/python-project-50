import argparse


def run_argparse():
    parser = argparse.ArgumentParser(description='Compares two '
                                                 + 'configuration files and '
                                                 + 'shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        default='stylish', dest='format',
                        help='set format of output.')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
