#!/usr/bin/env python3
from gendiff.gendiff import gendiff, get_item


def main():
    args = parse_arg()
    first_file = get_item(args)
    second_file = get_item(args)
    gendiff(first_file, second_file)


def parse_arg():
    parser = argparse.ArgumentParser(description='Compares two '
                                     + 'configuration files and '
                                     + 'shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    return [args.first_file, args.second_file]


if __name__ == '__main__':
    main()
